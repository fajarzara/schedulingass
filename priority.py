class fcfs:
    process = []
    burstTime = []
    arrivalTime = []
    pr = []
    def __init__(self):
        process = []
        burstTime = []
        arrivalTime = []
        pr = []

def getData(counter):
    data = fcfs();
    i = 0;
    print 'Enter the data '
    data.process.append(counter);
    brstTime = input("Burst Time ?");
    data.burstTime.append(brstTime);
    arvalTime = input("Arrival Time ?");
    data.arrivalTime.append(arvalTime);
    prr = input("Priority ?");
    data.pr.append(prr);
    return;

data = fcfs();
Processes = input("Total Processes of processes ?")
start = 0;

for loop in range(Processes):
    counter = 0;
    getData(counter);
    counter += 1;
print 'GANTT CHART IS '
for i in range(len(data.pr)):
    mins = min(data.pr);
    index = data.pr.index(min(data.pr))

    print start , '------' , data.burstTime[index]+start;
    start = start + data.burstTime[index];
    data.pr.remove(mins);
    data.burstTime.remove(data.burstTime[index]);