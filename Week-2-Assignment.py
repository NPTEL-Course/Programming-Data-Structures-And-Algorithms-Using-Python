def primeproduct(m):
    l=[]    
    if m>=2:
        for i in range(2,m):
            if m%i==0:                
                l+=[i]            
        if len(l)==2:
            if m==l[0]*l[1]:
                if l[1]%l[0]==0:
                    return False
                return True
        elif len(l)==1:
            if m==l[0]*l[0]:
                return True
        else:
            return False     
    else:
        return False

def delchar(s,c):
    if len(c)==1:
        s=s.replace(c,'')  
        return (s)
    else:
        return (s)
        
def shuffle(l1,l2):
    c=[]
    if len(l1)!=0 and len(l2)!=0:
      for i in range(min(len(l1), len(l2))):
        c.extend([l1[i],l2[i]])      
      c.extend(l1[i+1:] or l2[i+1:])
    else:
      c.extend(l1[0:] or l2[0:])      
    return (c)
