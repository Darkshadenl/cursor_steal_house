import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

from crawler_job.services.house_service import HouseService
from crawler_job.models.house_models import House
from crawler_job.models.db_models import DbHouse


@pytest.fixture
def sample_house():
    """Sample House object for testing"""
    return House(
        address="123 Test Street",
        city="Test City",
        status="For rent",
        high_demand=False,
        postal_code="1234AB",
        rental_price="€1000",
        square_meters=80,
        bedrooms=2,
    )


@pytest.fixture
def sample_db_house():
    """Sample DbHouse object for testing"""
    db_house = MagicMock(spec=DbHouse)
    db_house.id = 1
    db_house.address = "123 Test Street"
    db_house.city = "Test City"
    db_house.status = "For rent"
    db_house.high_demand = False
    db_house.postal_code = "1234AB"
    db_house.rental_price = "€1000"
    db_house.square_meters = 80
    db_house.bedrooms = 2
    return db_house


@pytest.mark.asyncio
async def test_identify_new_houses_async(sample_house):
    """Test identifying new houses"""
    # Mock repository
    mock_repo = AsyncMock()
    mock_repo.get_by_address.return_value = None  # No existing house found

    # Mock session and context manager
    mock_session = AsyncMock()

    with patch("crawler_job.services.house_service.get_repository") as mock_get_repo:
        mock_get_repo.return_value.__aenter__.return_value = mock_repo
        mock_get_repo.return_value.__aexit__.return_value = None

        # Create service with mocked session
        house_service = HouseService()
        house_service.session = mock_session

        # Test the method
        houses = [sample_house]
        new_houses = await house_service.identify_new_houses_async(houses)

        # Assertions
        assert len(new_houses) == 1
        assert new_houses[0] == sample_house
        mock_repo.get_by_address.assert_called_once_with(
            sample_house.address, sample_house.city
        )


@pytest.mark.asyncio
async def test_identify_new_houses_existing(sample_house, sample_db_house):
    """Test identifying houses when they already exist"""
    # Mock repository
    mock_repo = AsyncMock()
    mock_repo.get_by_address.return_value = sample_db_house  # Existing house found

    # Mock session and context manager
    mock_session = AsyncMock()

    with patch("crawler_job.services.house_service.get_repository") as mock_get_repo:
        mock_get_repo.return_value.__aenter__.return_value = mock_repo
        mock_get_repo.return_value.__aexit__.return_value = None

        # Create service with mocked session
        house_service = HouseService()
        house_service.session = mock_session

        # Test the method
        houses = [sample_house]
        new_houses = await house_service.identify_new_houses_async(houses)

        # Assertions
        assert len(new_houses) == 0
        mock_repo.get_by_address.assert_called_once_with(
            sample_house.address, sample_house.city
        )


@pytest.mark.asyncio
async def test_store_houses_atomic_async(sample_house, sample_db_house):
    """Test storing houses atomically"""
    # Mock returned houses
    mock_new_houses = [sample_house]
    mock_existing_houses = []
    mock_updated_houses = []

    # Mock repository
    mock_repo = AsyncMock()

    # Mock session and context manager
    mock_session = AsyncMock()
    mock_session.in_transaction.return_value = False

    async def mock_begin():
        # Mock the session.begin() async context manager
        class AsyncContextManager:
            async def __aenter__(self):
                return None

            async def __aexit__(self, exc_type, exc_val, exc_tb):
                return None

        return AsyncContextManager()

    mock_session.begin = mock_begin

    with patch(
        "crawler_job.services.house_service.get_repository"
    ) as mock_get_repo, patch.object(
        HouseService, "_store_houses_with_repo"
    ) as mock_store:

        mock_get_repo.return_value.__aenter__.return_value = mock_repo
        mock_get_repo.return_value.__aexit__.return_value = None
        mock_store.return_value = (
            mock_new_houses,
            mock_existing_houses,
            mock_updated_houses,
        )

        # Create service with mocked session
        house_service = HouseService()
        house_service.session = mock_session

        # Test the method
        houses = [sample_house]
        all_houses = [sample_house]
        result = await house_service.store_houses_atomic_async(houses, all_houses)

        # Assertions
        assert result["new_count"] == 1
        assert result["existing_count"] == 0
        assert result["updated_count"] == 0
        # We can't use assert_called_once() here because we're mocking an async context manager
        assert mock_store.call_count == 1
        assert mock_store.call_args[0][0] == houses
        assert mock_store.call_args[0][1] == mock_repo


@pytest.mark.asyncio
async def test_store_houses_with_repo_new(sample_house):
    """Test storing a new house with repository"""
    # Create a sample db house as the returned value
    mock_db_house = MagicMock(spec=DbHouse)
    mock_db_house.address = sample_house.address
    mock_db_house.city = sample_house.city

    # Mock repository
    mock_repo = AsyncMock()
    mock_repo.get_by_address.return_value = None  # No existing house
    mock_repo.create.return_value = mock_db_house

    # Mock the db_houses_to_pydantic_async function
    with patch(
        "crawler_job.services.house_service.db_houses_to_pydantic_async"
    ) as mock_to_pydantic:
        # Return the same house for new_houses and empty list for existing_houses
        mock_to_pydantic.side_effect = [[sample_house], []]

        # Create service
        house_service = HouseService()

        # Test the method
        houses = [sample_house]
        new_houses, existing_houses, updated_houses = (
            await house_service._store_houses_with_repo(houses, mock_repo)
        )

        # Assertions
        assert len(new_houses) == 1
        assert len(existing_houses) == 0
        assert len(updated_houses) == 0
        mock_repo.get_by_address.assert_called_once_with(
            sample_house.address, sample_house.city
        )
        mock_repo.create.assert_called_once()
        assert mock_to_pydantic.call_count == 2


@pytest.mark.asyncio
async def test_store_houses_with_repo_update(sample_house, sample_db_house):
    """Test updating an existing house with repository"""
    # Mock repository
    mock_repo = AsyncMock()
    mock_repo.get_by_address.return_value = sample_db_house
    sample_db_house.status = "Rented"  # Different status to trigger update

    # Mock the updated house for the notification
    updated_house = sample_house.model_copy()
    updated_house.status = "Rented"

    # Mock the db_houses_to_pydantic_async function to properly handle multiple calls
    with patch(
        "crawler_job.services.house_service.db_houses_to_pydantic_async"
    ) as mock_to_pydantic:
        # First call for updated_houses (house_obj), second call for existing_houses
        mock_to_pydantic.side_effect = lambda houses: [updated_house] if houses else []

        # Create service
        house_service = HouseService()

        # Test the method
        houses = [sample_house]
        new_houses, existing_houses, updated_houses = (
            await house_service._store_houses_with_repo(houses, mock_repo)
        )

        # Assertions
        assert len(new_houses) == 0  # No new houses
        assert len(updated_houses) == 1  # One updated house
        mock_repo.get_by_address.assert_called_once_with(
            sample_house.address, sample_house.city
        )
        mock_repo.update.assert_called_once()


if __name__ == "__main__":
    pytest.main()
