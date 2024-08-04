#mark visited
class Solution:
    @staticmethod
    def undirectedPath(edges,nodeA,nodeB):
        graph= Solution.buildGraph(edges)
        return Solution.hasPath(graph,nodeA,nodeB, set())
    
    def hasPath(graph,src,dest, visited):
        if(src==dest): return True
        if(src in visited): return False
        visited.add(src)
        for neighbor in graph[src]:
            if(Solution.hasPath(graph, neighbor, dest, visited)== True): return True
        return False
    
    def buildGraph(edges):
        graph={}
        for edge in edges:
            a,b= edge
            if(a not in graph): graph[a]=[]
            if(b not in graph): graph[b]=[]
            graph[a].append(b)
            graph[b].append(a)
        return graph
    
    
        
setup = Solution
edge=[['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]
setup.undirectedPath(edge,'j','m')
#list to json format
graph= {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'], 
    'n': ['o']
}