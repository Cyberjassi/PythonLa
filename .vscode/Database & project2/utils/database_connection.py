import sqlite3

class DatabaseConnection:
    def __init__(self,host):
        self.connection = None
        self.host = host
    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection
    def __exit__(self,exc_type,ex_val,exc_tb):
        self.connection.commit()
        self.connection.close()