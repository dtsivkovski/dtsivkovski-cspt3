# Factorial of a number using recursion
from numpy import kaiser

MAGENTA_COLOR = u"\u001b[35;1m"
COMP_COLOR = u"\u001B[0m\u001B[2D"

def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        print(n)
        return n * recur_factorial(n-1)

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
def recur_fibonacci(n,h,i,j):
    if h == 0:
        return n
    else:
        # adds previous two values together, assign new values
        n = i + j
        i = j
        j = n
        # print the value 
        print(n)
        return recur_fibonacci(n,h-1,i,j)

def fibonacci(n):
    h = 0
    i = 0
    j = 1
    while h < n:
        # adds previous two values together and prints it
        k = i + j
        print(k)
        # assigns the new previous values
        i = j
        j = k
        # adds 1 to the iteration count
        h += 1
    return k
    

def fibonacci_tester():
    num = int(input("Enter a number for fibonacci: "))
    print("-" * 25)
    if num < 0:
        print("Sorry, fibonacci does not exist for negative numbers.")
    else:
      try:
        result = fibonacci(num)
        print(MAGENTA_COLOR)
        print("The result of fibonacci", num, "times is", result)
        print(COMP_COLOR)
      except:
        print("Error - Invalid Input")
        print(COMP_COLOR)

def recur_fibonacci_tester():
  num = int(input("Enter a number for fibonacci: "))
  print("-" * 25)
  if num < 0:
      print("Sorry, fibonacci does not exist for negative numbers.")
  else:
    try:
        result = recur_fibonacci(0, num, 0, 1)
        print(MAGENTA_COLOR)
        print("The result of fibonacci", num, "times is", result)
        print(COMP_COLOR)
    except:
        print("Error - Invalid Input")
        print(COMP_COLOR)


# this is test driver or code that plays when executed directly, versus import which will not run these statements
def factorial_tester():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    print("-" * 25)
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print(MAGENTA_COLOR)
        print("The factorial of", num, "is", recur_factorial(num))
        print(COMP_COLOR)

# this only applies if the file is run as main
if __name__ == "__main__":
    recur_fibonacci_tester()