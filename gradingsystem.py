import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] <= 37:
            if grades[i] < 10:
               grades[i]=None
                
            else:
                grades[i] = grades[i]
        else:
            if (((grades[i]//5)+1)*5) - grades[i] < 3:
                grades[i] = (((grades[i]//5)+1)*5)
    return grades
    # Write your code here

if name == 'main':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()