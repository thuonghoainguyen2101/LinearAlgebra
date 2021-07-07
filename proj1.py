from copy import *

def read_file(file_name_in):
    '''
    Read matrix from file
    
    Inputs:
        file_name_in : str
            The name of input file
            
    Outputs:
        marix : list (of list)
            Matrix which is read from file
    '''
    
    # YOUR CODE HERE
    file = open(file_name_in, "r")
    fileContent = file.read().split('\n')
    file.close()

    matrix=[]
    for line in fileContent:
        matrix.append(line.split(' '))

    print(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = float(matrix[i][j])

    return matrix
    
    
def write_file(file_name_out, determinant, inverse_matrix):
    '''
    Write determinant and inversed matrix into file
    
    Inputs:
        file_name_out : str
            The name of output file
            
        determinant : int or float
            The determinant of matrix read from input file
        
        inversed_matrix : list (of list)
            The inverse of matrix read from input file
    '''
    
    # YOUR CODE HERE
    
    
# YOUR OTHER FUNCTIONS
def sub_matrix(matrix, delete_row, delete_column):
    sub_matrix = deepcopy(matrix)
    sub_matrix.pop(delete_row)
    for row in sub_matrix:
        row.pop(delete_column)
    return sub_matrix

def unit_matrix(n):
    matrix = []
    for i in range(0, n):
        matrix.append([0.0] * n)
        matrix[i][i] = 1.0
    return matrix
            
def append_square_matrix(a, b):
    n = len(a)
    n_b = len(b)
    if n != n_b: return None #cant append matrix
    res = [0] * n
    
    for i in range(0, n):
        res[i] = a[i] + b[i]
    print(res)
    return res

def gauss_jordan(matrix):
    n = len(matrix)
    for i in range (0, n):
        print(matrix[i])
        if matrix[i][i] == 0:
            
            return False #divide by zero -> ERROR!!
        for j in range(0, n):
            if i != j:
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(0, 2*n):
                    #print(i, j, k)
                    matrix[j][k] -= ratio * matrix[i][k]

    for i in range(n):
        divisor = matrix[i][i]
        for j in range(2*n):
            matrix[i][j] = matrix[i][j]/divisor

    res = []
    for i in range(0, n):
        res.append([])
        for j in range(n, 2*n):
            res[i].append(matrix[i][j])
    print(res)
    return res

def calc_determinant_row_operation(matrix):
    '''
    Calculate determinant of input matrix
    
    Inputs:
        marix : list (of list)
            Matrix which is read from file
            
    Outputs:
        determinant : int or float
            The determinant of input matrix
    '''
    
    # YOUR CODE HERE
    
    numRow = len(matrix)
    for row in matrix:
        if len(row) != numRow:
            return None #not a square matrix -> det(matrix) = None

    #base case
    if numRow == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    det = 0.0
    for i in range(0, len(matrix)):
        #khai trien dinh thuc theo dong thu 0
        det += (-1)**(1 + i) * matrix[0][i] * calc_determinant_row_operation(sub_matrix(matrix, 0, i))
    return det
            

    
def invert_matrix_row_operation(matrix):
    '''
    Invert a matrix
    
    Inputs:
        marix : list (of list)
            Matrix which is read from file
            
    Outputs:
        inverse_matrix : list (of list) or None
            The inverse of input matrix
            `None` when the input matrix is not invertible
    '''
    
    # YOUR CODE HERE
    det = calc_determinant_row_operation(matrix)
    if det == None or det == 0:
        return None #matrix khong kha nghich

    res = append_square_matrix(matrix, unit_matrix(len(matrix)))
    if res == None: return None #error

    return gauss_jordan(res)
    
    numNodes = len(matrix)
    # for i in range (0, numNodes):
        


def main():
    matrix = read_file(file_name_in='input.txt')
    print("det = " , calc_determinant_row_operation(matrix))
    #det = calc_determinant_row_opertion(matrix)
    #inv_mat = invert_matrix_row_operation(matrix)
    print(invert_matrix_row_operation(matrix))
    #write_file(file_name_out='MSSV_output.txt', determinant=det, inverse_matrix=inv_mat)

if __name__ == "__main__":
    main()