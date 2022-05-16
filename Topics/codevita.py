# import math
# n=int(input())
# arr1=[]
# arr=[]
# a=0
# ans=[]
# for i in range (n):
#     x,y=map(int,input().split())
#     arr1.append([x,y])
# sides=1
# for ele in arr1:
#     if ele not in arr:
#         arr.append(ele)
# for i in range (len(arr)-1):
#     try:
#         a=arr[i+1][1]-arr[i][1]//arr[i+1][0]-arr[i][0]
#     except ZeroDivisionError:
#         a=0
#     ans.append(a)
# d={}
# count=0
# for ele in ans:
#     if ele in d:
#         d[ele]+=1
#     else:
#         d[ele]=1
# print(d)
# for i in d:
#     if d[i]%2==0:
#         count+=d[i]
# print(count)


# for i in range (n-1):
#     if arr[i][1]==arr[i+1][0]:
#         sides+=1
#     if arr[i+1][1]==arr[0][0]:
#         break
# if sides>=3:
#     print(sides,end="")
# else:
#     print(0,end="")

# from curses.ascii import isalpha


# seq=input()
# org=input()
# dict={}
# flag=1
# for i in range (len(seq)):
#     if seq[i]!="_":
#         seq[i].lower()
#         if seq[i] in dict:
#             flag=0
#             break
#         dict[seq[i]]=[]
#         dict[seq[i]].append(1)
#         dict[seq[i]].append(i)
# if flag==0:
#     print("New Language Error",end="")
# else:
#     empty=""
#     for i in range (len(org)):
#         org[i].lower()
#         if org[i] in seq:
#             if len(empty)==0:
#                 empty+=org[i]
#         else:
#             k=len(empty)-1
#             while (k>=0 and empty[k]!=" " and dict[empty[k]][1]>dict[org[i]][1]):
#                 k-=1
#             empty=empty[0:k+1]+org[i]+empty[k+1:len(empty)-k-1]
#         if org[i]==" ":
#             empty+=" "
#     print(empty,end="")

# seq=input()
# org=input()
# seq=seq.lower()
# org=org.lower()
# dict={}
# flag=1

# for i in range (len(seq)):
#   if seq[i]!=" ":
#     if seq[i] in dict:
#       flag=0
#       break
#     dict[seq[i]]=[]
#     dict[seq[i]].append(1)
#     dict[seq[i]].append(i)
# if flag==0:
#   print("New Language Error",end="")
# else:
#   empty=""
#   for i in range (len(org)):
#     if org[i] in dict:
#       if len(empty)==0:
#         empty+=org[i]
#       else:
#         k=len(empty)-1
#         while (k>=0 and empty[k]!=" " and dict[empty[k]][1]>dict[org[i]][1]):
#           k-=1
#         empty=empty[0:k+1]+org[i]+empty[k+1:len(empty)-k-1]
#     if org[i]==" ":
#       empty+=" "
#   print(empty,end="")


n=int(input())
flag=1e6
ans=-1
a1=True
a2=True
flag2=1e8
while n:
    s1, s2= map(int,input().split())
    if a1 and s2==flag2 and s1!=flag:
        ans+=1
        flag=s1
        flag2=s2
        a1=False
        a2=True
    elif a2 and s1==flag and s2!=flag2:
        ans+=1
        flag=s1
        flag2=s2
        a2=False
        a1=True
    
    elif s2!=flag2 and s1!=flag:
        ans+=1
        flag=s1
        flag2=s2
        a1=True
        a2=True
        
    else:
        flag=s1
        flag2=s2
    n-=1
print(ans+1,end="")



