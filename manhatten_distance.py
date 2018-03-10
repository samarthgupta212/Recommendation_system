from math import sqrt
import codecs

'''users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
 "Slightly Stoopid": 1.5,
 "The Strokes": 2.5, "Vampire Weekend": 2.0},

 "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5,
 "Deadmau5": 4.0, "Phoenix": 2.0,
 "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
 "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0,
 "Deadmau5": 1.0, "Norah Jones": 3.0,
 "Phoenix": 5, "Slightly Stoopid": 1.0},
 "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,
 "Deadmau5": 4.5, "Phoenix": 3.0,
 "Slightly Stoopid": 4.5, "The Strokes": 4.0,
 "Vampire Weekend": 2.0},
 "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0,
 "Norah Jones": 4.0, "The Strokes": 4.0,
 "Vampire Weekend": 1.0},
 "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
 "Phoenix": 5.0, "Slightly Stoopid": 4.5,
 "The Strokes": 4.0, "Vampire Weekend": 4.0},
 "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0,
 "Norah Jones": 3.0, "Phoenix": 5.0,
 "Slightly Stoopid": 4.0, "The Strokes": 5.0},
 "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
 "Phoenix": 4.0, "Slightly Stoopid": 2.5,
 "The Strokes": 3.0}}'''

data={}
productid2name={}
user2idname={}
username2id={}
def Book_Load():
    
    i=0
    f=codecs.open('C:\BX-Book-Ratings.csv','r')
    
    for line in f:
        i+=1
        fields=line.split(';')
        user=fields[0].strip('"')
        book=fields[1].strip('"')
        ratings=(fields[2].strip().strip('"'))
        if user in data:
            currentRatings=data[user]
        else:
            currentRatings={}
            
        currentRatings[book]=ratings
        data[user]=currentRatings

    f.close()
    f=codecs.open('C:\BX-Books.csv','r')
    
    for line in f:
        
        i += 1
        fields = line.split(';')
        isbn = fields[0].strip('"')
        title = fields[1].strip('"')
        author = fields[2].strip().strip('"')
        title = title + ' by ' + author
        productid2name[isbn] = title

    f.close()
    
    '''f=codecs.open('C:/Users/Samarth Gupta/Downloads/BX-Users.csv','r')
   
    for line in f:
    i+=1
    fields=line.split(';')
    userid=fields[0].strip('"')
    location=fields[1].strip('"')
    age=fields[2].strip().strip('"')
    if age!='NULL':
        value=location + 'age:',age

    userid2name[userid]=value
    username2id[location]=userid   
    f.close()'''


def Manhatten_distance(user1,user2):
    
    distance=0
    for key in users[user1]:
        if key in users[user2]:
            distance+=abs(users[user1][key]-users[user2][key])

    return distance

def pearson(user1,user2):    
    
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    
    for user in data[user1]: 
        
        if user in data[user2]:
            
            n+=1
            x=int(data[user1][user])
            y=int(data[user2][user])
            sum_x=x+sum_x
            sum_y=y+sum_y
            sum_x2=x**2+sum_x2
            sum_y2=y**2+sum_y2
            sum_xy=x*y+sum_xy
            

    if n==0:
        return 0
    
    denominator = sqrt(sum_x2 - (sum_x**2) / n) *sqrt(sum_y2 - (sum_y**2) / n)
    if denominator==0:
        return 0
    
    r=(sum_xy-(sum_x*sum_y)/n)/denominator

    return r

def Nearest_Neighbour(username):
    
    distance=[]
    for user in data:
        if user!=username:
            d=pearson(user,username)
            distance.append((d,user))

    distance.sort(reverse=True)
    return distance

def Recommend(username):
     
    neighbour=Nearest_Neighbour(username)
    print neighbour[0][1]
    recommended=[]
    for i in data[neighbour[0][1]]:
        if i not in data[username]:
            if i in productid2name:
               
                recommended.append((productid2name[i],data[neighbour[0][1]][i]))
                
    recommended.sort(key=lambda artistTuple: artistTuple[1],
                            reverse = True)
    return recommended[:5]   

Book_Load()
print Recommend('132375')
            
            
    
   

        
    


    

        
            
                
                
    
                
    
            

