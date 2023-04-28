#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#include <string.h>
#include <pthread.h>


void* thread_function(void* arg);
void* thread_print_function(struct thread_arg_struct* arg[]);


struct thread_arg_struct
{
    int threadNumber;
    char name[20];
    int retASCIISum;
};


int main(void)
{
    int numberOfInputs = 3;

    pthread_t thread_id[numberOfInputs];
    struct thread_arg_struct thread_arg[numberOfInputs];

    for (int i = 0; i < numberOfInputs; i++)
    {
        thread_arg[i].threadNumber = i;
        thread_arg[i].retASCIISum = 0;
        printf("Enter name %d: ", i+1);
        scanf("%s", thread_arg[i].name);
        pthread_create(&thread_id[i], NULL, thread_function, (void *) &thread_arg[i]);
    }

    for (int i = 0; i < numberOfInputs; i++)
    {
        pthread_join(thread_id[i], NULL);
    }
    
    pthread_create(&thread_id, NULL, thread_print_function, (void *) &thread_arg);
    pthread_join(thread_id, NULL);

    return 0;
    
}


void* thread_function(void* arg)
{
    struct thread_arg_struct *thread_arg = (struct thread_arg_struct*)arg;
    
    for (int i = 0; i < strlen(thread_arg->name); i++)
    {
        thread_arg->retASCIISum = thread_arg->retASCIISum + thread_arg->name[i];
    }
    
    pthread_exit(&(thread_arg->threadNumber));
}


void* thread_print_function(struct thread_arg_struct *arg[])
{
    int sizeof_thread_arg_struct = 4;

    int sum1 = arg[0]->retASCIISum;
    int sum2 = arg[1]->retASCIISum;
    int sum3 = arg[2]->retASCIISum; 
    
    if (sum1 == sum2 && sum2 == sum3)
    {
        printf("Youreka\n");
    }
    else if (sum1 == sum2 || sum2 == sum3 || sum1 == sum3)
    {
        printf("Miracle\n");
    }
    else
    {
        printf("Hasta la vista\n");
    }
    
    pthread_exit(&sizeof_thread_arg_struct);
}