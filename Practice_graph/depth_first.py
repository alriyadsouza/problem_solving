# class Solution:
#     @staticmethod
#     def depthFirstPrint(graph,source):
#         stack=[source]
#         while (len(stack)>0):
#             current= stack.pop()
#             print(current)
#             for i in graph[current]:
#                 stack.append(i)


# #recursively
# class Solution:
#     @staticmethod
#     def depthFirstPrint(graph,source):
#         print(source)
#         for i in graph[source]:
#             Solution.depthFirstPrint(graph,i)
from collections import deque

class Solution:
    @staticmethod
    def breadthFirstPrint(graph,source):
        queue=deque(source)
        while (len(queue)>0):
            current = queue.popleft()
            print(current)
            for i in graph[current]:
                queue.append(i)

graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
solution=Solution()
solution.breadthFirstPrint(graph,'a')