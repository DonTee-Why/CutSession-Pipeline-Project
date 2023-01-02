import sqlite3
from fastapi import HTTPException


class DBConnection():
    def __init__(self, db):
        self.conn = sqlite3.connect(database=db, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("pragma foreign_keys = on")
        self.conn.commit()
    
    # Get DBManager instance
    @classmethod
    def get_db_conn_instance(cls):
        if not hasattr(cls, "instance"):
            cls.db_instance = DBConnection("cut_sess.sqlite")
        return cls.db_instance.conn


class DBManager():
    def __init__(self) -> None:
        self.db = DBConnection.get_db_conn_instance()

    def create_tables(self, sql_script: str):
        try:
            return self.db.executescript(sql_script)
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500,
                                detail={
                                    "message": "Error occured while trying to execute query.",
                                    "errors": [
                                        repr(e)
                                    ]
                                })
        finally:
            self.db.commit()
    
    def to_dict(self, row):
        return {key: row[key] for key in row.keys()}

    def fetch_one(self, arg: str):
        try:
            cursor = self.db.cursor()
            cursor.execute(arg)
            row = cursor.fetchone()

            return self.to_dict(row)
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500,
                                detail={
                                    "message": "Error occured while trying to execute query.",
                                    "errors": [
                                        repr(e)
                                    ]
                                })
        finally:
            self.db.commit()

    def fetch_all(self, arg: str):
        try:
            cursor = self.db.cursor()
            cursor.execute(arg)

            return cursor.fetchall()
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500,
                                detail={
                                    "message": "Error occured while trying to execute query.",
                                    "errors": [
                                        repr(e)
                                    ]
                                })
        finally:
            self.db.commit()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.db.close()


class DbQuery():
    def __init__(self) -> None:
        self.query = ""

    def db_select(self, select_columns: str, table_name: str):
        self.query = ""
        select_query = f"SELECT {select_columns} FROM {table_name} "
        self.query = "".join([select_query, self.query])
        return self

    def db_where(self, column: str, operator: str, value: str):
        where_query = f"WHERE {column} {operator} '{value}' "
        self.query = "".join([self.query, where_query])
        return self

    def db_and_where(self, column: str, operator: str, value: str):
        where_query = f"AND {column} {operator} '{value}' "
        self.query = "".join([self.query, where_query])
        return self

    def db_insert(self, table_name: str):
        self.query = ""
        insert_query = f"INSERT INTO {table_name} "
        self.query = "".join([insert_query, self.query])
        return self

    def db_values(self, arg: dict):
        columns = ", ".join(arg.keys())
        column_values = ", ".join(
            [f"'{str(value)}'" for value in arg.values()])
        # return_values = ", ".join(
        #     [f"'{value}'" for value in return_val])
        values_query = f"({columns}) VALUES ({column_values}) RETURNING *"
        self.query = "".join([self.query, values_query])
        return self

    def db_paginate(self, arg: list):
        pagination_query = f"LIMIT {arg[0]} OFFSET {arg[1]} "
        self.query = "".join([self.query, pagination_query])
        return self


class User(DbQuery):
    def __init__(self) -> None:
        super().__init__()
        self.table_name = "users"

    def select(self):
        select_columns = "users.user_id, users.name, users.username, users.email, users.dob, users.city_of_residence, users.phone_number, users.password"
        self.db_select(select_columns, self.table_name)
        return self

    def where(self, column: str, operator: str, value: str):
        self.db_where(column, operator, value)
        return self

    def and_where(self, column: str, operator: str, value: str):
        self.db_and_where(column, operator, value)
        return self

    def insert(self):
        self.db_insert(self.table_name)
        return self

    def values(self, arg: dict()):
        self.db_values(arg)
        return self

    def paginate(self, limit: int, offset: int = 1):
        arg = [limit, (limit * offset - limit)]
        self.db_paginate(arg)
        return self


class Merchant(DbQuery):
    def __init__(self) -> None:
        super().__init__()
        self.table_name = "merchants"

    def select(self):
        select_columns = "merchants.merchant_id, merchants.name, merchants.username, merchants.email, merchants.dob, merchants.city_of_operation, merchants.phone_number, merchants.password"
        self.db_select(select_columns, self.table_name)
        return self

    def where(self, column: str, operator: str, value: str):
        self.db_where(column, operator, value)
        return self

    def and_where(self, column: str, operator: str, value: str):
        self.db_and_where(column, operator, value)
        return self

    def insert(self):
        self.db_insert(self.table_name)
        return self

    def values(self, arg: dict()):
        self.db_values(arg)
        return self

    def paginate(self, limit: int, offset: int = 1):
        args = (limit, (limit * offset - limit))
        self.db_paginate(args)
        return self


class Session(DbQuery):
    def __init__(self) -> None:
        super().__init__()
        self.table_name = "studio_sessions"

    def select(self):
        select_columns = "*"
        self.db_select(select_columns, self.table_name)
        return self

    def where(self, column: str, operator: str, value: str):
        self.db_where(column, operator, value)
        return self

    def and_where(self, column: str, operator: str, value: str):
        self.db_and_where(column, operator, value)
        return self

    def insert(self):
        self.db_insert(self.table_name)
        return self

    def values(self, arg: dict()):
        self.db_values(arg)
        return self

    def paginate(self, limit: int, offset: int = 1):
        args = (limit, (limit * offset - limit))
        self.db_paginate(args)
        return self


class Booking(DbQuery):
    def __init__(self) -> None:
        super().__init__()
        self.table_name = "bookings"

    def select(self):
        select_columns = "*"
        self.db_select(select_columns, self.table_name)
        return self

    def where(self, column: str, operator: str, value: str):
        self.db_where(column, operator, value)
        return self

    def and_where(self, column: str, operator: str, value: str):
        self.db_and_where(column, operator, value)
        return self

    def insert(self):
        self.db_insert(self.table_name)
        return self

    def values(self, arg: dict()):
        self.db_values(arg)
        return self

    def paginate(self, limit: int, offset: int = 1):
        args = (limit, (limit * offset - limit))
        self.db_paginate(args)
        return self


db = DBManager()
