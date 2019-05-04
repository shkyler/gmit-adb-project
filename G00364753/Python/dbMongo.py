import pymongo
## global variable to track connections
myclient = None

def connect():
  ## use the global connection variable to connect
  global myclient
  myclient = pymongo.MongoClient()
  myclient.admin.command('ismaster')

def find_car(size):
  # connect to the data base is not already connected
  if not myclient:
    connect()
  # specfity DB and collection details
  myDB = myclient["mongo"]
  myCollection = myDB["docs"]  
  # define the query, run it and return the results
  query =  {"car.engineSize":size}
  cars = myCollection.find(filter=query)
  return cars

def add_car(ID, registration, engine_size):
  # connect to the data base is not already connected
  if not myclient:
    connect()  
    # specfity DB and collection details
  myDB = myclient["mongo"]
  myCollection = myDB["docs"]
  ins = {"_id": ID, "car":{"reg":registration, "engineSize": engine_size}}
  myCollection.insert(ins) 
