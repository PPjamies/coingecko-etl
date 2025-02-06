import pytest

from coingecko.db.coin import Base, engine, Session


@pytest.fixture(scope='session')
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def session(setup_database):
    db = Session()
    yield db
    db.rollback()
    db.close()
