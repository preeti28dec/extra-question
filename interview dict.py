
user=input("enter any thing ")
i=0
c=1
dic={}
space=[]
while i<len(user):
    if user[i]==" ":
        key1 = "space"+str(c)
        dic[key1]=""
        c+=1
    else:
        dic[i]=user[i]
    i+=1
print(dic)

sum = 0
N = int(input("Enter a number: "))
temp_N = 100
while(N):
    k = 1
    fact = 1
    r = N % 10
while(k <= r):
    fact = fact * k
    k = k + 1
sum = sum + fact
N = N//10
if(sum == temp_N):
    print(str(temp_N) + " is a strong number")
else:
    print(str(temp_N) + " is not a strong number")