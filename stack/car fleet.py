class Solution:
    def carFleet(self, target, position ,speed):
        ans = 0
        times = [float(target - p) / s for p, s in sorted(zip(position, speed),
                                                 reverse=True)]
        maxTime = 0  # The time of the slowest car to reach the target

        for time in times:
            if time > maxTime:
                maxTime = time
                ans += 1
        return ans