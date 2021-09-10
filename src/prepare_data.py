from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv


ENGINE = create_engine('sqlite:///data_sqlite/f1.sqlite')


TABLE_NAME = 'drivers'
PATH_TO_CSV = 'data_csv/drivers.csv'

create_table_from_csv(ENGINE,
                      PATH_TO_CSV,
                      table_name=TABLE_NAME,
                      fields=[
                            ('driver_id', 'integer'),
                            ('driver_ref', 'string'),
                            ('number', 'integer'),
                            ('code', 'string'),
                            ('forename', 'string'),
                            ('surname', 'string'),
                            ('dob', 'date'),
                            ('nationality', 'string'),
                            ('url', 'string')],
                      create_id=True
                  )


TABLE_NAME = 'qualifying'
PATH_TO_CSV = 'data_csv/qualifying.csv'

create_table_from_csv(ENGINE,
                      PATH_TO_CSV,
                      table_name=TABLE_NAME,
                      fields=[
                            ('qualify_id', 'integer'),
                            ('race_id', 'integer'),
                            ('driver_id', 'integer'),
                            ('constructor_id', 'integer'),
                            ('number', 'integer'),
                            ('position', 'integer'),
                            ('q1', 'string'),
                            ('q2', 'string'),
                            ('q3', 'string')],
                      create_id=True
                  )



TABLE_NAME = 'races'
PATH_TO_CSV = 'data_csv/races.csv'

create_table_from_csv(ENGINE,
                      PATH_TO_CSV,
                      table_name=TABLE_NAME,
                      fields=[
                            ('race_id', 'integer'),
                            ('year', 'integer'),
                            ('round', 'integer'),
                            ('circuit_id', 'integer'),
                            ('name', 'string'),
                            ('date', 'date'),
                            ('time', 'string'),
                            ('url', 'string')],
                      create_id=True
                  )