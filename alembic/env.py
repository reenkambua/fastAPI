import sys
import os
from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
from dotenv import load_dotenv

load_dotenv()

# Add app directory to path
sys.path.append(os.path.join(sys.path[0], "app"))

from app.database import Base
from app.models.item import Item

config = context.config
fileConfig(config.config_file_name)

# Metadata for autogenerate
target_metadata = Base.metadata

# Build database URL from .env
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def run_migrations_online():
    connectable = create_engine(DATABASE_URL)  # ✅ Use URL directly
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    raise Exception("Offline mode not configured")
else:
    run_migrations_online()
