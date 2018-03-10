from math import sqrt

users = {"David": {"Imagine Dragons": 3, "Daft Punk": 5,
"Lorde": 4, "Fall Out Boy": 1},
"Matt": {"Imagine Dragons": 3, "Daft Punk": 4,
"Lorde": 4, "Fall Out Boy": 1},
"Ben": {"Kacey Musgraves": 4, "Imagine Dragons": 3,
"Lorde": 3, "Fall Out Boy": 1},
"Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,
"Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
"Tori": {"Kacey Musgraves": 5, "Imagine Dragons": 4,
"Daft Punk": 5, "Fall Out Boy": 3}}

def cosine_similarity(band1,band2):
    
    sum1=0
    sum2=0
    sum3=0
    average={}
    n=0

    for key in users:
        average[key]=float(sum(users[key].values()))/len(users[key].values())

    for key in users:
        normalised=[]
        for keys in users[key]:
            
            if keys==band1:
                n+=1
                x=users[key][keys]
                
            elif keys==band2:
                n+=1
                y=users[key][keys]
        
        if n==2:
            
            sum1+=float((x-average[key])*(y-average[key]))
            sum2+=float((x-average[key])**2)
            sum3+=float((y-average[key])**2)
            
        n=0       
        
    s=sum1/(sqrt(sum2)*sqrt(sum3))
    
    return s

    
bands=['Imagine Dragons','Daft Punk','Lorde','Fall Out Boy','Kacey Musgraves']

def Expected_Rating(user):
    
    a=[]
    
    for i in range(len(bands)-1):
        for j in range(i+1,len(bands)):
        
            x=cosine_similarity(bands[i],bands[j])
            a.append((bands[i],bands[j],x))

    normalised=[]
    bands2=[]
    bands2=bands
    n=0
    total=0
    similarity_total=0
    expected=[]
    
    for keys in users[user]:
        
        k=float(2*(users[user][keys]-1)-4)/4
        normalised.append((keys,k))
        n+=1
        bands2.remove(keys)

    print bands
    if n!=5:   
        for band in bands2:
            for j in range(len(a)):
                if a[j][0]==band or a[j][1]==band:
                    for k in range(len(normalised)):
                        if normalised[k][0]==a[j][1]:
                            total+=normalised[k][1]*a[j][2]
                            similarity_total+=abs(a[j][2])
                        elif normalised[k][0]==a[j][0]:
                            total+=normalised[k][1]*a[j][2]
                            similarity_total+=abs(a[j][2])

            normalised_predicted_rating=total/similarity_total

            actual_predicted_rating=((normalised_predicted_rating+1)*4)/2+1
            
            expected.append((band,actual_predicted_rating))
            
        return expected

print Expected_Rating('David')                                            
                


                
                
                
            
            
            
        
        
        
    
        
            
            
            
            
    
                       
    
   

        
    
