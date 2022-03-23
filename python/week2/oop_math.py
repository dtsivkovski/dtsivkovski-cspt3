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
        print("Sequence: \n", *self.fiboSeq)

class Factorial:
    def __init__(self):
        self.factorial = []

    def __call__(self,n):
        if n == 1 or n == 0:
            self.printseq()
            return 1
        else:
            # print(n)
            self.factorial.append(n)
            return n * self.__call__(n-1)
    
    def printseq(self):
        print("Sequence: \n", *self.factorial)


def factorial_run():
    n = int(input("Input a number for your factorial: "))
    facto = Factorial()
    result = facto(n)
    print("The factorial of", n, "is", result)


def fib_run():
    n = int(input("Input a number for your fibonacci: "))
    fibo_of = Fibonacci() # object instantiation and run __init__ method
    result = fibo_of(n)
    fibo_of.printseq()
    print("The final result is: ", result) # object running __call__ method
    

if __name__ == "__main__":
    factorial_run()
    fib_run()
