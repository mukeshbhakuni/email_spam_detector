
import functools as f

def laplace_smoothing():
    return 

def get_vocablary_size(spam,ham):
    lst=[x for j in spam for x in j]
    lst+=[x for j in ham for x in j]
    x=[]
    for i in lst:
        if i not in x:
            x+=[i]
    return len(x)

def count_(x,y):
    yy=[a for j in y for a in j]
    cnt=0
    for i in yy:
        if i==x:
            cnt+=1
    return cnt
    

def get_probability(x,y,k,voc_size):
    n=len([a for j in y for a in j])
    return (count_(x,y)+k)/float(n+k*voc_size)

def mul(a,b):
    return a*b
    
def solve1(y,lst,k,voc_size,pspam,pham,spam,ham):
    p=f.reduce(mul,map(lambda x:get_probability(x,spam,k,voc_size),lst))
    m=pspam*p
    p=f.reduce(mul,map(lambda x:get_probability(x,ham,k,voc_size),lst))
    n=pham*p
    if y=="SPAM":
        print float(m)/(m+n)
    else:
        print float(n)/(m+n)
    
def solve2(lst,y,k,voc_size,spam,ham):
    if y=="SPAM":
        y=spam
    else:
        y=ham
    l=map(lambda x:get_probability(x,y,k,voc_size),lst) 
    print f.reduce(mul,l)

spam=[["OFFER","IS","SECRET"],["CLICK","SECRET","LINK"],["SECRET","SPORTS","LINK"]]
ham=[["PLAY","SPORTS","TODAY"],["WENT","PLAY","SPORTS"],["SECRET","SPORTS","EVENTS"],["SPORTS","IS","TODAY"],["SPORTS","COSTS","MONEY"]]

voc_size=get_vocablary_size(spam,ham)
k=int(raw_input("Enter the value of k: "))

n=len(spam)
m=len(ham)

Pspam=(n+k)/float((n+m)+k*2)
Pham=(m+k)/float((n+m)+k*2)
x=raw_input("Enter the string like ((M/SPAM) or (SPAM/M)) or (SPAM) OR (HAM): ")

lst=x.split("/")
if(len(lst))==1:
    lst=filter(lambda x:x!=' ',lst[0])
    if lst=="SPAM":
        print Pspam
    elif lst=="HAM":
        print Pham
    else:
        print "Invalid Input"
else:
    lst[1]=filter(lambda x:x!='',lst[1].split(' '))
    lst[0]=filter(lambda x:x!='',lst[0].split(' '))
    if lst[0][0] in ['SPAM','HAM']:
        solve1(lst[0][0],lst[1],k,voc_size,Pspam,Pham,spam,ham)
    else:
        solve2(lst[0],lst[1][0],k,voc_size,spam,ham)
    
    




