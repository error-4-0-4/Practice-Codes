#budget_hiring

def knapsack(W, wt, val, n):
    dp = [[0 for j in range(W + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if(i == 0 or j == 0):
                dp[i][j] = 0
            elif wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], val[i - 1] + dp[i - 1][j - wt[i - 1]])
    return dp[n][W]


def dfs(emp, visited,graph, temp):
    temp.append(emp)
    visited[emp] = True
    for dost in graph[emp]:
        if visited[dost] is not True:
            dfs(dost, visited,graph, temp)
    return temp

def budget_hiring (n,emp_details, groups, b):
    graph={}
    visited=[False]* (n+1)
    groupwise_list=[]

    for emp in range(1,n+1):
        graph[emp] = graph.get(emp,list())

    for group in groups:
        u = group[0]
        v= group[1]
        graph[u].append(v)
        graph[v].append(u)

    for emp in range (1,n+1):
        if visited[emp] is not True:
            temp=[]
            groupwise_list.append(dfs(emp, visited , graph, temp))

    num= len (groupwise_list)
    skills=[0]*num
    salaries=[0]*num
    for i in range(num):
        for emp_no in groupwise_list[i]:
            details= emp_details[emp_no-1]
            skills[i] += details[0]
            salaries[i] += details[1]

    ans= knapsack(b, salaries,skills, num )
    return ans

    # skills= [[], [], []]   val 
    # salaries= [[],[], []]  wt 
    # b                      c

if __name__=="__main__":
    n=7
    q=4
    b=41
    emp_details=[[12,7], [11,6],[12,6], [15,11], [20,20], [21,16], [23,14]]
    groups=[[1,2], [2,3], [2,5], [4,6]]

    ans= budget_hiring(n,emp_details, groups,b)
    print(ans)