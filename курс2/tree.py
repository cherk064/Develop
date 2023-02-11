class Solution:
    def tree(self, n, c="#"):
        for i in range(1,n):
            print(" "*(n-i)+c*(2*i-1))
a=Solution()
a.tree(5)
a.tree(10, "!")
a.tree(100, "O")
a.tree(50, "p")
