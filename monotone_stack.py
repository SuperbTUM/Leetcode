from typing import List


def monotone_stack(heights: List[int]) -> int:
    target = 0
    stack = [0]
    heights = [0] + heights + [0]  # involve guard signals
    i = 1
    while stack and i < len(heights):
        if heights[stack.pop()] <= heights[i]:
            stack.append(i)
            i += 1
        else:
            target = max(target, heights[i] * (i - stack[-1] - 1))
    return target
