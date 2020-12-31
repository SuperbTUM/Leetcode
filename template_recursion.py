from typing import List

def solution(n: int, arr: List[str]): -> List[str]
    def template_recursion(start: int, path: List[str], result: List[str], n: int, arr: List[str]):
        if len(path) == n:
            result.append(path[:])
            return
        for i in range(start, len(arr)):
            if judgement:
                path.append(arr[i])
                template_recursion(i+1, path, result, n, arr)
                path.pop()
    result = []
    template_recursion(0, [], result, n, arr)
    return result