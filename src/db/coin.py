import os

from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# base class for model classes
Base = declarative_base()


# model class
class Coin(Base):
    __tablename__ = "coins"

    id = Column(String(30), primar_key=True)
    symbol = Column(String(5), nullable=False)
    name = Column(String(30), nullable=False)
    current_price = Column(Float)
    total_volume = Column(Integer)
    market_cap_rank = Column(Integer)
    market_cap = Column(Integer)
    total_supply = Column(Integer)
    max_supply = Column(Integer)
    circulating_supply = Column(Integer)
    last_updated = Column(DateTime)


# create db connection
db_url = os.getenv("DB_URL")
if not db_url:
    raise ValueError("Missing environment variable: DB_URL")
engine = create_engine(db_url, echo=True)

# create tables (if they don't already exist)
Base.metadata.create_all(engine)

# create sessionmaker for interacting with db
Session = sessionmaker(bind=engine)


def create_coin(coin: Coin):
    session = Session()
    session.add(coin)
    session.commit()
    session.close()


def retrieve_coin(coin_id: String):
    session = Session()
    coin = session.query(Coin).filter_by(id=id).first()
    if not coin:
        print(f"No coin found with ID = {coin_id}")
    session.close()
    return coin
