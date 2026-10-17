import pytest
from sqlalchemy import Engine
from .connection import db_connection_handler

# integration test
@pytest.mark.skip(reason='Interaction w/ database')
def test_connect_to_db():
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
