def staircase(n):
    final = ''
    for i in range(n):
        indent = ' ' * (n-i-1)
        cell = "#" * (i+1)
        combined = indent + cell + "\n"
        final += combined
    return print(final)