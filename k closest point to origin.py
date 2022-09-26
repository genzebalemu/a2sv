class Solution(object):
    def kClosest(self, points, k):
        points.sort(key = lambda k: k[0]**2 + k[1]**2)
        return points[:k]  
        return(kClosest(points, k))

#         empty=[]
#         list=[]
#         for i in range(len(points)):
#             list.append(((points[i][0])**2)+((points[i][1])**2))
#         list.sort()
#         for i in range(k):
#             for j in range(len(points)):
#                 if list[i]==((points[j][0])**2)+((points[j][1])**2):
#                     empty.append(points[j])
#         return empty[:k]
                