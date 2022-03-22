

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

if __name__ == "__main__":
    fibo_of = Fibonacci() # object instantiation and run __init__ method
    result = fibo_of(5)
    fibo_of.printseq()
    print("The final result is: ", result) # object running __call__ method