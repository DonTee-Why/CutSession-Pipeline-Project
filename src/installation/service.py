from typing import Any

from fastapi import Depends
from ..database.database import DBManager


def install_tables() -> Any:
    db = DBManager()

    with open('create_tables.sql', 'r') as sql_file:
        sql_script = sql_file.read()


    db.create_tables(sql_script)
    return "Tables created successfully"
