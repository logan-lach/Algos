# Correct Answer, times out
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    def continuous(p1, p2, p3):

        while p1 < len(s1) and p2 < len(s2) and p3 < len(s3):
            if s1[p1] == s2[p2] and s1[p1] == s3[p3]:
                return continuous(p1 + 1, p2, p3+1) or continuous(p1, p2 + 1, p3+1)

            elif s1[p1] == s3[p3]:
                p1 += 1

            elif s2[p2] == s3[p3]:
                p2 += 1

            else:
                return False

            p3 += 1

        if p3 == len(s3):
            return True

        elif p1 < len(s1):
            while p1 < len(s1) and p3 < len(s3):
                if s1[p1] != s3[p3]:
                    return False
                p1 += 1
                p3 += 1
            return True if p3 == len(s3) else False

        elif p2 < len(s2):
            while p2 < len(s2) and p3 < len(s3):
                if s2[p2] != s3[p3]:
                    return False
                p2 += 1
                p3 += 1
            return True if p3 == len(p3) else False

    return continuous(0, 0, 0)

print(isInterleave("aabcc",
"dbbca",
"aadbbcbcac"))
