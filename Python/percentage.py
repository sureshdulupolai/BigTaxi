import random
import math

def starPrinting(NumberOfStar):
    for Star in range(NumberOfStar):
        print('⭐', end='')

lst = [random.randint(0, 5) for i in range(900)]; totalUser = 1000; totalReview = 0; maxReview = totalUser * 5; 
for j in lst:
    totalReview += j

percentage = (totalReview / maxReview) * 100; firstData, secondData = math.modf(percentage)

if round(firstData, 2) > 0.49: roundOfPer = math.ceil(percentage)
else: roundOfPer = math.floor(percentage)

# print(roundOfPer)
if roundOfPer >= 0 and roundOfPer <= 20: starPrinting(NumberOfStar=1)
elif roundOfPer >= 21 and roundOfPer <= 40: starPrinting(NumberOfStar=2)
elif roundOfPer >= 41 and roundOfPer <= 60: starPrinting(NumberOfStar=3)
elif roundOfPer >= 61  and roundOfPer <= 80: starPrinting(NumberOfStar=4)
elif roundOfPer >= 81  and roundOfPer <= 100: starPrinting(NumberOfStar=5)

# print("Total Reviews Given:", totalReview)
# print("Maximum Possible Reviews:", maxReview)
# print("Percentage:", round(percentage, 2), "%")