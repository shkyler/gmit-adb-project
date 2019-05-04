## Patrick Moore - GMIT - G00364753 - Applied Databases Project
import pymysql
import dbConnect
import dbMongo

def return_15():
  ## query the database
  cities = dbConnect.get_15_cities()
  ## format the output
  print("View 15 Cities")
  print("--------------")
  for city in cities:
    print(city["ID"],'|',city["Name"], '|', city["CountryCode"], '|', city["District"], '|', city["Population"])

def return_city_pop():
  print("View Cities by Population")
  print("-------------------------")  
  ## defined the allowed operators
  allowed_operator = ['<','>','=']
  ## use a while loop to validate user input of the operator
  op_selected = input("Enter < > or = : ")
  while op_selected not in allowed_operator:
    op_selected = input("Enter < > or = : ")
  ## use error hadling to make the user enters number  
  while True:
    try:  
      pop_entered = int(input("Enter Population: "))
      cities = dbConnect.cities_by_pop(op_selected, pop_entered)
      break
    except ValueError as e:
      ## if a number is not entered - warn the user and start again
      print("**ERROR - you must enter a number, please try again**")
  ## format the output
  print("------------------")
  for city in cities:
    print(city["ID"],'|',city["Name"], '|', city["CountryCode"], '|', city["District"], '|', city["Population"])

def new_city():
  print("Add New City")
  print("----------------------")
  ## use a while loop until valid city data is entered
  while True:
    try:  
       ## get user input for the new city
      city_name = input("Enter city name: ")
      count_code = input("Country Code: ")
      dist_name = input("District: ")
      pop = int(input("Population: "))
      ## enter the data in the database  
      dbConnect.add_city(city_name, count_code, dist_name, pop)
      ## if the data is good, break from the while loop
      break
    ## catch errors related to the population being entered wrong  
    except ValueError:
      print("**ERROR - You must enter an integer for population, please try again**") 
    ## catch errors related to the country code being entered wrong   
    except pymysql.err.IntegrityError as e:
      print("**ERROR - You must enter a valid Country Code, please try again**")  
    ## catch any other error  
    except Exception as e:
      print("**ERROR - ", e, "**")   

def get_cars():
  print("Show Cars by Engine Size")
  print("------------------------")
  # use a while loop until valid data is entered
  while True:
    try:
      engine_size = float(input("Enter engine size: ")) 
      # run the query
      cars = dbMongo.find_car(engine_size)
      break
    # catch error related to incorrect data type entry  
    except ValueError as e:
      print("**ERROR - You must enter a number for engine size**")  
  print("----------------------------")
  # loop through the returned data and print
  for car in cars:
    try:
      # print the details of the car
      print(car["_id"], "|", car["car"]["reg"], "|", car["car"]["engineSize"],"|", car["addresses"])  
      # if no address is present in the record it throws a KeyError
    except KeyError:
      print(car["_id"], "|", car["car"]["reg"], "|", car["car"]["engineSize"])    


def new_car():
  print("Add New Car")
  print("-----------")  
  # use a while loop until valid data is entered
  while True:
    try:
      car_id = input("Enter car ID: ")
      car_reg = input("Enter car Registration: ")
      engine_size = float(input("Enter car engine size: "))
      dbMongo.add_car(car_id,car_reg,engine_size)
      break
    # ValueError will catch non-numeric engine sizes  
    except ValueError as e:
      print("**ERROR - You must enter a number for engine size**") 
    # other exceptions will catch duplicate ID numbers  
    except Exception:
      print("**ERROR - You must specify a unique ID for the car**")  
  # if sucessfull give the user some feedback    
  print("New car entered with ID: ", car_id)   
 

     
## main function acts as a user interface
def main():
  # print the main menu to the console
  print("World DB")
  print("________")
  print("        ")
  print("MENU")
  print("====")
  print("1 - View 15 Cities")
  print("2 - View Cities by Population")
  print("3 - Add New City")
  print("4 - Find Car by Engine Size")
  print("5 - Add New Car")
  print("6 - View Countries by Name")
  print("7 - View Countries by Population")
  print("x - Exit Application")
  # ask the user to pick an option
  choice = input("Choice:")
  # check the user input and call the appropriate function
  if choice == "1":
    return_15()
    main()
  elif choice == "2":  
    return_city_pop()
    main()
  elif choice == "3":  
    new_city()
    main()
  elif choice == "4":  
    get_cars()
    main()  
  elif choice == "5":  
    new_car()
    main()
  elif choice == "6":  
    print("You selected 6!")
    main()  
  elif choice == "7":  
    print("You selected 7!")
    main()  
  elif choice == "x":  
    quit()
  else:
    main() 

## call the main function to start the program
if __name__ == "__main__":
  main()