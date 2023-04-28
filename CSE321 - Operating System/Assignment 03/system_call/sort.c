#include <stdio.h>
#include <stdlib.h>


int* sort(int* numbers, int size);
int* print_array(int* numbers, int size);


int main( int argc, char *argv[] )  {

    int numbers[argc];

    //printf("%s", *argv);

    for (int i = 1; i < argc; i++)
    {
        numbers[i] = atoi(argv[i]);
    }

    print_array(sort(numbers, argc), argc);

    return 0;
}


int* sort(int* numbers, int size)
{
    int temp;
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            if (numbers[i] < numbers[j])
            {
                temp = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = temp;
            }
        }
    }
    return numbers;
}


int* print_array(int* numbers, int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", numbers[i]);
    }
    printf("\n");
    return numbers;
}