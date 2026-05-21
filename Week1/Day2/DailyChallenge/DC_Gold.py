# The matrix string
matrix_string = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# Step 1: Convert the string into a 2D list (rows and columns)
rows = matrix_string.split("\n")
matrix = [list(row) for row in rows]

# Step 2: Read each column from top to bottom
columns = []
for col in range(len(matrix[0])):
    column = ""
    for row in range(len(matrix)):
        column += matrix[row][col]
    columns.append(column)

# Step 3: Extract only alpha characters, replace symbol groups with a space
message = ""
for column in columns:
    for char in column:
        if char.isalpha():
            message += char
        else:
            # Add a space only if the last character wasn't already a space
            if message and message[-1] != " ":
                message += " "

# Step 4: Clean up and print the result
message = message.strip()
print(message)