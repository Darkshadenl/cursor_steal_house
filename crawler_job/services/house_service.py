from typing import AsyncGenerator, Dict, Any, List, Optional, Union, Tuple
import logging
from crawler_job.models.house_models import (
    House,
)
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
import warnings

from .repositories import (
    HouseRepository,
)
from .db_connection import get_db_session
from ..models.db_models import (
    DbHouse,
)
from ..helpers.transformers import (
    db_houses_to_pydantic_async,
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def get_repository(
    session: AsyncSession,
) -> AsyncGenerator[HouseRepository, None]:
    """Context manager to get the house repository with a session"""
    try:
        yield HouseRepository(session)
    finally:
        pass


class HouseService:
    """Service for handling house data storage"""

    def __init__(self, notification_service=None):
        """Initialize with a new database session and optional notification service

        Args:
            notification_service: Optional notification service for sending alerts
        """
        self.session = get_db_session()
        self._closed = False
        self.notification_service = notification_service

    async def __aenter__(self):
        """Enter the context manager"""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager and close the session"""
        await self.close()

    async def close(self):
        """Explicitly close the session"""
        if not self._closed:
            await self.session.close()
            self._closed = True

    def __del__(self):
        """Attempt to clean up resources when object is garbage collected"""
        if not self._closed:
            warnings.warn(
                "HouseService was not properly closed. "
                "Please use 'async with' statement or call 'await service.close()' explicitly.",
                ResourceWarning,
                stacklevel=2,
            )
            # We can't use await in __del__, so we just make a warning

    async def identify_new_houses(self, houses: List[House]) -> List[House]:
        """
        Identify houses that don't exist in the database

        Args:
            houses: List of House objects to check

        Returns:
            List[House]: List of houses that are not in the database
        """
        new_houses = []
        async with get_repository(self.session) as repo:
            for house in houses:
                existing_house = await repo.get_by_address(house.address, house.city)
                if not existing_house:
                    new_houses.append(house)
        return new_houses

    async def store_houses_atomic(
        self,
        houses: List[House],
        all_houses: List[House],
    ) -> Dict[str, int]:
        """
        Store houses in an atomic transaction

        Args:
            houses: List of House objects to store
            all_houses: List of all House objects (including ones not being stored)

        Returns:
            Dict[str, int]: Dictionary with counts of new, existing, and updated houses
        """
        has_active_transaction = self.session.in_transaction()

        async def _execute_transaction():
            async with get_repository(self.session) as repo:
                new_houses, existing_houses, updated_houses = (
                    await self._store_houses_with_repo(houses, repo)
                )

                # Send notifications if notification service is available
                if self.notification_service:
                    # Send notifications for new houses
                    if new_houses:
                        logger.info(
                            f"Sending notifications for {len(new_houses)} new houses"
                        )
                        for house in new_houses:
                            try:
                                await self.notification_service.send_new_house_notification(
                                    house
                                )
                            except Exception as e:
                                logger.error(
                                    f"Failed to send notification for {house.address}: {e}",
                                    exc_info=True,
                                )

                    # Send notifications for updated houses
                    if updated_houses:
                        logger.info(
                            f"Sending notifications for {len(updated_houses)} updated houses"
                        )
                        for house, old_status in updated_houses:
                            try:
                                await self.notification_service.send_updated_house_notification(
                                    house, old_status
                                )
                            except Exception as e:
                                logger.error(
                                    f"Failed to send update notification for {house.address}: {e}",
                                    exc_info=True,
                                )

                return {
                    "new_count": len(new_houses),
                    "existing_count": len(existing_houses),
                    "updated_count": len(updated_houses),
                }

        if has_active_transaction:
            return await _execute_transaction()
        else:
            async with self.session.begin():
                return await _execute_transaction()

    async def _store_houses_with_repo(
        self, houses: List[House], repo: HouseRepository
    ) -> Tuple[List[House], List[House], List[Tuple[House, str]]]:
        """
        Internal method to store houses with the given repository

        Args:
            houses: List of House objects to store
            repo: Repository to use for storage

        Returns:
            Tuple[List[House], List[House], List[Tuple[House, str]]]:
            Lists of new, existing, and updated houses (with old status)
        """
        new_db_houses: List[DbHouse] = []
        existing_db_houses: List[DbHouse] = []
        updated_houses: List[Tuple[House, str]] = []

        for house in houses:
            existing_house = await repo.get_by_address(house.address, house.city)
            if existing_house:
                if existing_house.status != house.status:
                    old_status = existing_house.status
                    existing_house.status = house.status
                    await repo.update(existing_house.id, house)
                    # Store house and its old status for notification
                    house_obj = await db_houses_to_pydantic_async([existing_house])
                    if house_obj:
                        updated_houses.append((house_obj[0], old_status))
                existing_db_houses.append(existing_house)
            else:
                stored_db_house = await repo.create(house)
                new_db_houses.append(stored_db_house)

        new_houses = await db_houses_to_pydantic_async(new_db_houses)
        existing_houses = await db_houses_to_pydantic_async(existing_db_houses)

        # Store the updated houses for notification in the _execute_transaction method
        return (new_houses, existing_houses, updated_houses)

    async def _store_houses(
        self, houses: List[House]
    ) -> Tuple[List[House], List[House], List[Tuple[House, str]]]:
        """
        Internal method for house storage

        Args:
            houses: List of House objects to store

        Returns:
            Tuple[List[House], List[House], List[Tuple[House, str]]]:
            Lists of new, existing, and updated houses (with old status)
        """
        async with get_repository(self.session) as repo:
            return await self._store_houses_with_repo(houses, repo)
