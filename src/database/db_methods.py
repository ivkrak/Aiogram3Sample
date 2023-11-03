import sqlalchemy as db

engine = db.create_engine('sqlite:///Database_files/db.sqlite3')

connection = engine.connect()

metadata = db.MetaData()
