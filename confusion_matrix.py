# Copy specified test and data file to C:/ drive 
data=[]
mpg=[]
cylinder=[]
ci=[]
hp=[]
weight=[]
time=[]

def manhatten_distance(a,b,c,d,e):
    
    nearest_neighbour=[]
    for key in range(len(data)):
        distance=abs(data[key][1]-a)+abs(data[key][2]-b)+abs(data[key][3]-c)+abs(data[key][4]-d)+abs(data[key][5]-e)
        nearest_neighbour.append((distance,data[key][0]))

    nearest_neighbour.sort()
    return nearest_neighbour[0][1]

def get_median(array):
    
    if len(array)%2!=0:
        
        return array[len(array)/2]
    
    else:
        
        x=(len(array)/2)-1
        y=(len(array)/2)
        
        return float(float(array[x])+float(array[y]))/2

def standard_deviation(u,array):
    
    sum1=0
    
    for item in array:
        
        sum1+=abs(float(item)-int(u))

    return float(sum1/len(array))

filename='C:/mpgdata.txt'
f=open(filename,'r')
line=f.readline()
    
while line!='':
    
    fields=line.split()
    cylinder.append(fields[1])    
    ci.append(fields[2])   
    hp.append(fields[3])
    weight_int=fields[4].split('.')
    weight.append(weight_int[0])
    time.append(fields[5])
    data.append(fields)
    line=f.readline()

f.close()
cylinder.sort()
ci.sort()
hp.sort()
weight.sort()
time.sort()

cylinder_median=get_median(cylinder)
hp_median=get_median(hp)
ci_median=get_median(ci)
weight_median=get_median(weight)
time_median=get_median(time)

cylinder_deviation=standard_deviation(get_median(cylinder),cylinder)
ci_deviation=standard_deviation(get_median(ci),ci)
hp_deviation=standard_deviation(get_median(hp),hp)
weight_deviation=standard_deviation(get_median(weight),weight)
time_deviation=standard_deviation(get_median(time),time)

for i in range(len(data)):
    
    data[i][1]=(float(data[i][1])-get_median(cylinder))/cylinder_deviation
    data[i][2]=(float(data[i][2])-get_median(ci))/ci_deviation
    data[i][3]=(float(data[i][3])-get_median(hp))/hp_deviation
    data[i][4]=(float(data[i][4])-get_median(weight))/weight_deviation
    data[i][5]=(float(data[i][5])-get_median(time))/time_deviation

def test():
  
    filename='C:/mpgtest.txt'
    f=open(filename,'r')
    line=f.readline()
    predicted_mpg=[]
    m=0
    n=0
    while line!='':
        fields=line.split()
        cylinder_test=(float(fields[1])-cylinder_median)/cylinder_deviation
        hp_test=(float(fields[3])-hp_median)/hp_deviation
        ci_test=(float(fields[2])-ci_median)/ci_deviation
        weight_test=(float(fields[4])-hp_median)/weight_deviation
        time_test=(float(fields[5])-time_median)/time_deviation
        n+=1
        x=manhatten_distance(cylinder_test,ci_test,hp_test,weight_test,time_test)
        y=float(x)//5
        if float(x)-(5*y)<=2:
            x=5*y
        else:
            x=5*y+5

        predicted_mpg.append((fields[0],x))
        line=f.readline()

print test()
        
    
    

    



