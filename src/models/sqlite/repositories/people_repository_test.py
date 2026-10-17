from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from .people_repository import PeopleRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[]
        )

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_insert_person():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)
    repo.insert_person(
        first_name='John',
        last_name='Doe',
        age=30,
        pet_id=1
    )

    mock_connection.session.add.assert_called_once()
