class fcfs:
    process = []
    burstTime = []
    arrivalTime =[]


def getData(counter):
    data = fcfs();
    print 'Enter the data '
    data.process[counter] = counter;
    brstTime = input("Burst Time ?");
    data.bursTime[counter] = brstTime;
    arvalTime = input("Arrival Time ?");
    data.arrivalTime[counter] = arvalTime;

def find_min():
    for loop in range (len(data.arrivalTime)):
        if (len(data.arrivalTime) >= 0):
            mins = data.arrival_time[0]
            for i in range(len(data.arrival_time)):
                if (mins > data.arrivalTime [loop] ):
                    mins = data.arrivalTime[loop]
                    index = loop
               
    arrival_time[index] = 999999999;
    i_arr.append(index);
    if(mins == 999999999):
        i_arr.append(index);
        break;     
    

data = fcfs();
Processes = input("Total Processes of processes ?")
for loop in range(Processes):
    counter = loop;
    getData(loop);
    
avg = 0;
index = 0;
count = 0;
i_arr = [];
pbt = 0; 



for i in range(len(i_arr)):
    if(i == 0):
        avg = avg + ca[i];
        pbt = burst_time[i];
    if(i > 0):
        avg = avg + (pbt - ca[i])
        pbt = pbt + burst_time[i];
print 'The AVG time is ', avg/len(i_arr) ;
add = 0;
print 'Gantt chart ';
for i in range(len(i_arr)):
    print 'p',i_arr[i], ' .... ' , (burst_time[i_arr[i]]+ add )
    add = add +burst_time[i_arr[i]];
    