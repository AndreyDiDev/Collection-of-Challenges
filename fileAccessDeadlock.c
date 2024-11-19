#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

// Example of deadlock with simple 2 threads and 2 mutexes

pthread_mutex_t lock1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t lock2 = PTHREAD_MUTEX_INITIALIZER;

void *thread1(void *arg){
    // lock first mutex
    pthread_mutex_lock(&lock1);
    printf("Thread 1: Holding lock 1\n");

    // sleep for 1 second
    sleep(1);

    // lock second mutex
    pthread_mutex_lock(&lock2);
    printf("Thread 1: Holding lock 2\n");

    // unlock second mutex
    pthread_mutex_unlock(&lock2);
    printf("Thread 1: Unlocking lock 2\n");

    // unlock first mutex
    pthread_mutex_unlock(&lock1);
    printf("Thread 1: Unlocking lock 1\n");

    return NULL;
}

void *thread2(void *arg){
    // lock second mutex
    pthread_mutex_lock(&lock2);
    printf("Thread 2: Holding lock 2\n");

    // sleep for 1 second
    sleep(1);

    // lock first mutex
    pthread_mutex_lock(&lock1);
    printf("Thread 2: Holding lock 1\n");

    // unlock first mutex
    pthread_mutex_unlock(&lock1);
    printf("Thread 2: Unlocking lock 1\n");

    // unlock second mutex
    pthread_mutex_unlock(&lock2);
    printf("Thread 2: Unlocking lock 2\n");

    return NULL;
}


int main(){
    pthread_t th1, th2;

    pthread_create(&th1, NULL, thread1, NULL);
    pthread_create(&th2, NULL, thread2, NULL);

    pthread_join(th1, NULL);
    pthread_join(th2, NULL);

    return 0;
}