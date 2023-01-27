import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

student_df = pandas.DataFrame(student_dict)
# print(student_df)

# Loop through a data frame
# for (key, value) in student_df.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    # print(index)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
