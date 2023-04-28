#include <stdio.h>
#include <unistd.h>




int main()
{

    pid_t parent, child, grandchild;
    parent = getpid();
    fork();
    child = getpid();

    if (child != parent)
    {
        printf("I am the parent\n");
    }
    else
    {
        fork();
        grandchild = getpid();

        if (child != grandchild)
        {
            printf("I am the child\n");
        }
        else
        {
            printf("I am the grandchild\n");
        }
    }
    


    return 0;

}