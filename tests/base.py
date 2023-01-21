import sqlite3
from pathlib import Path
from fastapi import FastAPI
from src.config import get_settings
from src.database.database import DBManager, User, Merchant, Session, Booking



class BaseTestClass():
    db: DBManager
    
    def set_up(self):
        self.db = DBManager("testing")
        self.create_tables()

    def create_tables(self) -> None:
        with open('create_tables.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        self.db.create_tables(sql_script)
    
    def tear_down(self) -> None:
        Path.unlink("./test_db.sqlite")

user = User()
merchant = Merchant()
session = Session()
booking = Booking()