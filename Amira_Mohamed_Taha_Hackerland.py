def countDroppedRequests(server):
    numThreads=0
    droppedRequests=0

    for i in range(len(server)):
        if server[i] > 0:
            numThreads += server[i]
        elif server[i] == -1:
            if numThreads > 0:
                numThreads -= 1
            else:
                droppedRequests += 1
    return droppedRequests
server=[]
n=input("Enter number of servers: ")
for x in range (0,n):
          server.append(input("Enter Number: "))
print(server)
dropped = countDroppedRequests(server)
print(dropped)