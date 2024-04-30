from fastapi import Depends
from requests import Session
from app.schema import Transaction
from app.database import Base , get_db


def addTransaction(sender_id:int , amount:int):
    Transaction=Base.classes.transaction
    transaction=Transaction(sender_id=sender_id, amount=amount)
    db_gen=get_db()
    db=next(db_gen)
    db.add(transaction)
    db.commit()
    