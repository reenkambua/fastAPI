from app.database import Base, engine
from app.models.item import Item

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
