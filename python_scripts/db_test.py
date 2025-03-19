#!/usr/bin/env python
"""
Test script to verify database connection and schema.
"""
import logging
from sqlalchemy import text, inspect
from sqlalchemy.exc import SQLAlchemyError

from python_scripts.db_models.db_connection import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_connection():
    """Test database connection"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            for row in result:
                logger.info(f"Connection successful: {row[0]}")
            return True
    except SQLAlchemyError as e:
        logger.error(f"Database connection error: {str(e)}")
        return False

def list_schemas():
    """List available schemas"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT schema_name FROM information_schema.schemata"))
            schemas = [row[0] for row in result]
            logger.info(f"Available schemas: {schemas}")
            return schemas
    except SQLAlchemyError as e:
        logger.error(f"Error listing schemas: {str(e)}")
        return []

def list_tables(schema='steal_house'):
    """List tables in a schema"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text(
                f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{schema}'"
            ))
            tables = [row[0] for row in result]
            logger.info(f"Tables in {schema} schema: {tables}")
            return tables
    except SQLAlchemyError as e:
        logger.error(f"Error listing tables: {str(e)}")
        return []

def inspect_table(table_name, schema='steal_house'):
    """Inspect a table structure"""
    try:
        inspector = inspect(engine)
        columns = inspector.get_columns(table_name, schema=schema)
        
        logger.info(f"Table: {schema}.{table_name}")
        logger.info("Columns:")
        for column in columns:
            logger.info(f"  - {column['name']}: {column['type']} (nullable: {column['nullable']})")
        
        primary_keys = inspector.get_pk_constraint(table_name, schema=schema)
        logger.info(f"Primary keys: {primary_keys['constrained_columns']}")
        
        foreign_keys = inspector.get_foreign_keys(table_name, schema=schema)
        if foreign_keys:
            logger.info("Foreign keys:")
            for fk in foreign_keys:
                logger.info(f"  - {fk['constrained_columns']} -> {fk['referred_schema']}.{fk['referred_table']}.{fk['referred_columns']}")
        
        return True
    except SQLAlchemyError as e:
        logger.error(f"Error inspecting table: {str(e)}")
        return False

if __name__ == "__main__":
    logger.info("Testing database connection...")
    if test_connection():
        schemas = list_schemas()
        if 'steal_house' in schemas:
            tables = list_tables('steal_house')
            for table in tables:
                inspect_table(table, 'steal_house')
        else:
            logger.error("Schema 'steal_house' not found. Make sure migrations have been run.")
    else:
        logger.error("Database connection failed. Check your database settings.") 