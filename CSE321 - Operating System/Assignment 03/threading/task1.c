#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#include <pthread.h>


void* thread_function(void* arg)
{
    int i = *(int*) arg;
    printf("thread-%d running\n", i+1);
    
    pthread_exit(&i);
}


int main(void)
{

    pthread_t thread_id[5];

    for (int i = 0; i < 5; i++)
    {
        pthread_create(&thread_id[i], NULL, thread_function, &i);
        pthread_join(thread_id[i], NULL);
        printf("thread-%d closed\n", i+1);
    }

    return 0;
    
}