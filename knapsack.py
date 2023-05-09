# import the time module
import time
import matplotlib.pyplot as plt
  
  
def knapSack(W, wt, val, n):
    
    # Base Case
    if n == 0 or W == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
 
# end of function knapSack
 
def memoized_knapsack(W, wt, val, n):

    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
 
    # choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + memoized_knapsack(W-wt[n-1],wt, val, n-1),
            memoized_knapsack(W, wt, val, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = memoized_knapsack(W, wt, val, n-1)
        return t[n][W]


def knapSack_dynamic(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                                + K[i-1][w-wt[i-1]],
                                K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


def knapSack_dynamic_optimised(W, wt, val, n):
     
    # Making the dp array
    dp = [0 for i in range(W+1)]
 
    # Taking first i elements
    for i in range(1, n+1):
       
        # Starting from back,
        # so that we also have data of
        # previous computation when taking i-1 items
        for w in range(W, 0, -1):
            if wt[i-1] <= w:
                 
                # Finding the maximum value
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
     
    # Returning the maximum value of knapsack
    return dp[W]

def make_data(name):
    
    f = open(name, "r")
    a = f.readline().splitlines()
    length = int(a[0])
    P = []
    W = []
    for i in range(int(a[0])):
        a = f.readline().splitlines()
        z = a[0].split(' ')
        P.append(int(z[1]))
        W.append(int(z[2]))
    a = f.readline().splitlines()
    return P,W,int(a[0]),length
 
# Driver Code
if __name__ == '__main__':

    N = []
    R = []
    D = []
    M = []
    for i in range(5):
        fname = f'tests/test{i}.txt'
        a = make_data(fname)
        profit = a[0]
        weight = a[1]
        
        W = a[2]
        N.append(a[3]) #length of problem
        n = len(profit)

        t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
        seconds1 = time.time()    
        print(memoized_knapsack(W, weight, profit, n))    # Dynamic Knapsack code implementation from geeksforgeeks
        seconds2 = time.time()
        M.append(seconds2 - seconds1)

        seconds1 = time.time()    
        print(knapSack_dynamic_optimised(W, weight, profit, n))    # Dynamic Knapsack code implementation from geeksforgeeks
        seconds2 = time.time()
        D.append(seconds2 - seconds1)
        

    # create data
    
    
    # plt.plot(N, R, label = "Recursion")
    plt.plot(N, D, label = "Dynamic")
    plt.plot(N, M, label = "Memoized")
    plt.xlabel("Problem Length")
    plt.ylabel("Time in Seconds")
    plt.legend()
    plt.show()
 
# This code is contributed by Nikhil Kumar Singh