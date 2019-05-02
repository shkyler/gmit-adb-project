import pymysql
## global variable to track connections
conn = None

def connect():
  ## use the global connection variable to connect
  global conn
  conn = pymysql.connect(user="root", password="root", db="world", host="localhost", cursorclass=pymysql.cursors.DictCursor)

def get_15_cities():
  # connect to the DB if not already
  if(not conn):
    connect();
  ## define a query
  get = "SELECT * FROM city LIMIT 15"
  ## with the connection..
  with conn:
    ## ...define a cursor ..
    cursor = conn.cursor()
    ## .. execute the query..
    cursor.execute(get)
    ## .. and return the result
    return cursor.fetchall()

def cities_by_pop(operator, population):
  # connect to the DB if not already
  if(not conn):
    connect();
  # check the operator and run the appropriate query
  if operator == ">":
    get = "SELECT * FROM city WHERE population > %s"
  elif operator == "<":
    get = "SELECT * FROM city WHERE population < %s"
  elif operator == "=":
    get = "SELECT * FROM city WHERE population = %s"
  ## with the connection..
  with conn:
    # ...define a cursor ..
    cursor = conn.cursor()
    ## .. execute the query..
    cursor.execute(get,(population))
    ## .. and return the result
    return cursor.fetchall()    