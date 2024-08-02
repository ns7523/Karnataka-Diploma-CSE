print("***dictionary operations***")
student={"name":"abc","reg_no":"cs001","branch":"cse"}
print("the student dictionary is:",student)
print("the student name is:",student["name"])
print("the student reg_no is:",student["reg_no"])
student["sem"]=3
student["college"]="bgsp"
print("the student dictionary after inserting sem and college is:",student)
student["name"]="xyz"
print("the student dictionary after changing name is:",student)
del student["branch"]
print("the student dictionary after deleting branch:",student)
student.pop("reg_no")
print("the student dictionary after removing reg_no:",student)
