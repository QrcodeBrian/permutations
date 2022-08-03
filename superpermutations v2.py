from itertools import permutations
lists=["1","2","3","4","5"]
arangements1 = ["".join(p) for p in permutations(["1"]+lists)]

print(len(arangements1))

def lastn(x,n):
	return x[-n:-1] + x[-1]

def smallest(x):
    small=x[1]
    for y in x:
        if y<small:
            small = y
    return small

def twist(perm,x,remstart):
    x=str(x)
    a=perm + perm
    rep = a[a.find(x):a.find(x)+len(lists)+1]
    extra = rep[0:4]
    rep+=extra
    return rep[remstart:-1]+rep[-1]
    


def loop(current,start, arangements):
    permend = current + start
    if start=="":
        permend += arangements[0]
    while len(arangements)>0:
        set4 = []
        for x in arangements:
            if lastn(permend,4) in x:
                set4.append(x)
        if len(set4)==1:
            permend+= twist(set4[0],lastn(permend,4)[0],4)
            arangements.remove(set4[0])
            set4=[]
            continue
        elif len(set4)>1:
            smallest = 10000000000000000000000000000000000000000000000000000000
            perms = ""
            for x in set4:
                copy = list(arangements)
                try:
                    copy.remove(x)
                except:
                    continue
                size,perm = loop(permend,twist(x,lastn(permend,4)[0],4),copy)
                if size<smallest:
                    smallest = size
                    perms = perm
            return smallest,perm
        set3 = []
        for x in arangements:
            if lastn(permend,3) in x:
                set3.append(x)
        if len(set3)==1:
            permend+= twist(set3[0],lastn(permend,3)[0],3)
            arangements.remove(set3[0])
            set3=[]
            continue
        elif len(set3)>1:
            smallest = 10000000000000000000000000000000000000000000000000000000
            perms = ""
            for x in set3:
                copy = list(arangements)
                try:
                    copy.remove(x)
                except:
                    continue
                size,perm = loop(permend,twist(x,lastn(permend,3)[0],3),copy)
                if size<smallest:
                    smallest = size
                    perms = perm
            return smallest,perm
        set2 = []
        for x in arangements:
            if lastn(permend,2) in x:
                set2.append(x)
        if len(set2)==1:
            permend+=twist(set2[0],lastn(permend,2)[0],2)
            arangements.remove(set2[0])
            set2=[]
            continue
        elif len(set2)>1:
            smallest = 10000000000000000000000000000000000000000000000000000000
            perms = ""
            for x in set2:
                copy = list(arangements)
                try:
                    copy.remove(x)
                except:
                    continue
                size,perm = loop(permend,twist(x,lastn(permend,2)[0],2),copy)
                if size<smallest:
                    smallest = size
                    perms = perm
            return smallest,perm
        set1 = []
        for x in arangements:
            if lastn(permend,1) in x:
                set1.append(x)
        if len(set1)==1:
            permend+= twist(set1[0],lastn(permend,1)[0],1)
            arangements.remove(set1[0])
            set1=[]
            continue
        elif len(set1)>1:
            smallest = 10000000000000000000000000000000000000000000000000000000
            perms = ""
            for x in set1:
                copy = list(arangements)
                try:
                    copy.remove(x)
                except:
                    continue
                size,perm = loop(permend,twist(x,lastn(permend,1)[0],1),copy)
                if size<smallest:
                    smallest = size
                    perms = perm
            return smallest,perm
    return len(permend),permend
                
    
#print(loop("","",arangements1))
    
