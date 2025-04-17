# Step 2: Database Model Refactoring

## Objective
Combine `GalleryHouse` and `DetailHouse` into a single unified `House` model while removing unused fields and the `FloorPlan` model.

## Tasks

*   **Define Unified Models:**
    *   In `crawler_job/models/pydantic_models.py`:
        *   Create a new Pydantic model `House`.
        *   Combine fields from the current `GalleryHouse` (excluding `image_url`) and `DetailHouse` (excluding `complex_image_url`, `read_more_url`) into the `House` model. Exclude any fields related to `FloorPlan`.
        *   Add `to_db_model()` method to `House` for converting to `DbHouse`.
        *   Add `@classmethod from_db_model()` to `House` for converting from `DbHouse`.
        *   Ensure all fields have type hints and the model has a docstring.
    *   In `crawler_job/models/db_models.py`:
        *   Create a new SQLAlchemy model `DbHouse` inheriting from `Base`.
        *   Mirror the structure and fields of the Pydantic `House` model.
        *   Ensure it uses appropriate SQLAlchemy column types.
*   **Remove Old Models:**
    *   Delete `GalleryHouse`, `DetailHouse`, and `FloorPlan` from `crawler_job/models/pydantic_models.py`.
    *   Delete `DbGalleryHouse`, `DbDetailHouse`, and `DbFloorPlan` from `crawler_job/models/db_models.py`.
*   **Verify Alembic Configuration:**
    *   Check `database_migrations/env.py` and confirm that `target_metadata` is correctly set to `crawler_job.models.db_models.Base.metadata`.

## Expected Outcomes
- A single, unified `House` Pydantic model replacing the separate `GalleryHouse` and `DetailHouse` models
- A single, unified `DbHouse` SQLAlchemy model replacing the separate database model classes
- Removal of the `FloorPlan` model and related code
- Removal of unused fields (`image_url`, `complex_image_url`, and `read_more_url`)
- Maintained conversion methods between Pydantic and SQLAlchemy models 