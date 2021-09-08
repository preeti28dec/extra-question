old_dict = {'one':1,'two':2,'three':3,'four':4} 
i=0
k=[]
v=[]
while i<=len(old_dict):
    k=old_dict.keys()
    v=old_dict.values()
    d=dict(zip(v,k))
    i+=1
print(d)

a = {'one':1,'two':2,'three':3,'four':4} 
a.pop('four')
a.pop('three')
print(a)