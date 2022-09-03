import sys


def parse_data_from_file(filename, ret = None):
    with open(filename, 'r') as f:
        ret = f.read().strip().split('\n')
    return ret


def LCS(X, Y, Z):
    m, n, o = len(X)+1, len(Y)+1, len(Z)+1
    c = [[([None]*(o)) for _ in range(n)] for _ in range(m)]
    
    for i in range(0, m):
        for j in range(0, n):
            for k in range(0, o):
                if i == 0 or j == 0 or k == 0:
                    c[i][j][k] = 0
                else:
                    if X[i-1] == Y[j-1] == Z[k-1]:
                        c[i][j][k] = 1 + c[i-1][j-1][k-1]
                    else:
                        if c[i-1][j][k] >= c[i][j-1][k]:
                            maximum = c[i-1][j][k]
                            if maximum >= c[i][j][k-1]:
                                c[i][j][k] = maximum
                            else:
                                maximum = c[i][j][k-1]
                                c[i][j][k] = maximum
    
                        else:
                            maximum = c[i][j-1][k]
                            if maximum >= c[i][j][k-1]:
                                c[i][j][k] = maximum
                            else:
                                maximum = c[i][j][k-1]
                                c[i][j][k] = maximum
    return c[m-1][n-1][o-1] 
    

def tester():
    sys.stdout = open('output2.txt', 'w')
    string1, string2, string3 = parse_data_from_file('input2.txt', 'r')
    print(LCS(string1, string2, string3))


def main():
    tester()


if __name__=="__main__":
    main()
