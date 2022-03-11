def matrix(list):
    for i in list:
        # prints all elements in each list i 
        print(*i)
    return(list)

def matrix_tester():
    matrix1 = [ [1,2,3],[4,5,6],[7,8,9] ]
    matrix(matrix1)
    matrix2 = [ [1,2,3],[4,5,6],[7,8,9],[10,11,12] ]
    matrix(matrix2)

# this only applies if the file is run as main
if __name__ == "__main__":
    matrix_tester()