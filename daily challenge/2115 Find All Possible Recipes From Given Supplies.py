# Class to determine which recipes can be created given a list of available supplies, using a BFS-based approach.

from collections import deque
def findAllRecipes(recipes, ingredients, supplies):
        
        available = set(supplies)
        recipeQueue = deque(range(len(recipes)))
        createdRecipes = []
        lastSize = -1

        while len(available) > lastSize:
            lastSize = len(available)
            queueSize = len(recipeQueue)
            
            while queueSize > 0:
                queueSize -= 1
                recipeIdx = recipeQueue.popleft()

                canCreate = True
                for ingredient in ingredients[recipeIdx]:
                    if ingredient not in available:
                        canCreate = False
                        break

                if canCreate is False:
                    recipeQueue.append(recipeIdx)
                else:
                    available.add(recipes[recipeIdx])
                    createdRecipes.append(recipes[recipeIdx])

        return createdRecipes
