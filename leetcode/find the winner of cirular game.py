class Solution(object):
    def findTheWinner(self, n, k):
        friends = [False] * n
        friendCount = n
        fp = 0  # friends' pointer
        while friendCount > 1:
            for _ in range(k):
                while friends[fp % n]:
                    fp += 1  # Point to the next one
                fp += 1
            friends[(fp - 1) % n] = True
            friendCount -= 1
        fp = 0
        while friends[fp]:
            fp += 1
        return fp + 1

        