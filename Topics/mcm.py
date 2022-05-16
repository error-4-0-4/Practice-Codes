# #memoization
# def rMCM(arr, i, j,dp):
#     #base case
#     if i==j:
#         dp[i][j]=0

#     if dp[i][j]!=-1:
#         return dp[i][j]

#     minimum=100000
#     for k in range (i, j):
#         count=rMCM(arr, i, k,dp) + rMCM(arr, k+1, j, dp)+ (arr[i-1]* arr[k]* arr[j])
#         if count<minimum:
#             minimum=count
#     dp[i][j]= minimum
#     return dp[i][j]

# def mcm(arr, n):
#     dp=[[-1]*n for i in range(n)]
#     return rMCM (arr, 1, n-1,dp)

# if __name__=='__main__':
#     arr=[2,3,4,3,5]
#     ans=mcm(arr, 5)
#     print(ans)


#tabulation
def rMCM(arr, i, j,dp):
    #base case
    if i==j:
        dp[i][j]=0

    if dp[i][j]!=-1:
        return dp[i][j]

    dp[i][j]=100000
    for k in range (i, j):
        dp[i][j]=min(dp[i][j], rMCM(arr, i, k,dp) + rMCM(arr, k+1, j, dp)+ (arr[i-1]* arr[k]* arr[j]))
        # if count<minimum:
        #     minimum=count
    # dp[i][j]= minimum
    return dp[i][j]

def mcm(arr, n):
    dp=[[-1]*n for i in range(n)]
    return rMCM (arr, 1, n-1,dp)

if __name__=='__main__':
    arr=[2,3,4,3,5]
    ans=mcm(arr, 5)
    print(ans)