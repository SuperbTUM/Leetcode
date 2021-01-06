# Given n, how many structurally unique BST's (Binary Search Tree)
# that stores values 1...n?
# Interview (2nd round) with Linkedin

class Solution:
    def num_of_bst(self, n: int) -> int:
        if not n:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for k in range(i):
                dp[i] += dp[k] * dp[i-1-k]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.num_of_bst(3))

