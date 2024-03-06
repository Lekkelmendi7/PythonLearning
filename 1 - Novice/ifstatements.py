

#deklarimi dhe instancimi i nje variable

age = 18

# a simple if statement block code

if(age>=18):
    print('People on this age, are allowed to work')
else:
    print('People on this, are not allowed to work, so they just need to finish the school!')
    

# now we are trying to work with multiple else if statements


speed=120.0

if(speed <60):
    print('You are driving safely')
elif(speed >=60 and speed <100):
    print('You are driving in a high speed, so be careful')
elif(speed >= 100 and speed<130):
    print('You are driving in a really dangerous way, you are gonna kill yourself with that speed.')
else:
    ('You just crashed!!!')    
    

# so we are trying to do a nested if
'''
Define variables age and gender with predetermined values. You can choose arbitrary values for testing.
Implement nested if statements to categorize individuals based on their age and gender into the following groups:
Minor Male
Minor Female
Adult Male
Adult Female
Senior Citizen Male
Senior Citizen Female
Display a message corresponding to the category the individual falls into.
Ensure that your program does not take input from the user or use any predefined functions.
Test your program with different values of age and gender to ensure it categorizes individuals correctly.
'''

age = 27
gender = "female"

if(gender=='male'):
    if(age<18):
     print('Minor male')
    elif(age>=18 and age<=30):
         print('adult male')
    elif(age>30 and age<60):
             print('Senior citizen male')
elif(gender=='female'):
    if(age<18):
        print('minor female')
    elif(age>=18 and age<=30):
            print('adult female')
    elif(age>30 and age<60):
                print('senior citizen female')
else:
    print('You are just in the age of retirement')

'''

Title: Nested If Statement Exercise: Student Grading System

Objective:
The objective of this assignment is to practice using nested if statements in a context outside of age and gender categorization.

Instructions:
Write a program in the programming language of your choice (Python, Java, C++, etc.) to accomplish the following tasks:

Define variables marks and attendance with predetermined values. You can choose arbitrary values for testing.
Implement nested if statements to evaluate student performance based on their marks and attendance into the following grades:
A: Marks >= 90 and Attendance >= 90%
B: Marks >= 80 and Attendance >= 80%
C: Marks >= 70 and Attendance >= 70%
D: Marks >= 60 and Attendance >= 60%
E: Marks >= 50 and Attendance >= 50%
F: Otherwise
Display a message corresponding to the grade the student receives.
Ensure that your program does not take input from the user or use any predefined functions.
Test your program with different values of marks and attendance to ensure it evaluates student performance correctly.
Add comments to your code to explain the purpose of each section and improve readability.
Optionally, consider adding additional features such as handling invalid inputs or providing more detailed feedback.
Submission:
Submit your code file (.py, .java, .cpp, etc.) containing the implementation of the program.

Note:
This assignment challenges you to apply nested if statements in the context of a student grading system. Pay attention to the conditions for each grade and ensure your program accurately evaluates student performance based on their marks and attendance.
'''


marks=38
attendace=90


if(marks>=50):
    print('You just passed the exam successfully')
    if(marks>=50 and marks<=59):
        print('Your grade for this subject is E')
        print('Your results fulfill the minimum criteria to pass the exam')
    elif(marks>=60 and marks<=69):
        print('Your grade for the subject is D')
        print('Your performance is not bad at all, with sufficient knowledge to pass the exam, but there too many mistakes and many area for improvement')
    elif(marks>=70 and marks<=79):
        print('Your grade for this subject is C')
        print('Your performance is generally good, with high and advanced knowledge, but with some area for improvement')
    elif(marks>=80 and marks<=89):
        print('Your grade for this subject is B')
        print('Your work is excellent and wonderful, but with a few mistakes that are not serious')
    elif(marks>= 90 and marks<=100):
        print('Your grade for this subject is A')
        print('Your performance is exceptional and fulfill all the requirements to pass the exam, well done!')
else:
    print('You failed to meet the requirements to pass the exam')
    
    