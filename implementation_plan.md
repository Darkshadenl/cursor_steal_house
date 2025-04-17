# Step 3: Crawler Logic Refactoring

## Objective
Update the crawler logic to work with the unified `House` model, eliminating the two-step collection process and removing extraction of unused fields.

## Tasks

*   **Update Vesteda Steps (`crawler_job/crawlers/vesteda/vesteda_steps.py`):**
    *   Modify `execute_property_extraction`:
        *   Aim to extract all required fields for the new `House` model from the gallery page results.
        *   Remove logic for extracting `image_url`.
    *   Modify `execute_detailed_property_extraction`:
        *   If still needed for data not on the gallery page, update it to fetch remaining `House` fields.
        *   Remove logic for extracting `complex_image_url`, `read_more_url`, and any floor plan data.
        *   Consider merging this step's logic into `execute_property_extraction` if feasible.
    *   Modify `execute_llm_extraction`:
        *   Ensure it populates the unified `House` model, excluding the removed fields.
        *   Adjust prompts/parsing as needed for the new model structure.
*   **Update Main Crawler (`crawler_job/crawlers/vesteda/vesteda_crawler.py`):**
    *   In `VestedaCrawler.run_full_crawl`:
        *   Change the flow to process each property into a single `House` Pydantic object.
        *   Remove intermediate lists like `gallery_data: List[GalleryHouse]` and `detail_houses: List[DetailHouse]`.
        *   Use a single list `houses: List[House]` if needed.
        *   Update the call to `house_service.identify_new_houses` to accept and return `List[House]`.
        *   Update the call to `house_service.store_houses_atomic` to accept `List[House]` and operate on the `houses` table. Adjust parameters accordingly.

## Expected Outcomes
- Streamlined crawling process that directly populates `House` objects
- Elimination of the two-step (gallery then detail) crawling process
- Removal of code extracting unused fields
- Updated extraction logic that fits the new unified data model 