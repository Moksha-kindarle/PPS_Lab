# Input marks
m1, m2, m3, m4 = map(int, input().split())

# Total marks
total = m1 + m2 + m3 + m4

# Aggregate percentage
aggregate = total / 4

# Grade calculation
if aggregate >= 75:
    grade = "Distinction"
elif aggregate >= 60:
    grade = "First Division"
elif aggregate >= 50:
    grade = "Second Division"
elif aggregate >= 40:
    grade = "Third Division"
else:
    grade = "Fail"

# Output
print(total)
print(f"{aggregate:.2f}")
print(grade)
