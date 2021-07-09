import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76,98]
}

for key, value in student_dict.items():
    print(f'{key}: {value}')

student_df = pd.DataFrame(student_dict)
print(student_df)
print()

for key, value in student_df.items():
    print(key)
    print(value)
print()

for index, row in student_df.iterrows():
    print(index)
    print(row)
print()

for index, row in student_df.iterrows():
    print(row.student, row.score)
print()

for index, row in student_df.iterrows():
    if row.student == 'Angela':
        print(row.score)
