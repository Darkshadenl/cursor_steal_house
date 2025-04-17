# Step 4: Service Layer Refactoring

## Objective
Update the HouseService and other service components to work with the new unified House model and table.

## Tasks

*   **Update `HouseService` Methods:**
    *   Modify `identify_new_houses`:
        *   Update to accept and return `List[House]` instead of `List[GalleryHouse]`.
        *   Adjust internal logic for identifying new houses based on unified model.
    *   Modify `store_houses_atomic`:
        *   Update to accept a `List[House]` parameter.
        *   Remove logic dealing with separate gallery/detail objects or floor plans.
        *   Update the transaction logic to work with a single table/model.
    *   Update any other relevant methods to work exclusively with the `House` Pydantic model and the `DbHouse` SQLAlchemy model.
*   **Update Database Interactions:**
    *   Ensure all SQLAlchemy queries (inserts, updates, selects) target the new `houses` table (`DbHouse`) and use its defined columns.
    *   Update any service filtering logic that relied on fields from the old models.
*   **Notification Logic (if applicable):**
    *   Update any notification templates or message generation to use the unified `House` model fields.

## Expected Outcomes
- Service layer that works exclusively with the unified `House` model
- Simplified database interactions targeting a single table
- Maintained functionality for identifying new properties and storing them atomically
- Updated notification logic (if any) using the new model structure 