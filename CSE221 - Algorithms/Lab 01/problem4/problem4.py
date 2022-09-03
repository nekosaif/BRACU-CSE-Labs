import sys


def multiply_matrix(a, b):
    c = [[0 for j in range(len(a))] for i in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                c[i][j] += (a[i][k] * b[k][j])
    return c


def tester():
    sys.stdin = open('input4.txt', 'r')
    sys.stdout = open('output4.txt', 'w')
    
    n = int(sys.stdin.readline())
    a, b = [], []
    
    for i in range(n):
        a.append(list(map(int, sys.stdin.readline().split(' '))))
    next(sys.stdin)
    for i in range(n):
        b.append(list(map(int, sys.stdin.readline().split(' '))))
    
    c = multiply_matrix(a, b)
    
    for line in c:
        print(' '.join(list(map(str, line))))


def main():
    tester()
        

if __name__ == '__main__':
    main()