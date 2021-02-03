from sqlalchemy import *
import subprocess
import sqlalchemy.dialects.mysql

config = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'moi',
    'password' : 'iom',
    'database' : 'classicmodels'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

engine = create_engine(connection_str)
connection = engine.connect()
print('--- MySQL Docker Container Python connection ok ---\n')

print('--- docker ps info ---\n')
returned_value = subprocess.call("docker ps", shell=True)

print('\n--- Tables into database---\n')

with engine.connect() as connection:
    result = connection.execute("show tables")
    print(result)


    rs = connection.execute("select * from offices order by country,state,city;")
    for row in rs:
        print(row)