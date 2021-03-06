from typing import List

global judgement
def solution(n: int, arr: List[str]): -> List[List[str]]
    def template_recursion(start: int, path: List[str], result: List[str], n: int, arr: List[str]):
        if len(path) == n:
            result.append(path[:])
            return
        for i in range(start, len(arr)):
            if judgement: # The judgement is for pruning
                path.append(arr[i])
                template_recursion(i+1, path, result, n, arr)
                path.pop()
    result = []
    template_recursion(0, [], result, n, arr)
    return result

def solution2(arr: List[int]): -> List[List[int]]
    def template_recursion(path: List[int], result: List[int], visited: List[int], arr: List[int]):
        if len(path) == len(arr):
            result.append(path[:])
            return
        for i in range(len(arr)):
            if not visited[i] and judgement:
                path.append(arr[i])
                visited[i] = True
                template_recursion(i+1, path, result, n, arr)
                path.pop()
                visited[i] = False
    result = []
    visited = [False] * len(arr)
    template_recursion([], result, visited, arr)
    return result    

# example for judgement
# for subset
judgement = ["i > start and nums[i] == nums[i-1]"]
# for full array
judgement = ["i > 0 and nums[i] == nums[i-1] and not visited[i]"]
