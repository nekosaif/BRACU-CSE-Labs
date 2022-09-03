import sys


def parse_data_from_file(filename, ret = None):
    with open(filename, 'r') as f:
        ret = f.read().strip().split('\n')
    return ret


def LCS(X, Y):
    m, n = len(X)+1, len(Y)+1
    c = [([(0, None)]*(n) if i == 0 else ([(0, None)]+([(None, None)]*(n-1)))) for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1][0] + 1, 0
            elif c[i-1][j][0] >= c[i][j-1][0]:
                c[i][j] = c[i-1][j][0], 1
            else:
                c[i][j] = c[i][j-1][0], -1
                
    i, j, s = m-1, n-1, ''
    while not (i == 0 and j == 0):
        if X[j-1] == Y[i-1]:
            s = X[j-1] + s
        if c[i][j][1] == 0:
            i, j = i-1, j-1
        elif c[i][j][1] == 1:
            i = i-1
        elif c[i][j][1] == -1:
            j = j-1
    return c[-1][-1][0], s
    

def tester():
    sys.stdout = open('output1.txt', 'w')
    n, string1, string2 = parse_data_from_file('input1.txt', 'r')
    zone_names = {'Y': 'Yasnaya',
                  'R': 'Rozhok',
                  'S': 'School',
                  'P': 'Pochinki',
                  'F': 'Farm',
                  'M': 'Mylta',
                  'H': 'Shelter',
                  'I': 'Prison'}
    n_match, s_match = LCS(string1, string2)
    print(' '.join([zone_names[c] for c in s_match]))
    print(f'Correctness of prediction: {int(n_match/int(n)*100)}%')


def main():
    tester()


if __name__=="__main__":
    main()
