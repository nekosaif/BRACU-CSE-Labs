#include <stdio.h>
#include <stdbool.h>


bool isPerfectNumber(int num);


int main()
{

    int start, end;
    scanf("%d %d", &start, &end);


    for (int i = start; i <= end; i++)
    {
        if (isPerfectNumber(i))
        {
            printf("%d\n", i);
        }
    }


    return 0;

}


bool isPerfectNumber(int num)
{
    int sum = 0;

    for(int i = 1; i < num; i++)
    {
        if(num % i == 0)
        {
            sum += i;
        }
    }

    if(sum == num)
        return true;
    return false;
}