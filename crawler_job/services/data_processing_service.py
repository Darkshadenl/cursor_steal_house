from typing import List
from crawler_job.models.house_models import House
from crawler_job.services.house_service import HouseService
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class DataProcessingService:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    async def check_if_houses_exist(self, houses: List[House]) -> List[House]:
        async with HouseService(
            notification_service=self.notification_service
        ) as house_service:
            new_houses = await house_service.identify_new_houses_async(houses)

            if not new_houses:
                return []

            logger.info(f"Fetching details for {len(new_houses)} new houses...")
            return new_houses

    @staticmethod
    def merge_detailed_houses(
        houses: List[House], detailed_houses: List[House]
    ) -> None:
        for detailed_house in detailed_houses:
            for house in houses:
                if (
                    house.address == detailed_house.address
                    and house.city == detailed_house.city
                ):
                    for field, value in detailed_house.model_dump(
                        exclude_unset=True
                    ).items():
                        if value is not None and (
                            getattr(house, field) is None
                            or field not in ["address", "city", "status"]
                        ):
                            setattr(house, field, value)
                    break

    async def store_houses(self, houses: List[House]) -> None:
        async with HouseService(
            notification_service=self.notification_service
        ) as house_service:
            await house_service.store_houses_atomic_async(
                houses=houses,
            )
