#include <stdio.h>
#include <unistd.h>


int main()
{

    int n = 4;
    pid_t root = getpid();

    pid_t a, b, c;
    a = fork();
    b = fork();
    c = fork();

    if (a&2 != 0 || b&2 != 0 || c&2 != 0)
    {
        fork();
        ++n;
    }
    
    if (root == getpid())
    {
        printf("Total Processes = %d\n", n);
    }

    return 0;

}