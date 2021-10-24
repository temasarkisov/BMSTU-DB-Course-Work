# driver, circuits, races, constructors, status, result 


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


'''TABLE_NAME = 'qualifying'
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
                  )'''



'''TABLE_NAME = 'lap_times'
PATH_TO_CSV = 'data_csv/lap_times.csv'

create_table_from_csv(ENGINE,
                      PATH_TO_CSV,
                      table_name=TABLE_NAME,
                      fields=[
                            ('race_id', 'integer'),
                            ('driver_id', 'integer'),
                            ('lap', 'integer'),
                            ('position', 'integer'),
                            ('time', 'string'),
                            ('milliseconds', 'integer')],
                      create_id=True
                  )'''



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



'''TABLE_NAME = 'pit_stops'
PATH_TO_CSV = 'data_csv/pit_stops.csv'

create_table_from_csv(ENGINE,
                      PATH_TO_CSV,
                      table_name=TABLE_NAME,
                      fields=[
                            ('race_id', 'integer'),
                            ('driver_id', 'integer'),
                            ('stop', 'integer'),
                            ('lap', 'integer'),
                            ('time', 'string'),
                            ('duration', 'string'),
                            ('milliseconds', 'integer')],
                      create_id=True
                  )'''



TABLE_NAME = 'constructors'
PATH_TO_CSV = 'data_csv/constructors.csv'

create_table_from_csv(ENGINE,
                      PATH_TO_CSV,
                      table_name=TABLE_NAME,
                      fields=[
                            ('constructor_id', 'integer'),
                            ('constructor_ref', 'string'),
                            ('name', 'string'),
                            ('nationality', 'string'),
                            ('url', 'string')],
                      create_id=True
                  )



'''TABLE_NAME = 'driver_standings'
PATH_TO_CSV = 'data_csv/driver_standings.csv'

create_table_from_csv(ENGINE,
                      PATH_TO_CSV,
                      table_name=TABLE_NAME,
                      fields=[
                            ('driver_standings_id', 'integer'),
                            ('race_id', 'integer'),
                            ('driver_id', 'integer'),
                            ('points', 'integer'),
                            ('position', 'integer'),
                            ('position_text', 'string'),
                            ('wins', 'integer')],
                      create_id=True
                  )'''



TABLE_NAME = 'results'
PATH_TO_CSV = 'data_csv/results.csv'

create_table_from_csv(ENGINE,
                      PATH_TO_CSV,
                      table_name=TABLE_NAME,
                      fields=[
                            ('result_id', 'integer'),
                            ('race_id', 'integer'),
                            ('driver_id', 'integer'),
                            ('constructor_id', 'integer'),
                            ('number', 'integer'),
                            ('grid', 'integer'),
                            ('position', 'integer'),
                            ('position_text', 'string'),
                            ('position_order', 'integer'),
                            ('points', 'integer'),
                            ('laps', 'integer'),
                            ('time', 'string'),
                            ('milliseconds', 'integer'),
                            ('fastest_lap', 'integer'),
                            ('rank', 'integer'),
                            ('fastest_lap_time', 'string'),
                            ('fastest_lap_speed', 'string'),
                            ('status_id', 'integer'),
                            ],
                      create_id=True
                  )



TABLE_NAME = 'status'
PATH_TO_CSV = 'data_csv/status.csv'

create_table_from_csv(ENGINE,
                      PATH_TO_CSV,
                      table_name=TABLE_NAME,
                      fields=[
                            ('status_id', 'integer'),
                            ('status', 'string'),
                            ],
                      create_id=True
                  )



TABLE_NAME = 'circuits'
PATH_TO_CSV = 'data_csv/circuits.csv'

create_table_from_csv(ENGINE,
                      PATH_TO_CSV,
                      table_name=TABLE_NAME,
                      fields=[
                            ('circuit_id', 'integer'),
                            ('circuit_ref', 'string'),
                            ('name', 'string'),
                            ('location', 'string'),
                            ('country', 'string'),
                            ('lat', 'float'),
                            ('lng', 'float'),
                            ('alt', 'float'),
                            ('url', 'string')],
                      create_id=True
                  )                  