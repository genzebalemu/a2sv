class Solution(object):
    def fizzBuzz(self, n):
        list=[]
        for i in range(n):
                list.append(str(i+1)) 
                if (i+1)%3 == 0 and (i+1)%5==0:
                    list[i]="FizzBuzz"
                elif (i+1)%3==0 and (i+1%5) !=0:
                    list[i]="Fizz"
                elif (i+1)%5 ==0:
                    list[i]="Buzz"
                
        return list