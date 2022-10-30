class Solution(object):
    def corpFlightBookings(self, bookings, n):
        ans=[0]*n
        for i in range(len(bookings)):
            ans[bookings[i][0]-1] += bookings[i][-1]
            if bookings[i][1] < n :
                ans[bookings[i][1]] -=bookings[i][-1]
        for i in range(1,len(ans)):
            ans[i] +=ans[i-1]
        return ans 