import sys


def parse_data_from_file(filename, ret = None):
    with open(filename, 'r') as f:
        ret = f.read().strip().split('\n')
    return ret


def print_3d_array(A):
    for i in range(len(A)):
        print("Student: ",(i+1))
        for j in range(len(A[i])):
            print("Course: ",(j+1))
            print("Marks of Mid and Final: ")
            for k in range(len(A[i][j])):
                print(A[i][j][k],end=" ")
            print()
        print()
    

def tester():
    sys.stdout = open('output3.txt', 'w')
    A=[[[30, 25],
        [35, 40],
        [41, 45],
        [26, 26]],
       [[41, 45],
        [43, 47],
        [49, 44],
        [46, 47]],
       [[10, 15],
        [35, 20],
        [11, 17],
        [29, 16]]]
    print_3d_array(A)


def main():
    tester()


if __name__=="__main__":
    main()
