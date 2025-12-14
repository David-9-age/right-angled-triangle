# Mirrored right-angled triangle pattern

rows = 5  # Number of rows in the triangle

for i in range(1, rows + 1):
    # Print spaces first
    print(" " * (rows - i), end="")
    # Then print stars
    print("*" * i)
