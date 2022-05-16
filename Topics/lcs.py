# recursion plus memoization
# def lcs(s1,s2,m,n,dp):
    # if m==0 or n==0:
    #     return 0
    
    # if dp[m][n] != -1:
    #     return dp[m][n]

    # if s1[m-1] == s2[n-1]:
    #     dp[m][n] = 1+ lcs(s1,s2,m-1,n-1,dp)
    #     return dp[m][n]

    # dp[m][n] = max(lcs(s1,s2,m,n-1,dp),lcs(s1,s2,m-1,n,dp))
    # return dp[m][n]

# if __name__ == "__main__":
#     s1="cabac"
#     s2="eabcd"
#     m=len(s1)
#     n=len(s2)
#     dp=[[-1]*(m+1) for i in range (n+1)]
#     for i in range(m+1):
#         for j in range(n+1):
#             if i==0 or j ==0:
#                 dp[i][j]=0
#     ans=lcs(s1,s2,m,n)
#     print(ans)

# tabulation
def lcs(s1,s2,m,n):
    dp=[[0]* (n+1) for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]= max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

if __name__ == "__main__":
    s1="cabac"
    s2="eabcd"
    m=len(s1)
    n=len(s2)
    ans=lcs(s1,s2,m,n)
    print(ans)
    # 26- ans (alphabetical sharechat change m and n in dp)