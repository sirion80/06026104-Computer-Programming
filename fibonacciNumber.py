# fibonacciNumber.py return the nth fibonacci number from the given n

def main():
    n = eval(input('Please enter fibonacci number: '))

    fn_1 = 0
    fn_2 = 1
    output = 0

    if n==1:
        output = fn_2
    else:
        for i in range(1, n):
            output = fn_1 + fn_2
            fn_1 = fn_2
            fn_2 = output

    print('F({0}): {1}'.format(n, output))

if __name__ == '__main__':
    main()
