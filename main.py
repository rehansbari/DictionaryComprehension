#Practicing Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if condition}

import random
import pandas

#Looping through a list to generate a dictionary of random scores
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

#Generating a dictionary of students who have a score of > 60
passed_students = {student:score for (student,score) in student_scores.items() if score > 60}
print(passed_students)

#Generating a dictionary of words that has a key with the amount of letters in the word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_split = sentence.split()
result = {word:len(word) for word in sentence_split}
print(result)

#Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp * 9/5) +32 for (day,temp) in weather_c.items()}
print(weather_f)

#Iterating over a Pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)
for (index, row) in student_df.iterrows():
    print(row.student)