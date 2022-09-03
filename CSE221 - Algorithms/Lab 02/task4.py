import sys


def merge(arr, p, q, r):
    n1 = q - p + 1 
    n2 = r - q
    L = [None for i in range(n1+2)]
    R = [None for i in range(n2+2)]
    for i in range(1, n1+1):
        L[i] = arr[p+i-1]
    for j in range(1, n2+1):
        R[j] = arr[q+j]
    L[n1+1] = sys.maxsize
    R[n2+1] = sys.maxsize
    i = 1
    j = 1
    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
    

def merge_sort(arr, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


def tester():
    sys.stdin = open('input4.txt', 'r')
    sys.stdout = open('output4.txt', 'w')
    
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split(' ')))
    
    merge_sort(arr, 0, n-1)
    print(' '.join(list(map(str, arr))))


def main():
    tester()


if __name__ == '__main__':
    main()