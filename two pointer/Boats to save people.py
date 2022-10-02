class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i = 0
        j = len(people) - 1
        ans = 0
        while (i <= j):
            ans +=1
            if (people[i] + people[j] <= limit):
                i +=1
            j -=1
        return ans  