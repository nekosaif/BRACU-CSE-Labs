import sys


"""
Name: Mollah Md. Saif
Id:   20101416

In the given bubblesort, there are two for loops.
1st for loop run n(arr size) times
2nd for loop run n-1, n-2, n-3,...., 1 times
Total run time 1+2+3+4+.....+ n-1 = n(n-1)/2 = 0.5(n^2-n)
θ(n) = n^2

But in the following altered code, the first for breaks
if there is no for loop. Because if there is no swap any
instance of for loop that array is fully sorted and sort-
function breaks.
So, in the best-case when the array is sorted or close to
its sorted state, the  θ(n) = n
"""


def bubbleSort(arr):
    for i in range(len(arr)-1):
        swap_flag = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = True
        if not swap_flag:
            break


def tester():
    sys.stdin = open('input1.txt', 'r')
    sys.stdout = open('output1.txt', 'w')
    
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split(' ')))
    
    bubbleSort(arr)
    print(' '.join(list(map(str, arr))))


def main():
    tester()


if __name__ == '__main__':
    main()