class Fibonacci:
    def __init__(self):
        self.fiboSeq = [0, 1]

    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2) # two recursive calls to self (__call__(self, n))
            self.fiboSeq.append(fib_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.fiboSeq[n]
    
    def printseq(self):
        print("-"*45, "\nSequence: \n", *self.fiboSeq)

class Factorial:
    # init creates a factorial sequence list
    def __init__(self):
        self.factorial = []

    # factorial function to find the last value and append all previous ones
    def __call__(self,n):
        if n == 1 or n == 0:
            self.printseq()
            return 1
        else:
            # print(n)
            self.factorial.append(n)
            return n * self(n-1)

    # print sequence function for factorial
    def printseq(self):
        print("-"*45, "\nSequence: \n", *self.factorial)

class LCM:
    # Only needs a call, no init because no defined properties
    def __call__(self, a, b):
        if (a > b):
            maximum = a
        else:
            maximum = b
        while (True):
            if (maximum % a == 0 and maximum % b == 0):
                break
            maximum = maximum + 1
        return maximum


def lcm_run():
    # Tester 1
    a = 9227 # int(input("Input your first value: "))
    b = 377 # int(input("Input your second value: "))
    lcm = LCM()
    result = lcm(a,b)
    print("-"*45, "\nThe least common multiple of", a, "and", b, "is", result)
    # Tester 2
    a = 10
    b = 8
    result = lcm(a,b)
    print("-"*45, "\nThe least common multiple of", a, "and", b, "is", result)

def factorial_run():
    # tester 1
    n = 9 # int(input("Input a number for your factorial: "))
    facto = Factorial()
    result = facto(n)
    print("-"*45, "\nThe factorial of", n, "is", result)


def fib_run():
    # Tester 1
    n = 9 # int(input("Input a number for your fibonacci: "))
    fibo_of = Fibonacci() # object instantiation and run __init__ method
    result = fibo_of(n)
    fibo_of.printseq()
    print("-"*45, "\nThe fibonacci of", n ,"is", result) # object running __call__ method
    
class Consec_Nums:
  # init defines num which is input for user
  def __init__(self, num):
    self.num = num
  def __call__(self):
    # since 0 is the first number, there are no numbers before it, so there is no sequnetial sum
    if self.num <= 0:
      print("No sequencial sum for this number")
    else:
      n = 0
      # for loop ends with the length of input + 1, because length starts at 0 while range starts at 1 (so the max number needs to be increased by one)
      for i in range (1, int(self.num) + 1):
        n = n + i
      print("The sum of all the numbers from 1 to", self.num, "is", n)

# allows users to put input into sequential sum instead of using tester
def consec_print():
  inp = int(input("Enter a number you want to find the sequential sum of: "))
  func = Consec_Nums(inp)
  func() # uses call function from class

if __name__ == "__main__":
    factorial_run()
    fib_run()
    lcm_run()
    consec_print()
