I'll help you understand the database tables needed for adding a new website to the crawler. Let me first check the database migrations to see the table structures.

Ran tool
Let me examine the migration files to understand the table structures.

Read file: database_migrations/versions/2025_04_20_2315-a1b2c3d4e5f6_combined_initial_migrations.py
Based on the migration files and the architecture document, I'll explain how each table works and how they interact with each other for configuring a new website crawler:

1. **`websites` Table**
   - This is the root table that defines basic information about each website you want to crawl
   - Fields:
     - `id`: Primary key
     - `name`: Unique name for the website (e.g., "Vesteda")
     - `base_url`: The main URL of the website
     - `is_active`: Boolean to enable/disable crawling for this website
   - This table is referenced by all other configuration tables through `website_id`

2. **`login_configs` Table** (Optional)
   - Contains configuration for websites that require login
   - Links to `websites` through `website_id`
   - Fields:
     - `login_url`: URL of the login page
     - `username_selector`: CSS/XPath selector for username field
     - `password_selector`: CSS/XPath selector for password field
     - `submit_selector`: CSS/XPath selector for submit button
   - You only need to create a record here if your website requires authentication

3. **`navigation_configs` Table**
   - Defines how to navigate to and through the listing pages
   - Links to `websites` through `website_id`
   - Fields:
     - `listing_page_url`: URL where the house listings can be found
     - `listing_selector`: CSS/XPath selector to find individual house listings
     - `next_page_selector`: Optional selector for pagination (if the site has multiple pages)

4. **`extraction_configs` Table**
   - Defines what data to extract and how to extract it
   - Links to `websites` through `website_id`
   - Fields:
     - `name`: Name of the field being extracted (e.g., "price", "address")
     - `selector`: CSS/XPath selector to find the element
     - `extraction_type`: How to extract the data (e.g., "text", "attribute", "html")
     - `attribute_name`: If extraction_type is "attribute", which attribute to extract
     - `is_required`: Whether this field must be present

5. **`field_mappings` Table**
   - Maps extracted data to house model fields
   - Links to `extraction_configs` through `extraction_config_id`
   - Fields:
     - `target_field`: The field name in the `houses` table
     - `transformation_rule`: JSON object defining how to transform the extracted data

6. **`houses` Table**
   - This is where the actual scraped data is stored
   - Contains all the fields for storing house information like address, price, etc.
   - Updated whenever new houses are found or existing ones change

Here's an example flow of how these tables work together:

1. The crawler starts by looking up a website by name in the `websites` table
2. If login is required, it uses the `login_configs` for that website
3. It then uses `navigation_configs` to:
   - Navigate to the listing page
   - Find all house listings using the listing selector
   - Navigate through pages if there's a next_page_selector
4. For each listing found, it uses `extraction_configs` to:
   - Extract data using the specified selectors and methods
5. The extracted data is then transformed using `field_mappings` rules
6. Finally, the processed data is stored in the `houses` table

To add a new website, you would:
1. Add a record to `websites`
2. Add login configuration to `login_configs` if needed
3. Add navigation rules to `navigation_configs`
4. Add extraction rules to `extraction_configs` for each piece of data you want to extract
5. Create field mappings in `field_mappings` to map the extracted data to house fields
