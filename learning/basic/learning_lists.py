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

print(return_number_list("25"))