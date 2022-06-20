# Lesson 1.2

time = int(input("Enter time in seconds: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = (time - hours * 3600 - minutes * 60)
print(hours, ':', minutes, ':', seconds)