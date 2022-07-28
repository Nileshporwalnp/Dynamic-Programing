"""You are given weights and values of N items,
 put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
 Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which 
represent values and weights associated with N items respectively. 
Also given an integer W which represents knapsack capacity, 
find out the maximum value subset of val[] such that
 sum of the weights of this subset is smaller than or equal to W.
  You cannot break an item, either pick the complete item or dont pick it (0-1 property)."""
def knapsack(wt,val,w,n):
    if n==0 or w==0:
        return 0
    if k[n][w]!=-1:
        return k[n][w]
    
    if wt[n-1]<=w:
        k[n][w]=max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
        return k[n][w]
    
    elif wt[n-1]>w:
        k[n][w]=knapsack(wt,val,w,n-1)
        return k[n][w]
val = [60, 100, 120 ]
wt = [10, 20, 30 ]
w = 50
n = len(val)
k=[[-1 for i in range(w+1)] for j in range((n+1))]
print(knapsack(wt,val,w,n))
    

