
#include<stdio.h>
#include<stdlib.h>

int mutex=1, full=0, empty=3, x=0;

int wait (int s){
    return (--s);
}
int signal (int s){
    return (++s);
}
void producer(){
    mutex = wait(mutex); 
    empty = wait(empty); 
    x++;
    printf("\nProducer Produces an Item %d\n", x);
    mutex = signal(mutex); 
    full = signal(full);
}
void consumer(){
    mutex = wait(mutex); 
    full = wait(full);
    x--;
    printf("\nConsumer consumes an Item %d\n", x);
    mutex = signal(mutex); 
    empty = signal(empty);
}
void main(){
    int n;
    printf("1. Producer\n2. Consumer\n3. Exit");
    while (1){
    printf("\nEnter Your Choice : ");
   scanf("%d", &n);
        switch (n){
            case 1:
                if( (mutex==1) && (empty!=0))
                    producer();
                else
                    printf("Buffer is Full");
                break;

            case 2:
                if( (mutex==1) && (full!=0))
                    consumer();
                else
                    printf("Buffer is Empty");
                break;

            case 3: 
                exit(0);
        }
    }
}
