from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:

        # setup adj list
        adj = defaultdict(list)
        indegree = defaultdict(int)

        recipe_lookup = set(recipes)
        
        for i in range(len(recipes)):
            recipe = recipes[i]
            for j in range(len(ingredients[i])):
                 adj[ingredients[i][j]].append(recipe)
                 indegree[recipe] += 1
        
        q = deque(supplies)
        res = []

        while q:
            food = q.popleft()
            if food in recipe_lookup:
                res.append(food)
            for item in adj[food]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    q.append(item)
        return res



        