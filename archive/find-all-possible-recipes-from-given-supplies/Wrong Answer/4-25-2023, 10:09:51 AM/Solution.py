// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        recipes, supplies = map(set, (recipes, supplies))
        adj = defaultdict(list)
        for reqs, dish in zip(ingredients, recipes):
            for req in reqs:
                adj[req].append(dish)
        indegree = {dish: len(reqs) 
            for reqs, dish in zip(ingredients, recipes)}

        queue = deque([supply 
            for supply in supplies 
            if supply in set([e for row in ingredients for e in row])])
        visited = set()
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
                    if v in recipes:
                        visited.add(v)
        return list(visited)