#include<stdio.h>
#include<stdbool.h>


struct process {
    int pid;
    int const_burst_time;
    int burst_time;
    int waiting_time;
    int turnaround_time;
};


int main() {

    int time_quantum;
    printf("Enter time quantum: ");
    scanf("%d", &time_quantum);
    printf("\n");

    int n;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    printf("\n");

    struct process processes[n];

    for (int i = 0; i < n; i++) {
        printf("Enter process id: ");
        scanf("%d", &processes[i].pid);
        printf("Enter burst time: ");
        scanf("%d", &processes[i].burst_time);
        processes[i].const_burst_time = processes[i].burst_time;
        processes[i].waiting_time = 0;
        processes[i].turnaround_time = 0;
    }

    bool is_running[n];
    for (int i = 0; i < n; i++) {
        is_running[i] = true;
    }

    bool is_completed[n];
    for (int i = 0; i < n; i++) {
        is_completed[i] = false;
    }


    int time = 0;
    int idx = 0;
    while(true)
    {
        // run process 
        if (!is_completed[idx] && is_running[idx]) {
            if (processes[idx].burst_time >= time_quantum)
            {
                processes[idx].burst_time -= time_quantum;
                time += time_quantum;
            } else {
                time += processes[idx].burst_time;
                processes[idx].burst_time -= processes[idx].burst_time;
            }
        }

        // check if any process is completed
        if (!is_completed[idx] && processes[idx].burst_time == 0) {
            is_running[idx] = false;
            is_completed[idx] = true;
            processes[idx].turnaround_time = time;
        }

        // increment index
        idx = (idx + 1) % n;

        // finished all processes
        for (int i = 0; i < n; i++) {
            if (!is_completed[i]) {
                goto not_finished;
            }
        }
        break;
        not_finished:
        continue;
    }

    // calculate waiting time
    for (int i = 0; i < n; i++) {
        processes[i].waiting_time = processes[i].turnaround_time - processes[i].const_burst_time;
    }

    // print table
    for (int i = 0; i < n; i++) {
        printf("Process id: %d, Waiting time: %d, Turnaround time: %d\n", processes[i].pid, processes[i].waiting_time, processes[i].turnaround_time);
    }


    return 0;
}