matrix_size = int(input("Please enter the size for your SQUARE Matrix:  "))

# Now I want to populate the matrix with users values
matrix = []

for row in range(matrix_size):
    current_row = []
    for column in range(matrix_size):
        val = int(input(f"Please enter your value for the matrix at index {[row]}{[column]} "))
        current_row.append(val)
        
    matrix.append(current_row)    
        

print("This is your customized Matrix:  ")
for i in range(len(matrix)):
    print(matrix[i])


def search_value(matrix):
    target = int(input("Enter the value to search for: "))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == target:
                print(f"Found {target} at index {row} {col}")
                
                
                
                

def main_diagonal(matrix):
    main_sum = 0
    n = len(matrix)
    for i in range(n):
        main_sum += matrix[i][i]
        
    print(f"The main diagonal sum is {main_sum}")    
    


def sec_diagonal(matrix):
    sec_sum = 0
    n = len(matrix)
    for i in range(n):
        sec_sum += matrix[i][n-1-i]
    
    
    print(f"The secondary diagonal sum is {sec_sum}")
    


def largest_val(matrix):
    largest = matrix[0][0]
    l_row = 0
    l_col = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                l_row = i
                l_col = j
    print(f"Largest value is {largest} at index {l_row} {l_col}")
    
    
    

def transpose_mat(matrix):
    transpose_matrix = []
    col_len = len(matrix[0])
    for i in range(col_len):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
            
        transpose_matrix.append(new_row)         
    print(f"The transposed matrix is {transpose_matrix}")
 
 


 