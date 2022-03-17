# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "John",  
               "LastName": "Mortensen",  
               "Residence": "San Diego",  
               "Owns_Tech":["Laptop", "Phone", "Bitcoin Farm"]  
              })  

InfoDb.append({  
               "FirstName": "Daniel",  
               "LastName": "Tsivkovski",  
               "Residence": "San Diego",  
               "Owns_Tech":["Laptop","Desktop","Samsung Phone", "Tablet"]
              })  

InfoDb.append({  
               "FirstName": "Jason",  
               "LastName": "Ott",  
               "Residence": "San Diego",  
               "Owns_Tech":["Laptop","iPhone"]
              })  

InfoDb.append({  
               "FirstName": "Andrew",  
               "LastName": "Kim",  
               "Residence": "San Diego",  
               "Owns_Tech":["Desktop","iPhone", "Chromebook"]
              })  


def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Tech: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Tech"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

# for loop iterates on length of InfoDb
def for_loop():
    print("=" * 25)
    print("For loop")
    print("-" * 25)
    for n in range(len(InfoDb)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    print("=" * 25)
    print("While loop")
    print("-" * 25)
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def while_loop_run():
    while_loop(0)

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def recursive_loop_run():
    print("=" * 25)
    print("Recursive loop")
    print("-" * 25)
    recursive_loop(0)
    print("=" * 25)

def list_finder():
  num = int(input("Which index do you want to search (0-3): "))
  print("-" * 25)
  try:
    print(InfoDb[num]["FirstName"] + InfoDb[num]["LastName"])
    print("Residence: " + InfoDb[num]["Residence"])
    print("Owns Tech: ")
    for i in range (0)
  
  except:
    print("Invalid index given.")

def tester():
    
  for_loop()
  
  while_loop(0)  # requires initial index to start while
  
  recursive_loop_run(0)  # requires initial index to start recursion

  list_finder()

# this only applies if the file is run as main
if __name__ == "__main__":
    tester()