# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
#new_dict = {new_key: new_value for item in list}
student_dict = {
    "students": ["Angela", "Tim", "Lilly"],
    "scores": [56, 70, 89]
}
import pandas
students_data_frame = pandas.DataFrame(student_dict)
print(students_data_frame)

#Loop through a data frame
for (key, value) in students_data_frame.items():
    print(key)
    print(value)

#Loop through rows of data frame
for (index, row) in students_data_frame.iterrows():
    print(index)
    print(row)