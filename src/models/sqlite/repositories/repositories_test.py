import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

db_connection_handler.connect_to_db()

# Integration test
@pytest.mark.skip(reason='Interaction w/ database')
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()

    print(response)

# Integration test
@pytest.mark.skip(reason='Interaction w/ database')
def test_delete_pet():
    name = 'Kripto'
    repo = PetsRepository(db_connection_handler)
    repo.delete_pet(name=name)
