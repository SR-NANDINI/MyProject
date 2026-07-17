student1 = {"Math", "Science", "English"}
student2 = {"Science", "English", "History"}

print("Common Subjects:")
print(student1 & student2)

print("\nAll Subjects:")
print(student1 | student2)

print("\nOnly Student1:")
print(student1 - student2)