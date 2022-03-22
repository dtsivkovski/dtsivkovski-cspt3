def matrixfunc(list):
    for i in list:
        # prints all elements in each list i 
        print(*i)
    return(list)

def matrix_tester():
    # Asks for an integer of how many rows
    rowcount = int(input("How many rows? (integer input) - "))
    matrix = []
    # Loop for finding values for each row, splitting each value by the comma
    for row in range(0, rowcount):
      s = input("Input values separated by commas for Row #" + str(row) + " - ")
      rowvalue = s.split(",")
      matrix.append(rowvalue)
    # Prints matrix and formatted
    print("=" * 25)
    print("Your original matrix is: ")
    print(matrix)
    print("=" * 25)
    print("Your formatted matrix is: ")
    matrixfunc(matrix)

# this only applies if the file is run as main
if __name__ == "__main__":
    matrix_tester()