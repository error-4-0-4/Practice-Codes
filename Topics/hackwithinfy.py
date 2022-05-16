# Print minimum subarray such that arr[i to j] gcd(arr[i],arr[j])>1 
def gcd (x,y):
    while(y):
        x,y=y,x%y
    return x

arr=[3,5,1,7,8,20,14,28,22,361]
dp=[0]*(len(arr)+1)
for i in range (len(arr)-1,-1,-1):
    m=dp[i+1]+1
    for j in range (i+1,len(arr)):
        if gcd(arr[i],arr[j])>1:
            m=min(m,1+dp[j+1])
    dp[i]=m
print(dp[0])

#NSER
arr=[2,3,1,2,4,2]
dis=[]
stack=[]
no_dis=[]
for i in range (len(arr)-1,-1,-1):
    while(len(stack) != 0 and stack[-1] >arr[i]):
        stack.pop()
    if len(stack) == 0 :
        dis.append(arr[i])
        no_dis.append(i)
    else:
        dis.append(arr[i]-stack[-1])
    stack.append(arr[i])

print(sum(dis))
print(sorted(no_dis))
