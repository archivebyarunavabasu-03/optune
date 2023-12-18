


def fcfs(processes):
    n = len(processes)

    '''
    it going to take the arrival time as argument and sort them  
    '''
    processes.sort(key=lambda x: x[1]) 
    waiting_time = [0] * n
    turnaround_time = [0] * n


    process_sequence = []
    waiting_time[0] = 0
    turnaround_time[0] = processes[0][2]  
    process_sequence.append(processes[0][0])

    for i in range(1, n):
        waiting_time[i] = turnaround_time[i - 1]
        turnaround_time[i] = waiting_time[i] + processes[i][2]
        process_sequence.append(processes[i][0])


    average_waiting_time = sum(waiting_time) / n
    average_turnaround_time = sum(turnaround_time) / n


    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        process_id, arrival_time, burst_time = processes[i]
        print(f"{process_id}\t\t{arrival_time}\t\t{burst_time}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")
    

    print("\nProcess Execution Sequence:", "->".join(map(str, process_sequence)))


if __name__ == "__main__":

    processes = [
        (1, 10, 5),
        (2, 2, 3),
        (3, 5, 8),
        (4, 9, 2)
    ]

    fcfs(processes)
