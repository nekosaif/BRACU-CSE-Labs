import sys


def selection_sort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i, len(arr)):
            if arr[j] <= arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
        

def tester():
    sys.stdin = open('input2.txt', 'r')
    sys.stdout = open('output2.txt', 'w')
     
    N, M = list(map(int, sys.stdin.readline().strip().split()))
    arr = list(map(int, sys.stdin.readline().strip().split(' ')))
      
    selection_sort(arr)
    
    print(' '.join(list(map(str, arr[:M:]))))


def main():
    tester()


if __name__ == '__main__':
    main()