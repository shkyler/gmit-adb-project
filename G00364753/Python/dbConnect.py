import pymysql
import getpass
## global variable to track connections
conn = None

def connect():
  ## use the global connection variable to connect
  global conn
  while True:
    # ask the user for a username and password
    try:
      user_name = input("Please enter MySQL username: ")
      # getpass is used so that the password is not shown on the command line when typed
      user_pw = getpass.getpass("Please enter MySQL password: ")
      conn = pymysql.connect(user=user_name, password=user_pw, db="world", host="localhost", cursorclass=pymysql.cursors.DictCursor)
      break
    # if username or password is incorrect, inform the user and try again  
    except pymysql.err.OperationalError:
      print("Incorrect username or password, please try again.")

def get_15_cities():
  # connect to the DB if not already
  if(not conn):
    connect()
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
    connect()
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

def add_city(name, country_code, district, population):
  # connect to the DB if not already
  if not conn:
    connect()
  # define a query to add a city
  add = ("INSERT INTO city (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s)")      
  ## with the connection..
  with conn:
    # ...define a cursor ..
    cursor = conn.cursor()
    ## .. execute the query..
    cursor.execute(add, (name, country_code, district, population))
    ## .. and return the result
    return cursor.fetchall()

def get_countries():
  # connect to the DB if not already
  if(not conn):
    connect()
  ## define a query
  get = "SELECT * FROM country"
  ## with the connection..
  with conn:
    ## ...define a cursor ..
    cursor = conn.cursor()
    ## .. execute the query..
    cursor.execute(get)
    ## .. and return the result
    return cursor.fetchall()
