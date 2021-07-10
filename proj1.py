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
    empty_value = ''
    for line in fileContent:
        matrix_row = line.split(' ')

        while ( empty_value in matrix_row ):
            matrix_row.remove(empty_value)

        matrix.append(matrix_row)        

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
    file = open(file_name_out, "w")
    file.write("Det: " + "{:.1f}".format(determinant))
    file.write ("\n\n")

    if inverse_matrix == None:
        file.write ("Can't find inverse matrix")
    else:
        n = len (inverse_matrix)
        for i in range(0, n):
            for j in range(0, n):
                if (inverse_matrix[i][j] < 0) == False:
                    file.write(' ')
                inverse_matrix[i][j] = "{:.1f}".format(inverse_matrix[i][j])
                file.write(str(inverse_matrix[i][j]) + ' ')
            file.write('\n')
        
    file.close()
    
    
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
    return res

def swap_rows(row_a, row_b):
    n = len(row_a)
    for i in range(0, n):
        temp = row_a[i]
        row_a[i] = row_b[i]
        row_b[i] = temp

def gauss_jordan(matrix):
    matrix_row = len(matrix)
    matrix_col = len(matrix[0])

    for i in range(0, matrix_row):
    # The main diagonal must not have 0
        if matrix[i][i] == 0:
            for row in range(i + 1, matrix_row):
                if matrix[row][i] != 0:
                    swap_rows(matrix[i], matrix[row])
                    break

    # The main diagonal must be 1 & the 2 triangle must be 0
        # The main diagonal must be 1
        divide_value = matrix[i][i]
        for col in range (0, matrix_col):
            matrix[i][col] = matrix[i][col] / divide_value

        # The 2 triangle must be 0
        for row in range(0, matrix_row):
            if row != i:
                divide_value = matrix[row][i] / matrix[i][i]
                for col in range(0, matrix_col):
                    matrix[row][col] = matrix[row][col] - (divide_value) * matrix[i][col]           

    # Split matrix to get te final result
    res = []
    row = []
    for i in range (0, matrix_row):
        for j in range (matrix_row, matrix_col):
            row.append(matrix[i][j])
        res.append(row.copy())
        row.clear()
    
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

    n = len(matrix)
    for i in matrix:
        if len(i) != n:
            return None #not a square matrix

    #use the copy matrix to caculate so that the oroginal matrix wont be affected
    matrix_copy = []
    for i in range (0, n):
        row_copy = matrix[i].copy()
        matrix_copy.append(row_copy)

    divide_by_zero = False
    for i in range(0, n):
        if matrix_copy[i][i] == 0:
            divide_by_zero = True
            for row in range(i + 1, n):
                if matrix_copy[row][i] != 0:
                    divide_by_zero = False
                    swap_rows(matrix_copy[i], matrix_copy[row])
                    break
            if divide_by_zero: return 0 
            # The main diagnoal has a 0 -> There will be a row or a column contains all 0 value -> det = 0

        # The 2 triangle must be 0
        for row in range(i + 1, n):
            if row != i:
                divide_value = matrix_copy[row][i] / matrix_copy[i][i]
                for col in range(0, n):
                    matrix_copy[row][col] = matrix_copy[row][col] - (divide_value) * matrix_copy[i][col]

    # determinant = multiple of main diagnoal
    det = 1
    for i in range(0, n):
        det *= matrix_copy[i][i]

    if det >= 0: return det
    else: return -det

    # Split matrix to get te final result
    
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

    append_matrix = append_square_matrix(matrix, unit_matrix(len(matrix)))
    if append_matrix == None: return None #error

    res = gauss_jordan(append_matrix)
    return res     


def main():
    matrix = read_file(file_name_in='input.txt')
    
    det = calc_determinant_row_operation(matrix)
    inv_mat = invert_matrix_row_operation(matrix)
    
    write_file(file_name_out='19127287_output.txt', determinant=det, inverse_matrix=inv_mat)

if __name__ == "__main__":
    main()