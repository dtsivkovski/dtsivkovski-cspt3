from tkinter.simpledialog import askstring


class multiply: 
    def __init__(self):
        self.col1 = []
        self.col2 = []
        self.col3 = []
        self.col4 = []
        
    def __call__(self, n):
        print("="*20)
        print("Original Number:", n)
        # Filter out values that won't work
        
        print("-" * 20)
        if int(n) > 99 or int(n) < 10:
            print("Invalid integer, must be from 10-99")
        else:
            # Create str, a and b default values
            string = str(n)
            a = int("0" + string[0])
            b = int("0" + string[1])

            # Append values for 0 index (starting)
            self.col1.append(a)
            self.col2.append(b)
            self.col3.append("(" + f'{a:02d}' + "+" + str(0) + ")")
            self.col4.append(n)
            # Prints 0th row in the table
            print(f'{self.col1[0]:02d}', f'{self.col2[0]:02d}', self.col3[0], self.col4[0])
            for i in range (2, 12):
                # Creates sub values for each multiplication factor
                sn = i * n
                sa =  i * a
                sb = i * b
                # Append sub values
                self.col1.append(sa)
                self.col2.append(sb)
                # Show adding value of sa + the first number of sb
                self.col3.append("(" + f'{sa:02d}' + "+" + f'{(sb):02d}'[0] + ")")
                self.col4.append(sn)
                # Print all columb values
                print(f'{self.col1[i-1]:02d}', f'{self.col2[i-1]:02d}', self.col3[i-1], self.col4[i-1])
            print("=" * 20)


def multiplytester(n):
    function = multiply()
    function(n)


if __name__ == "__main__":
    multiplytester(18)
    multiplytester(87)
    multiplytester(99)