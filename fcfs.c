

#include <stdio.h>
#include<stdlib.h>

void main() {
    int n, i, j, PID[10], AT[10], BT[10], WT[10], TAT[10], CT[10]; //at-arrival time,bt-burst/execution time,ct completion time,wt-waiting time,tat-turn around time

    float avgWT, avgTAT;
  //tat=ct-at
  //wt=tat-bt
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    for (i=0;i<n;i++) {
        printf(" PID for process :%d\n ", i);
        PID[i]=i;
        printf("Enter AT : ");
        scanf("%d", &AT[i]);
        printf("Enter BT : " );
        scanf("%d", &BT[i]);
        printf("\n");
    }

    
    for (i=0;i<n-1;i++) {
        for (j = 0; j < n-i-1; j++) {
            if (AT[j] > AT[j+1]) {
                
                int temp = AT[j];
                AT[j] = AT[j+1];
                AT[j+1] = temp;

                
                temp = BT[j];
                BT[j] = BT[j+1];
                BT[j+1] = temp;

                
                temp = PID[j];
                PID[j] = PID[j+1];
                PID[j+1] = temp;
            }
            else if(AT[j] == AT[j+1] ){
            if(PID[j] > PID[j+1]){
            
             int temp = AT[j];
                AT[j] = AT[j+1];
                AT[j+1] = temp;

                
                temp = BT[j];
                BT[j] = BT[j+1];
                BT[j+1] = temp;

                
                temp = PID[j];
                PID[j] = PID[j+1];
                PID[j+1] = temp;
            
            }
            
          }}}
  
    CT[0] = AT[0] + BT[0];
    TAT[0] = CT[0] - AT[0];
    WT[0] = TAT[0] - BT[0];

    for (i = 1; i < n; i++) {
        if (CT[i-1] < AT[i]) {
            CT[i] = AT[i] + BT[i];
        } else {
            CT[i] = CT[i-1] + BT[i];
        }
        TAT[i] = CT[i] - AT[i];
        WT[i] = TAT[i] - BT[i];
    }
    
    printf("Computed table\n");
    
    printf("PID\tAT\tBT\tCT\tTAT\tWT\n");
    for (i = 0; i < n; i++) {
        printf("%d\t%d\t%d\t%d\t%d\t%d\n", PID[i], AT[i], BT[i], CT[i], TAT[i], WT[i]);
    }
printf("\n");
    
    for(i=0;i<n;i++)
    avgTAT+=TAT[i];
    avgTAT=avgTAT/n;
    
    
    for(i=0;i<n;i++)
    avgWT+=WT[i];
    avgWT=avgWT/n;
    
   
    printf("Average TAT: %.2f\n", avgTAT);
    printf("Average WT: %.2f\n", avgWT);
    
   
 }
