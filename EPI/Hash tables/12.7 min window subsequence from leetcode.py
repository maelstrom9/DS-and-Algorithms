

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        def logic(g ,l ,i ,j):
            if i== 0:
                return (j, j, 0, j)
            if l == -1:
                return -1
            d = j - l[3] + l[2]
            if g == -1 or d < (g[1] - g[0]):
                return (j - d, j, d, j)
            else:
                return (g[0], g[1], j - d, j)

        if not S or not T:
            return ""

        M = [[-1] * (len(S) + 1) for i in range(len(T))]

        for i in range(len(T)):
            for j in range(len(S)):
                if T[i] == S[j]:
                    M[i][j + 1] = logic(M[i][j], M[i - 1][j], i, j)
                else:
                    M[i][j + 1] = M[i][j]

        if M[len(T) - 1][len(S)] == -1:
            return ""
        s, e, _, _ = M[len(T) - 1][len(S)]
        return S[s:e + 1]



s = Solution()

res = s.minWindow("hpsrhgogezyfrwfrejytjkzvgpjnqil","ggj")
print(res)