users = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
"Ben": {"Taylor Swift": 5, "PSY": 2},
"Clara": {"PSY": 3.5, "Whitney Houston": 4},
"Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}

def compute_deviation(artist1,artist2):
    
    dev=0
    n=0
    m=0
    for key in users:
        for keys in users[key]:
            
            if artist1==artist2:
                return 0,0
                
            else:
                if keys==artist1:
                    n+=1
                    x=users[key][keys]
                    
                if keys==artist2:
                    n+=1
                    y=users[key][keys]
                
        if n==2:
            dev+=float(x-y)/2
            m+=1
        n=0

    return dev,m
            
artists=['Taylor Swift','PSY','Whitney Houston']

def deviation_table():

    deviation=[]
    
    for i in range(len(artists)):
        for j in range(len(artists)):
            dev=compute_deviation(artists[i],artists[j])
            deviation.append((artists[i],artists[j],dev))

    return deviation

def Expected_Rating(user):

    expected=[]
    artists_unrated=[]
    
    for i in range(len(artists)):
        artists_unrated.append(artists[i])
            
    n=0
    x=deviation_table()
    
    for key in users[user]:
        artists_unrated.remove(key)
        n+=1

    total=0
    m=0
   
    for i in range(len(artists)-n):
        for key in users[user]:
            for j in range(len(artists)**2):
                if x[j][0]==artists_unrated[i] and x[j][1]==key:
                    total+=float(x[j][2][0]+users[user][key])*x[j][2][1]
                    m+=x[j][2][1]

        x=float(total/m)
        m=0
        expected.append((artists_unrated[i],x))

    return expected

print Expected_Rating('Daisy')

            


                

                
                    
                
                


            
    
       

            
            
