def fibonacci_1(n):
    if n <= 0:
        print("Invalid input!")
    elif n <= 2:
        return n-1
    else:
        return fibonacci_1(n-1)+fibonacci_1(n-2)


def fibonacci_2(n):
    fibonacci_array = [0,1]
    if n < 0:
        print("Invalid input!")
    elif n <= 2:
        return fibonacci_array[n-1]
    else:
        for i in range(2,n):
            fibonacci_array.append(fibonacci_array[i-1] + fibonacci_array[i-2])
        return fibonacci_array[-1]


def tester():
    n = int(input("Enter a number: "))
    nth_fib = fibonacci_1(n)
    print("The %d-th fibonacci number is %d" % (n, nth_fib))
    
    n = int(input("Enter a number: "))
    nth_fib = fibonacci_2(n)
    print("The %d-th fibonacci number is %d" % (n, nth_fib))

def main():
    tester()
    

if __name__ == '__main__':
    main()