#include<stdio.h>
#include<stdbool.h>


#define MAX_BURST_TIME 1000000
#define LOWEST_PRIORITY 1000000


struct process {
    int pid;
    int arrival_time;
    int const_burst_time;
    int burst_time;
    int priority;
    int waiting_time;
    int turnaround_time;
};


int main() {

    int n;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    printf("\n");

    struct process processes[n];

    for (int i = 0; i < n; i++) {
        printf("Enter process %d \"process_id arrival_time burst_time priority\": ", i + 1);
        scanf("%d %d %d %d", &processes[i].pid, &processes[i].arrival_time, &processes[i].burst_time, &processes[i].priority);
        processes[i].const_burst_time = processes[i].burst_time;
        processes[i].waiting_time = 0;
        processes[i].turnaround_time = 0;
    }

    bool is_running[n];
    for (int i = 0; i < n; i++) {
        is_running[i] = false;
    }

    bool is_completed[n];
    for (int i = 0; i < n; i++) {
        is_completed[i] = false;
    }


    int time = 0;
    while(true)
    {
        //debug
        /*
        printf("Time: %d\n", time);
        for (int i = 0; i < n; i++) {
            printf("Process id: %d, burst time: %d, waiting time: %d, is running: %d, is completed: %d\n", processes[i].pid, processes[i].burst_time, processes[i].waiting_time, is_running[i], is_completed[i]);
        }
        printf("\n");
        */


        // check arrived processes
        for (int i = 0; i < n; i++) {
            if (!is_completed[i] && !is_running[i] && processes[i].arrival_time <= time) {
                is_running[i] = true;
            }
        }

        // get highest proirity of running processes
        int highest_priority = LOWEST_PRIORITY;
        int highest_priority_index = -1;
        for (int i = 0; i < n; i++) {
            if (is_running[i] && processes[i].priority < highest_priority) {
                highest_priority = processes[i].priority;
                highest_priority_index = i;
            }
        }

        // run shortest burst time process
        if (highest_priority_index != -1) {
            processes[highest_priority_index].burst_time--;
            if (processes[highest_priority_index].burst_time == 0) {
                is_running[highest_priority_index] = false;
                is_completed[highest_priority_index] = true;
                processes[highest_priority_index].turnaround_time = processes[highest_priority_index].waiting_time + processes[highest_priority_index].const_burst_time;
            }
        }

        // calculate waiting time
        for (int i = 0; i < n; i++) {
            if (i != highest_priority_index && is_running[i]) {
                processes[i].waiting_time++;
            }
        }

        // finished all processes
        for (int i = 0; i < n; i++) {
            if (!is_completed[i]) {
                goto not_finished;
            }
        }
        break;
        not_finished:
        time++;
        continue;
    }

    // print table
    for (int i = 0; i < n; i++) {
        printf("Process id: %d, Waiting time: %d, Turnaround time: %d\n", processes[i].pid, processes[i].waiting_time, processes[i].turnaround_time);
    }


    return 0;
}