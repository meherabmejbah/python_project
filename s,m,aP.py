# import numpy as np

students = {
    "Mejbah" : 90,
    "Dibbo" : 95,
    "Mahi" : 80,
    "Rimi" : 60,
    "Malukha" : 48,
    "Sajid" : 92,
    "Tafim" :  82,
    "Riyad" :  33,
    "Ramim" : 13,
    "Habib" : 45,
    "Mahin" : 45,
    "Pial" : 55,
    "Neha" : 39,
    "Adrota" : 50,
    "Rishad" : 32,
}

names = list(students.keys())
marks = list(students.values())

#Creating Numpy Array
# marks_array = np.array(marks)

#Info
total_students = len(students)
# average = np.mean(marks_array)
# highest = np.max(marks_array)
# lowest = np.min(marks_array)

print(f"Total Students: {total_students}")
# print(f"Average Marks: {average}")
# print(f"Higest Marks: {highest}")
# print(f"Lowest Marks: {lowest}")

# print("\nPassed Students...")
# for names, marks in students.items():
#     if marks >= 50:
#         print(f"{names} passed with {marks}")

# print("\nFailed Students...")
# for names, marks in students.items():
#     if marks < 50:
#         print(f"{names} falied with {marks}")



#Sort Students by Marks (Descending)
sorted_students = sorted(students.items(), key = lambda item: item[1], reverse = True)

# Show Sorted Results
print("\nStudents Sorted by Marks (HIGH -> LOW): \n")
for names, marks in sorted_students:
    print(f"{names} : {marks}")

# Who is Highest & Lowest Scorer?
topper_name, topper_mark = sorted_students[0]
last_name, last_mark = sorted_students[-1]

print(f"\nHigest Score: {topper_name} with {topper_mark}")
print(f"\nLowest Score: {last_name} with {last_mark}")

# Full Report Print
print("\nFull Student Report\n..............")
for i, (names, marks) in enumerate(sorted_students, start = 1):
    status = "Pass" if marks >= 50 else "Fail"
    print(f"{i}. {names:<10} Marks: {marks:<3} Status: {status}")
