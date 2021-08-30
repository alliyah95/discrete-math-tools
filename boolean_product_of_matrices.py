def main():
    check_matrices_validity()


def check_matrices_validity():
    print(" Enter the dimensions of the two matrices.\n Format: rows of matrix 1, cols of matrix 1, rows of matrix 2, cols of matrix 2")
    print(" Sample input for multiplying a 2x3 matrix with a 3x2: 2 3 3 2 ")
    while True:
        try:
            row1, col1, row2, col2 = input(" --> ").split()
        except ValueError:
            print(" Please only input four numeric values separated by a space.")
        else:
            dimensions = [row1, col1, row2, col2]

            if not all(num.isdigit() for num in dimensions):
                print(" Enter numeric values only!")
            else:
                if dimensions[1] == dimensions[2] and all(int(num) > 0 for num in dimensions):
                    matrix_one = get_matrix(row1, col1)
                    matrix_two = get_matrix(row2, col2)
                    multiply_matrices(matrix_one, matrix_two, row1, col2)
                    break
                else:
                    print(" The matrices cannot be multiplied.\n The number of columns of matrix 1 must be equal to the number of rows of matrix 2.\n Values must be greater than 0.")


def get_matrix(num_rows, num_cols):
    row_ctr = 0
    matrix = []
    valid_length = True
    valid_values = True

    print("\n Input each row of the first matrix. Separate each value with a space.\n Sample input: 0 0 0 0 1 0 ")
    while row_ctr != int(num_rows):
        print(f"\n Row {row_ctr+1}: ")
        row = input(" ").split()

        if len(row) != int(num_cols):
            valid_length = False

        for ele in row:
            if ele == '0' or ele == '1':
                continue
            else:
                valid_values = False
                break

        if valid_length and valid_values:
            row_ctr+=1
            matrix.append([int(value) for value in row])
        else:
            if not valid_values:
                print(" The matrix can only contain zeroes or ones.")
                valid_values = True

            if not valid_length:
                print(f" The length of each row must be equal to {num_cols}.")
                valid_length = True

    return matrix


def multiply_matrices(matrix_one, matrix_two, product_row, product_col):
    matrix_product = [[0 for i in range(int(product_col))] for j in range(int(product_row))]

    for x in range(len(matrix_one)):
        for y in range(len(matrix_two[0])):
            for z in range(len(matrix_two)):
                matrix_product[x][y] = matrix_product[x][y] or (matrix_one[x][z] and matrix_two[z][y])

    print_bool_product(matrix_product)


def print_bool_product(matrix):
    print("\n"+"BOOLEAN PRODUCT".center(30,"-"))
    for row in matrix:
        print(f"{row}".center(30))
    print("-"*30)


main()
