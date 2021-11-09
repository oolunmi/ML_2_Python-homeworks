logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = int(input())
output=[]
for i in range(k):
    output.append(0)

def UAM_calculator(logs,k):
    output=[]
    for i in range(k):
        output.append(0)
    dict = {}
    for i, j in logs:
        if i not in dict:
            dict[i]=[j]
        elif i in dict and j not in dict[i]:
            dict[i].append(j)
    for key, value in dict.items():
        output[len(value)-1]+=1
    
    print(output)

UAM_calculator(logs,k)

     
        
