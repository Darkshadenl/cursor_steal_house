# Step 1: Script Reorganization

## Objective
Reorganize all scripts into a consistent directory structure for improved organization and maintainability.

## Tasks

*   **Create Directories:**
    *   Create a top-level `scripts` directory.
    *   Inside `scripts`, create `shell` and `docker` subdirectories.
    *   Inside `scripts/shell`, create a `test` subdirectory.
*   **Move Scripts:**
    *   Move all `.sh` files currently in the project root (e.g., `build-and-push.sh`, `create-new-job.sh`, `run_crawler.sh`, `validate_models.sh`) to `scripts/shell/`.
    *   Move the `Dockerfile` from the project root to `scripts/docker/`.
    *   Move all scripts currently inside the `ter-test/` directory to `scripts/shell/test/`.
*   **Cleanup:**
    *   Delete the now empty `ter-test/` directory.
*   **Update References:**
    *   Modify `scripts/docker/Dockerfile`: Update any `COPY` commands that referred to scripts in their old locations to use the new paths within `scripts/shell/`.
    *   Modify `README.md`: Update any instructions or examples that mention running scripts to use the new paths (e.g., `bash scripts/shell/run_crawler.sh`).
    *   Modify `docs/deployment.md`: Update any instructions related to building the Docker image or running scripts to use the new paths.

## Expected Outcomes
- All scripts organized into the `scripts` directory with clear separation between shell scripts and Docker-related files
- Updated references in documentation and Dockerfile to reflect the new locations
- Improved project structure with no scripts at the project root level 