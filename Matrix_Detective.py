matrix_size = int(input("Please enter the size for your SQUARE Matrix:  "))

# Now I want to populate the matrix with users values
matrix = []

for row in range(matrix_size):
    current_row = []
    for column in range(matrix_size):
        val = int(input(f"Please enter your value for the matrix at index {[row]}{[column]} "))
        current_row.append(val)
        
    matrix.append(current_row)    
        

print("This is your customised Matrix:  ",matrix)

