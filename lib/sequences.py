#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        return print([])
    elif length == 1 :
        return print([0])
    else:
        fibonacci_list = [0, 1]
        for i in range(2, length):
            next_value = fibonacci_list[-1] + fibonacci_list [-2]
            fibonacci_list.append(next_value)
        print(fibonacci_list)

print_fibonacci(0)