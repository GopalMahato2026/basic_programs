n = 5
for i in range(n):
    for j1 in range(i, n):
        print(" ", end=" ")
    for j2 in range(i):
        print("*", end=" ")
    for j3 in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n,-1, -1):
    for j1 in range(i, n):
        print(" ", end=" ")
    for j2 in range(i):
        print("*", end=" ")
    for j3 in range(i + 1):
        print("*", end=" ")
    print()
#####
def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    triangle = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * i
        triangle.append(spaces + stars)
    return triangle
def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The length of the longest word.
    """
    if not s:  # Check if string is empty
        return 0
    
    max_length = 0
    current_length = 0
    
    for char in s:
        if char == ' ' or char == '\t' or char == '\n':  # If we encounter a whitespace
            # Update max_length if current word is longer
            if current_length > max_length:
                max_length = current_length
            current_length = 0  # Reset current word length
        else:
            current_length += 1  # Increment current word length
    
    # Check for the last word (which might not be followed by a space)
    if current_length > max_length:
        max_length = current_length
        
    return max_length
