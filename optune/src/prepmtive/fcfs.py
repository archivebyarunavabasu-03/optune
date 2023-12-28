from typing import List
from pydantic import BaseModel
import pandas as pd

class Process(BaseModel):
    id: int
    arrival_time: float
    burst_time: float
    waiting_time: float = 0
    turnaround_time: float = 0

def fcfs(processes: List[Process]) -> pd.DataFrame:
    n = len(processes)

    processes.sort(key=lambda x: x.arrival_time)

    process_sequence = []
    processes[0].waiting_time = 0
    processes[0].turnaround_time = processes[0].burst_time
    process_sequence.append(processes[0].id)

    for i in range(1, n):
        processes[i].waiting_time = processes[i - 1].turnaround_time
        processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time
        process_sequence.append(processes[i].id)

    data = {
        'Process': [process.id for process in processes],
        'Arrival Time': [process.arrival_time for process in processes],
        'Burst Time': [process.burst_time for process in processes],
        'Waiting Time': [process.waiting_time for process in processes],
        'Turnaround Time': [process.turnaround_time for process in processes]
    }

    df = pd.DataFrame(data)

    average_waiting_time = df['Waiting Time'].mean()
    average_turnaround_time = df['Turnaround Time'].mean()

    print("Average Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)

    print("\nProcess Execution Sequence:", "->".join(map(str, process_sequence)))

    return df


if __name__ == "__main__":
    processes = [
        Process(id=1, arrival_time=10, burst_time=5),
        Process(id=2, arrival_time=2, burst_time=3),
        Process(id=3, arrival_time=5, burst_time=8),
        Process(id=4, arrival_time=9, burst_time=2)
    ]

    result_df = fcfs(processes)

    # Now you can access the DataFrame result for further analysis
    print(result_df)
    result_df.to_csv('fcfs_result.csv', index=False)