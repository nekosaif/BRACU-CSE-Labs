#include<stdio.h>
#include<stdbool.h>


#define MAX_BURST_TIME 1000000


struct process {
    int pid;
    int arrival_time;
    int const_burst_time;
    int burst_time;
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
        printf("Enter process %d \"process_id arrival_time burst_time\": ", i + 1);
        scanf("%d %d %d", &processes[i].pid, &processes[i].arrival_time, &processes[i].burst_time);
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

        // get shortest burst time of running processes
        int shortest_burst_time = MAX_BURST_TIME;
        int shortest_burst_time_index = -1;
        for (int i = 0; i < n; i++) {
            if (is_running[i] && processes[i].burst_time < shortest_burst_time) {
                shortest_burst_time = processes[i].burst_time;
                shortest_burst_time_index = i;
            }
        }

        // run shortest burst time process
        if (shortest_burst_time_index != -1) {
            processes[shortest_burst_time_index].burst_time--;
            if (processes[shortest_burst_time_index].burst_time == 0) {
                is_running[shortest_burst_time_index] = false;
                is_completed[shortest_burst_time_index] = true;
                processes[shortest_burst_time_index].turnaround_time = processes[shortest_burst_time_index].waiting_time + processes[shortest_burst_time_index].const_burst_time;
            }
        }

        // calculate waiting time
        for (int i = 0; i < n; i++) {
            if (i != shortest_burst_time_index && is_running[i]) {
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