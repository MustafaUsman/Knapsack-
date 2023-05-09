# import the time module
import time
import matplotlib.pyplot as plt
  
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
 
# Main greedy function to solve problem
def fractionalKnapsack(W, arr):
 
    # Sorting Item on basis of ratio
    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)   
 
    # Result(value in Knapsack)
    finalvalue = 0.0
 
    # Looping through all Items
    for item in arr:
 
        # If adding Item won't overflow,
        # add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
 
        # If we can't add current Item,
        # add fractional part of it
        else:
            finalvalue += item.profit * W / item.weight
            break
     
    # Returning final value
    return finalvalue



def make_data(name):

    f = open(name, "r")
    a = f.readline().splitlines()
    length = int(a[0])
    P = []
    W = []
    for i in range(int(a[0])):
        a = f.readline().splitlines()
        z = a[0].split(' ')
        P.append(Item(int(z[1]),int(z[2])))
        
    a = f.readline().splitlines()
    return P,int(a[0]),length
 
# Driver Code
if __name__ == '__main__':

    N = []
    R = []
    D = []
    M = []
    for i in range(7):
        fname = f'tests/test{i}.txt'
        a = make_data(fname)
        arr = a[0]
        
        W = a[1]
        N.append(a[2]) #length of problem


        seconds1 = time.time()    
        print(fractionalKnapsack(W, arr))    # Dynamic Knapsack code implementation from geeksforgeeks
        seconds2 = time.time()
        D.append(seconds2 - seconds1)
        

    # create data
    
    
    # plt.plot(N, R, label = "Recursion")
    plt.plot(N, D, label = "Greedy")
    # plt.plot(N, M, label = "Memoized")
    plt.xlabel("Problem Length")
    plt.ylabel("Time in Seconds")
    plt.legend()
    plt.show()