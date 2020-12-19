import csv 
from collections import Counter
#maam plz put the path of the height weight file according to your file location
with open("C:/Users/HOME/3D Objects/hv.csv",newline="") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range(len(filedata)):
    infiniteno=filedata[i][1]
    newdata.append(float(infiniteno))
calclength=len(newdata)
total=0
for x in newdata:
    total=total+x
mean=total/calclength
print(str(mean))

with open ("C:/Users/HOME/3D Objects/hv.csv",newline="") as medianfile:
    reader=csv.reader(medianfile)
    filedata = list(reader)
    filedata.pop(0)
    newdata = []
    for i in range (len(filedata)):
        lines=filedata[i][1]
        newdata.append(lines)
    n = len(newdata)
    newdata.sort()
    if n%2==0:
        median1=float(newdata[n//2])
        median2=float(newdata[n//2-1])
        median=(median2+median1)/2
    else:
         median=newdata[n//2]
    print("median is= "+str(median) )  

with open ("C:/Users/HOME/3D Objects/hv.csv",newline="") as filepath:
    read = csv.reader(filepath)
    data = list(read)
data.pop(0)
calculateddata=[]
for i in range (len(data)):
    line=data[i][1]
    calculateddata.append(line)
#caclutating the mode
datamode=Counter(calculateddata)
modedataforrange = {"50-60":0,"60-70":0,"70-80":0}
for height,occurence in datamode.items():
    if 50<float(height)<60:
        modedataforrange["50-60"]+=occurence
    elif 60<float(height)<70:
        modedataforrange["60-70"]+=occurence
    elif 70<float(height)<80:
        modedataforrange["70-80"]+=occurence
moderange,modeoccurence=0,0
for range,occurence in modedataforrange.items():
    if occurence>modeoccurence:
        moderange,modeoccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((moderange[0]+moderange[1])/2)
print(f"mode is->{mode:2f}")   
    
         
