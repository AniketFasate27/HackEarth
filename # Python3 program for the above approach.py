# Python3 program for the above approach

# Function for DFS traversal to update
# the distance vector
def dfs(u, s):
	
	global vis, Adj, dist
	vis[u] = True
	for it in Adj[u]:

		if (vis[it] == False):
			dfs(it, s + 1)

	dist[u] = max(dist[u], s)

def minFarthestDistance(arr, n):
	
	global dist, vis, Adj

	for i in range(n - 1):
		Adj[arr[i][0]].append(arr[i][1])
		Adj[arr[i][1]].append(arr[i][0])

	for i in range(1, n + 1):

		for j in range(n + 1):
			vis[j] = False

		dfs(i, 0)

	print(min(dist[i] for i in range(1, n + 1)))

# Driver Code
if __name__ == '__main__':
	
	dist = [0 for i in range(10001)]
	vis = [False for i in range(10001)]
	Adj = [[] for i in range(10001)]

	# Number of Nodes
	N = int(input())
	arr = [ [ 1, 4 ], [ 2, 3 ],
			[ 3, 4 ], [ 4, 5 ], [ 5, 6 ] ]

	minFarthestDistance(arr, N)

# This code is contributed by mohit kumar 29
