import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# base class for model classes
Base = declarative_base()

# create db connection
load_dotenv()
db_url = os.getenv("DB_URL")
if not db_url:
    raise ValueError("Missing environment variable: DB_URL")
engine = create_engine(db_url, echo=True)

# create tables (if they don't already exist)
Base.metadata.create_all(engine)

# create sessionmaker for interacting with db
Session = sessionmaker(bind=engine)


# custom error
class CoinNotFoundError(Exception):
    pass


# model class
class Coin(Base):
    __tablename__ = "coins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(5), nullable=False)
    name = Column(String(30), nullable=False)
    price = Column(Float)
    total_volume = Column(Integer)
    total_supply = Column(Integer)
    max_supply = Column(Integer)
    market_cap = Column(Float)  # (price per coin * total circulating supply)
    issuance_progress = Column(Float)  # (total supply / max supply)
    circulating_supply = Column(Integer)
    unavailable_supply = Column(Integer)  # (total supply - circulating supply)
    updated_on = Column(DateTime)


def create_coin(session, coin: Coin):
    session.add(coin)
    session.commit()


def retrieve_coin(session, coin_id: Integer):
    coin = session.query(Coin).filter_by(id=coin_id).first()
    if not coin:
        raise CoinNotFoundError(f"No coin found with ID = {coin_id}")
    return coin


def list_coins_by_symbol(session, symbol: str):
    coins = session.query(Coin).filter(Coin.symbol == symbol).all()
    if not coins:
        raise CoinNotFoundError(f"No coins found with Symbol = {symbol}")
    return coins
