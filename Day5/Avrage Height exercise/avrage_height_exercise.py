# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
student_heights_avg = sum(student_heights) / len(student_heights)
print(round(student_heights_avg))
#Write your code below this row 👇




