def print_grid(n):
    for i in range(0, n):
        if i % 5 == 0:
           print('+ - - - - + - - - - +')
        else:
           print('|         |         |')

print_grid(11)