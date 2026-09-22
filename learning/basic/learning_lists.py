#returns a string of numbers from 1 to n
def return_number_list(n):
    if (isinstance(n, str) and not n.isdigit()) or isinstance(n, bool):
        return "Argument must be an integer"
    else:
        n = int(n)
    if not isinstance(n, int):
        return "Argument must be an integer"
    if n < 1:
        return "Argument must be greater than 0"

    return " ".join(str(x) for x in range(1,n+1))

# Indexed Value Pairer
# Goal: Accept a list of strings and produce a new list where each item is a tuple consisting of (index, value.upper()).
# Primary Focus: enumerate(), .upper()
# Data Types Explored: List, Tuple
def generate_tuple(strings):
    return list((index, string.upper()) for index, string in enumerate(strings))


# Coordinate Bounds Finder
# Goal: Accept a list of 2D coordinate tuples [(x1, y1), (x2, y2), ...] and return a single tuple containing (min_x, max_x, min_y, max_y).
# Primary Focus: Tuple unpacking in a for loop, min(), max()
# Data Types Explored: List of Tuples, Tuple
def coordinate_bounds_finder(coords):
    if not coords:
        return "Coords must contain integer digits"
    x_values = []
    y_values = []
    for x, y in coords:
        if isinstance(x, str) and x.isdigit():
            x=int(x)
        if isinstance(y, str) and y.isdigit():
            y=int(y)
        if isinstance(x, int) and isinstance(y, int):
            x_values.append(x)
            y_values.append(y)
        else:
            return "All elements must be integer digits"
    return (min(x_values), max(x_values), min(y_values), max(y_values))
print(coordinate_bounds_finder([(1,"2"), (2,3), (3,4)]))
# Unique Element Counter & Sorter
# Goal: Accept a tuple containing repeated items and return a list of tuples formatted as (item, count), sorted in descending order based on the count.
# Primary Focus: Tuple method .count(), sorted() or .sort(), for loop
# Data Types Explored: Tuple input, List of Tuples output

# Parallel List Zipper with Filtering
# Goal: Accept two lists of equal length (e.g., names and scores) and return a single tuple containing only the names of individuals whose score is greater than or equal to a passing threshold (e.g., 70).
# Primary Focus: zip(), tuple() conversion, loop filtering
# Data Types Explored: List, Tuple

# Subsequence Extractor
# Goal: Accept a list of numbers and return a tuple containing two lists: the first containing only even numbers, and the second containing only odd numbers, maintaining their original order.
# Primary Focus: Modulo operator %, .append(), tuple() packing
# Data Types Explored: List, Tuple