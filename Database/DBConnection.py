import sqlite3
class MetaSingleton(type):
    _instances ={}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection =None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("Database/db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

