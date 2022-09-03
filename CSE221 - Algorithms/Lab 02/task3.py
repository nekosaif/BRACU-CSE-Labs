import sys


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp_0 = arr[i][0]
        temp_1 = arr[i][1]
        j = i - 1
        while j >= 0:
            if arr[j][1] >= temp_1:
                break
            arr[j+1][0] = arr[j][0]
            arr[j+1][1] = arr[j][1]
            j -= 1
        arr[j+1][0] = temp_0
        arr[j+1][1] = temp_1


def tester():
    sys.stdin = open('input3.txt', 'r')
    sys.stdout = open('output3.txt', 'w')
    
    n = int(sys.stdin.readline().strip())
    id_arr = list(map(int, sys.stdin.readline().strip().split(' ')))
    marks_arr = list(map(int, sys.stdin.readline().strip().split(' ')))
    combine_arr = [[id_arr[i], marks_arr[i]] for i in range(n)]

    insertion_sort(combine_arr)
    
    print(' '.join([str(i[0]) for i in combine_arr]))


def main():
    tester()


if __name__ == '__main__':
    main()