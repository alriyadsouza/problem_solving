
class Solution:
    @staticmethod
    def hasPath(graph,source, dest):
        if(source == dest): return True
        for neighbor in graph[source]:
            if( Solution.hasPath(graph, neighbor, dest) ==True): return True
        return False 
        
        
graph= {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[]
}

solution=Solution()
solution.hasPath(graph,'f','k')