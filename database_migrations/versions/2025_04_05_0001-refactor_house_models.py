"""Refactor house models into unified structure

Revision ID: refactor_house_models
Revises: c93f29304c50
Create Date: 2025-04-05 00:01:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session


# revision identifiers, used by Alembic.
revision: str = "refactor_house_models"
down_revision: Union[str, None] = "c93f29304c50"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema to create unified house model and migrate data."""
    # Create the new houses table
    op.create_table(
        "houses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("postal_code", sa.String(), nullable=True),
        sa.Column("neighborhood", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("high_demand", sa.Boolean(), nullable=True),
        sa.Column("demand_message", sa.String(), nullable=True),
        sa.Column("detail_url", sa.String(), nullable=True),
        sa.Column("rental_price", sa.String(), nullable=True),
        sa.Column("service_costs", sa.String(), nullable=True),
        sa.Column("min_income_single", sa.String(), nullable=True),
        sa.Column("min_income_joint", sa.String(), nullable=True),
        sa.Column("read_more_url", sa.String(), nullable=True),
        sa.Column("square_meters", sa.Integer(), nullable=True),
        sa.Column("bedrooms", sa.Integer(), nullable=True),
        sa.Column("energy_label", sa.String(), nullable=True),
        sa.Column("available_from", sa.String(), nullable=True),
        sa.Column("complex", sa.String(), nullable=True),
        sa.Column("complex_name", sa.String(), nullable=True),
        sa.Column("complex_description", sa.Text(), nullable=True),
        sa.Column("year_of_construction", sa.Integer(), nullable=True),
        sa.Column("number_of_objects", sa.String(), nullable=True),
        sa.Column("number_of_floors", sa.String(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("location_map_url", sa.String(), nullable=True),
        sa.Column("request_viewing_url", sa.String(), nullable=True),
        sa.Column("options", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        schema="steal_house",
    )

    # Transfer data from gallery and detail tables to the new houses table
    connection = op.get_bind()

    # Migrate data from gallery houses
    gallery_houses = connection.execute(
        sa.text("SELECT * FROM steal_house.gallery_houses")
    ).fetchall()

    # Migrate data from detail houses
    detail_houses = connection.execute(
        sa.text("SELECT * FROM steal_house.detail_houses")
    ).fetchall()

    # First, insert all gallery houses into the new table
    for gallery in gallery_houses:
        op.execute(
            sa.text(
                """
                INSERT INTO steal_house.houses 
                (address, city, status, high_demand, demand_message, detail_url)
                VALUES (:address, :city, :status, :high_demand, :demand_message, :detail_url)
            """
            ).bindparams(
                address=gallery.address,
                city=gallery.city,
                status=gallery.status,
                high_demand=gallery.high_demand,
                demand_message=gallery.demand_message,
                detail_url=gallery.detail_url,
            )
        )

    # Then, merge data from detail houses where possible, otherwise insert as new records
    for detail in detail_houses:
        # Try to find a matching record in the houses table by address and city
        matches = connection.execute(
            sa.text(
                """
                SELECT id FROM steal_house.houses 
                WHERE address = :address AND city = :city
            """
            ).bindparams(address=detail.address, city=detail.city)
        ).fetchall()

        if matches:
            # Update existing record
            house_id = matches[0][0]
            op.execute(
                sa.text(
                    """
                    UPDATE steal_house.houses 
                    SET 
                        postal_code = :postal_code,
                        neighborhood = :neighborhood,
                        rental_price = :rental_price,
                        service_costs = :service_costs,
                        min_income_single = :min_income_single,
                        min_income_joint = :min_income_joint,
                        read_more_url = :read_more_url,
                        square_meters = :square_meters,
                        bedrooms = :bedrooms,
                        energy_label = :energy_label,
                        available_from = :available_from,
                        complex = :complex,
                        complex_name = :complex_name,
                        complex_description = :complex_description,
                        year_of_construction = :year_of_construction,
                        number_of_objects = :number_of_objects,
                        number_of_floors = :number_of_floors,
                        description = :description,
                        location_map_url = :location_map_url,
                        request_viewing_url = :request_viewing_url,
                        options = :options
                    WHERE id = :id
                """
                ).bindparams(
                    id=house_id,
                    postal_code=detail.postal_code,
                    neighborhood=detail.neighborhood,
                    rental_price=detail.rental_price,
                    service_costs=detail.service_costs,
                    min_income_single=detail.min_income_single,
                    min_income_joint=detail.min_income_joint,
                    read_more_url=detail.read_more_url,
                    square_meters=detail.square_meters,
                    bedrooms=detail.bedrooms,
                    energy_label=detail.energy_label,
                    available_from=detail.available_from,
                    complex=detail.complex,
                    complex_name=detail.complex_name,
                    complex_description=detail.complex_description,
                    year_of_construction=detail.year_of_construction,
                    number_of_objects=detail.number_of_objects,
                    number_of_floors=detail.number_of_floors,
                    description=detail.description,
                    location_map_url=detail.location_map_url,
                    request_viewing_url=detail.request_viewing_url,
                    options=detail.options,
                )
            )
        else:
            # Insert as new record
            op.execute(
                sa.text(
                    """
                    INSERT INTO steal_house.houses 
                    (address, city, postal_code, neighborhood, status, 
                    rental_price, service_costs, min_income_single, min_income_joint, read_more_url,
                    square_meters, bedrooms, energy_label, available_from, complex,
                    complex_name, complex_description, year_of_construction, number_of_objects, number_of_floors,
                    description, location_map_url, request_viewing_url, options)
                    VALUES 
                    (:address, :city, :postal_code, :neighborhood, :status, 
                    :rental_price, :service_costs, :min_income_single, :min_income_joint, :read_more_url,
                    :square_meters, :bedrooms, :energy_label, :available_from, :complex,
                    :complex_name, :complex_description, :year_of_construction, :number_of_objects, :number_of_floors,
                    :description, :location_map_url, :request_viewing_url, :options)
                """
                ).bindparams(
                    address=detail.address,
                    city=detail.city,
                    postal_code=detail.postal_code,
                    neighborhood=detail.neighborhood,
                    status=detail.status,
                    rental_price=detail.rental_price,
                    service_costs=detail.service_costs,
                    min_income_single=detail.min_income_single,
                    min_income_joint=detail.min_income_joint,
                    read_more_url=detail.read_more_url,
                    square_meters=detail.square_meters,
                    bedrooms=detail.bedrooms,
                    energy_label=detail.energy_label,
                    available_from=detail.available_from,
                    complex=detail.complex,
                    complex_name=detail.complex_name,
                    complex_description=detail.complex_description,
                    year_of_construction=detail.year_of_construction,
                    number_of_objects=detail.number_of_objects,
                    number_of_floors=detail.number_of_floors,
                    description=detail.description,
                    location_map_url=detail.location_map_url,
                    request_viewing_url=detail.request_viewing_url,
                    options=detail.options,
                )
            )

    # Drop the old tables after data migration is complete
    op.drop_table("floor_plans", schema="steal_house")
    op.drop_table("detail_houses", schema="steal_house")
    op.drop_table("gallery_houses", schema="steal_house")


def downgrade() -> None:
    """Downgrade schema back to separate gallery and detail houses."""
    # Create the old tables
    op.create_table(
        "gallery_houses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("image_url", sa.String(), nullable=True),
        sa.Column("high_demand", sa.Boolean(), nullable=True),
        sa.Column("demand_message", sa.String(), nullable=True),
        sa.Column("detail_url", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        schema="steal_house",
    )

    op.create_table(
        "detail_houses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("gallery_id", sa.Integer(), nullable=True),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("postal_code", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("neighborhood", sa.String(), nullable=True),
        sa.Column("rental_price", sa.String(), nullable=False),
        sa.Column("service_costs", sa.String(), nullable=True),
        sa.Column("min_income_single", sa.String(), nullable=True),
        sa.Column("min_income_joint", sa.String(), nullable=True),
        sa.Column("read_more_url", sa.String(), nullable=True),
        sa.Column("square_meters", sa.Integer(), nullable=False),
        sa.Column("bedrooms", sa.Integer(), nullable=False),
        sa.Column("energy_label", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("available_from", sa.String(), nullable=True),
        sa.Column("complex", sa.String(), nullable=True),
        sa.Column("complex_name", sa.String(), nullable=True),
        sa.Column("complex_description", sa.Text(), nullable=True),
        sa.Column("year_of_construction", sa.Integer(), nullable=True),
        sa.Column("number_of_objects", sa.String(), nullable=True),
        sa.Column("number_of_floors", sa.String(), nullable=True),
        sa.Column("complex_image_url", sa.String(), nullable=True),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("location_map_url", sa.String(), nullable=True),
        sa.Column("request_viewing_url", sa.String(), nullable=True),
        sa.Column("options", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ["gallery_id"],
            ["steal_house.gallery_houses.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="steal_house",
    )

    op.create_table(
        "floor_plans",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("house_id", sa.Integer(), nullable=False),
        sa.Column("image_url", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["house_id"],
            ["steal_house.detail_houses.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="steal_house",
    )

    # Migrate data back would be more complex and lossy since we combined data
    # This is a simplified version that creates empty tables

    # Drop the new houses table
    op.drop_table("houses", schema="steal_house")
