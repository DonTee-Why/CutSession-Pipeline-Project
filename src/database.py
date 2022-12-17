import sqlite3
from .main import HTTPException


class DBConnection():
    def __init__(self, db):
        self.conn = sqlite3.connect(database=db, check_same_thread=False)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()

    # Get DBManager instance
    @classmethod
    def get_db_conn_instance(cls):
        if not hasattr(cls, 'instance'):
            cls.db_instance = DBConnection('cut_sess.sqlite')
        return cls.db_instance.conn

    def __del__(self) -> None:
        self.db_instance.close()


class DBManager(object):
    def  __init__(self) -> None:
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

    def query(self, arg: str):
        try:
            yield self.db.execute(arg)
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
