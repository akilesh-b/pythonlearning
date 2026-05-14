# Get inputs from user
student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
student_mark = input("Enter Student Mark: ")

# Open file in append mode and store records
fo =open("student_records.txt", "a")

# Write data into file
fo.write("ID: " + student_id + "\n")
fo.write("Name: " + student_name + "\n")
fo.write("Mark: " + student_mark + "\n")
fo.write("----------------------\n")

# Close file after writing
fo.close()

# Open file in read mode to display all records
fo = open("student_records.txt", "r")

print("\nAll Student Records:\n")
print(fo.read())

# Close file
fo.close()