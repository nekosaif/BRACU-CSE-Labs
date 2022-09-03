import sys
import heapq


def parse_data_from_file(filename):
    data = []
    with open(filename, 'r') as f:
        n, m = f.readline().strip().split(' ')
        for i in range(int(n)):
            s, e = f.readline().strip().split(' ')
            heapq.heappush(data, (int(e), int(s)))
    return int(m), data

def Maximum_Activity(arr, n, m):
    e, s = heapq.heappop(arr)
    selected = [[] for i in range(m)]
    selected[0].append((s, e))
    while arr:
        e, s = heapq.heappop(arr)
        for i, selected_person in enumerate(selected):
            if selected_person==[] or selected_person[-1][1] <= s:
                selected[i].append((s, e))
                break
    print(sum(len(i) for i in selected))


def main():
    sys.stdout = open('task2_output.txt', 'w')
    m, arr = parse_data_from_file('task2_input.txt')
    Maximum_Activity(arr, len(arr), m)


if __name__=="__main__":
    main()