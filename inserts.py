import datetime


from model.base import Session, engine, Base
from model.users import Users
from db_inserts import userinserter


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

temp = {'username': 'aanil',
        'email': 'anan@hotmail.com',
        'password': '3131',
        'register_date': str(datetime.datetime.now()),
        'proved': True}

userinserter(temp)

