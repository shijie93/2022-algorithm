class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        
        def traverse(graph, s, path):
            path.append(s)
            if s == n-1:
                res.append(path.copy())
                path.pop()
                return
            for v in graph[s]:
                traverse(graph, v, path)
            path.pop()
        traverse(graph, 0, [])
        return res
