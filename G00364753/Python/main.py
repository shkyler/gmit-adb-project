## Patrick Moore - GMIT - G00364753 - Applied Databases Project
import pymysql
import dbConnect

def return_15():
  ## query the database
  cities = dbConnect.get_15_cities()
  ## format the output
  for city in cities:
    print(city["ID"],'|',city["Name"], '|', city["CountryCode"], '|', city["District"], '|', city["Population"])

def return_city_pop():
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
      print("ERROR - you must enter a number, please try again")
      main()
  ## format the output
  for city in cities:
    print(city["ID"],'|',city["Name"], '|', city["CountryCode"], '|', city["District"], '|', city["Population"])

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
    print("You selected 3!")
    main()
  elif choice == "4":  
    print("You selected 4!")
    main()  
  elif choice == "5":  
    print("You selected 5!")
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