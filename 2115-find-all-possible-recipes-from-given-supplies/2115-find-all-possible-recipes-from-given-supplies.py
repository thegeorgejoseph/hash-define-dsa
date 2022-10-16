class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {recipe : [] for recipe in recipes}
        visit = set(supplies)
        cycle = set()
        res = []
        for i in range(len(recipes)):
            graph[recipes[i]].extend(ingredients[i])
        
        for i in range(len(ingredients)):
            for ing in ingredients[i]:
                if ing not in graph and ing not in visit:
                    graph[ing] = []
        
        def dfs(recipe):
            if recipe in cycle: return False
            if recipe in visit: return True
            if not graph[recipe]: return False
            
            cycle.add(recipe)
            for deps in graph[recipe]:
                if not dfs(deps): return False
            cycle.remove(recipe)
            visit.add(recipe)
            res.append(recipe)
            return True
        
        for recipe, deps in graph.items():
            dfs(recipe)
        
        return res
            
        
        