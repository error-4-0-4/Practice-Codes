# def largestRectangleArea(heights,dim):
#     s=[]
#     total=0
#     for i in heights:
#         total+=i*dim[0]*dim[1]
#     m=0
#     rstack,lstack=[],[]
#     r,l=[0]*len(heights),[0]*len(heights)
#     for i in range(len(heights)-1,-1,-1):
#         while rstack and rstack[-1][0]>=heights[i]:
#             rstack.pop()
#         if rstack:
#             r[i]=rstack[-1][1]
#         else:
#             r[i]=len(heights)
#         rstack.append([heights[i],i])
        
#     for i in range(len(heights)):
#         while lstack and lstack[-1][0]>=heights[i]:
#             lstack.pop()
#         if lstack:
#             l[i]=lstack[-1][1]
#         else:
#             l[i]=-1
#         lstack.append([heights[i],i])
#     for i in range(len(heights)):
#         m=max(m,(r[i]-l[i]-1)*heights[i]*dim[0]*dim[1])
#     print((total-(m))%((10**9)+7),end='')

# n=int(input())
# heights=list(map(int,input().split()))
# l=list(map(int,input().split()))
# largestRectangleArea(l,heights)

 
