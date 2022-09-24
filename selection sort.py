# class Solution: 
#     def selectionSort(self, arr,n):
#         for i in range(n - 1):
#             min = i
#             for j in range(i + 1, n):
#                 if(arr[j] < arr[min]):
#                     min = j
#             arr[i], arr[min] = arr[min], arr[i] 
#User function Template for python3

class Solution: 
    # def select(self, arr, i):
    #     n = len(arr)
    #     for i in range(n - 1):
    #         min = i
    #         for j in range(i + 1, n):
    #             if(arr[j] < arr[min]):
    #                 min = j
    #         arr[i], arr[min] = arr[min], arr[i]
        # n= len(arr)
        # for i in range(n-1):
        #     for j in range(n-1):
        #         if arr[j] < arr[j-1]:
        #             arr[j-1],arr[j]=arr[j],arr[j-1]
          
        #         # return arr
            
        # # code here 
    
    def selectionSort(self, arr,n):
        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):
                if(arr[j] < arr[min]):
                    min = j
            arr[i], arr[min] = arr[min], arr[i]    
        
