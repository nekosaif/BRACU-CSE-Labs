#include <stdio.h>
#include <stdbool.h>
#include <string.h>


const int MAX_STR_SIZE = 256;


void task_2_a();
void task_2_b();
void task_2_c();
void remove_extra_space(char *str);
void check_password(char *str);


int main()
{

    task_2_c();

    return 0;
}


void task_2_a()
{
    int a, b;
    char o;

    printf("Enter number, 'a': ");
    scanf("%d", &a);
    printf("Enter number, 'b': ");
    scanf("%d", &b);

    printf("Enter operator, o: ");
    scanf(" %c", &o);

    if (a > b)
    {
        printf("a + b = %d", a + b);
    }
    else if (a < b)
    {
        printf("a - b = %d", a - b);
    }
    else
    {
        printf("a * b = %d", a * b);
    }
}


void task_2_b()
{
    char str[MAX_STR_SIZE];
    scanf("%[^\n]s",str);

    remove_extra_space(str);
    
	printf("%s", str);
}


void task_2_c()
{
    char str[MAX_STR_SIZE];

    printf("Enter password: ");
    scanf("%[^\n]s",str);

    check_password(str);
}


void remove_extra_space(char *str)
{
    int i, j;
    for (i = 0; i < strlen(str); i++)
    {
        if (str[i] == ' ' && str[i + 1] == ' ')
        {
            for (j = i; j < strlen(str); j++)
            {
                str[j] = str[j + 1];
            }
            i--;
        }
    }
}


int addition(int a, int b)
{
    return a + b;
}

int subtraction(int a, int b)
{
    return a - b;
}

int multiplication(int a, int b)
{
    return a * b;
}


void check_password(char *password)
{
    bool lowerFlag = false, upperFlag = false, digitFlag = false, specialFlag = false;
    for (int i = 0; i < strlen(password); i++)
    {
        if (password[i] >= 'a' && password[i] <= 'z')
        {
            lowerFlag = true;
        }
        else if (password[i] >= 'A' && password[i] <= 'Z')
        {
            upperFlag = true;
        }
        else if (password[i] >= '0' && password[i] <= '9')
        {
            digitFlag = true;
        }
        else
        {
            specialFlag = true;
        }
    }

    if (lowerFlag && upperFlag && digitFlag && specialFlag)
    {
        printf("OK");
    }
    else
    {
        if (!lowerFlag)
        {
            printf("Lowercase Missing");
        }
        if (!upperFlag)
        {
            if (!lowerFlag)
            {
                printf(", ");
            }
            printf("Uppercase Missing");
        }
        if (!digitFlag)
        {
            if (!upperFlag)
            {
                printf(", ");
            }
            printf("Digit Missing");
        }
        if (!specialFlag)
        {
            if (!digitFlag)
            {
                printf(", ");
            }
            printf("Special Missing");
        }
    }
}