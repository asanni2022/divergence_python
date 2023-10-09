"""
Date: 08Oct2023
Calculate Value using While Loop and If statement

"""


# This is a tutorial program that illustrates the use of the while 
#  and if statements

# initialize variables 
counter = 0 
score_total = 0 
test_score = 0

# get scores
while test_score != 999:
    test_score = int(input("Enter test score: ")) 
    if test_score >= 0 and test_score <= 100: 
        score_total += test_score 
        counter += 1

# calculate average score
#average_score = score_total / counter 
       #average_score = round(average_score)
average_score = round(score_total / counter)

# display the result
print("Total Score: " + str(score_total) + "\nAverage Score: " + str(average_score))

# print("Total Score: " + str(score_total) \  
#     + "\nAverage Score: " + str(average_score))