import numpy as np

servetime = 90

f_read = open("C101.txt")
i = 0
returnMat = np.zeros((101,7),dtype = int)

for line in  f_read.readlines():
    i = i + 1
    demo = line.split()
    if i ==5:
        car_number = demo[0]
        car_Q = demo[1]
    if i > 9 and i < 111:        
        for j in range(7):
            returnMat[i-10][j] = demo[j]       
print(returnMat)
print(car_number,car_Q)

dataDict = {}
dataDict['NodeCoor'] = []
dataDict['Demand'] = []
dataDict['Timewindow'] = []
dataDict['MaxLoad'] = car_Q
dataDict['ServiceTime'] =  servetime

for i in range(101):
    dataDict['NodeCoor'].append((returnMat[i][1],returnMat[i][2])) 
print(dataDict['NodeCoor'])

for i in range(101):
    dataDict['Demand'].append(returnMat[i][3]) 
print(dataDict['Demand'])

for i in range(101):
    dataDict['Timewindow'].append((returnMat[i][4],returnMat[i][5])) 
print(dataDict['Timewindow'])
