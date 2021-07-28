
from collections import defaultdict
class Graph:

	def __init__(self,vertices):
		self.V = vertices 
		self.V_org = vertices
		self.graph = defaultdict(list) 

	def addEdge(self,u,v,w):
		if w == 1:
			self.graph[u].append(v)
		else:	
			self.graph[u].append(self.V)
			self.graph[self.V].append(v)
			self.V = self.V + 1
	
	
	def printPath(self, parent, j):
		Path_len = 1
		if parent[j] == -1 and j < self.V_org : 
			print (j)
			return 0 
		l = self.printPath(parent , parent[j])

		
		Path_len = l + Path_len

		
		if j < self.V_org :
			print (j)

		return Path_len

	
	def findShortestPath(self,src, dest):

		
		visited =[False]*(self.V)
		parent =[-1]*(self.V)

		
		queue=[]

		
		queue.append(src)
		visited[src] = True

		while queue :
			
			
			s = queue.pop(0)
			
			
			if s == dest:
				return self.printPath(parent, s)
				

			
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True
					parent[i] = s


# Create a graph given in the above diagram
g = Graph(4)
# g.addEdge(0, 1, 2)
g.addEdge(1, 2, 30)
g.addEdge(1, 3, 10)
g.addEdge(3, 4, 20)
g.addEdge(2, 5, 40)
g.addEdge(4, 5, 20)


src = 1; dest = 2,
print ("Shortest Path between %d and %d is " %(src, dest)),
l = g.findShortestPath(src, dest)
print ("\nShortest Dist bet %d and %d is %d " %(src, dest, l)),

