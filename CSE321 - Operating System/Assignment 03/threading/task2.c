#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#include <pthread.h>


struct thread_arg_struct
{
    int threadNumber;
    int printCounter;
};


void* thread_function(void* arg)
{
    struct thread_arg_struct *thread_arg = (struct thread_arg_struct*)arg;
    
    for (int i = 0; i < 5; i++)
    {
        printf("Thread %d prints %i\n", thread_arg->threadNumber, thread_arg->printCounter);
        thread_arg->printCounter++;
    }
    
    pthread_exit(&(thread_arg->threadNumber));
}


int main(void)
{

    pthread_t thread_id[5];

    struct thread_arg_struct thread_arg = {0, 1};

    for (int i = 0; i < 5; i++)
    {
        thread_arg.threadNumber = i;
        pthread_create(&thread_id[i], NULL, thread_function, (void *) &thread_arg);
        pthread_join(thread_id[i], NULL);
    }

    return 0;
    
}