import sys
import heapq


def parse_data_from_file(filename):
    data = []
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        for i in range(n):
            s, e = f.readline().strip().split(' ')
            heapq.heappush(data, (int(e), int(s)))
    return data

def Assignment_Selection(arr, n):
    e, s = heapq.heappop(arr)
    selected = [(s, e)]
    while arr:
        e, s = heapq.heappop(arr)
        if selected[-1][1] <= s:
            selected.append((s, e))
    print(len(selected))
    print('\n'.join([str(i[0])+' '+str(i[1]) for i in selected]))


def main():
    sys.stdout = open('task1_output.txt', 'w')
    arr = parse_data_from_file('task1_input.txt')
    Assignment_Selection(arr, len(arr))


if __name__=="__main__":
    main()