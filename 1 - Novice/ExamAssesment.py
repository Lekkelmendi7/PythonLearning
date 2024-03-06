id=input('Write the id of that student: ')

name=input('Write the student\'s name: ')


subject=input('Write the name of the subject: ')

marks=int(input('Write the marks that the student was asessed: '))

if(name=="Leke Kelmendi"):
    if(subject == "Computer Science"):
        if(marks<50):
          print('Student with id '+id+', with name '+name+', was just assessed on the subject name '+subject+', with '+str(marks)+' marks')
          print('Student doesnt meet the minimum requirements to pass, so he/she must retake the exam')
        elif(marks>=50):
            if(marks>=50 and marks <=59):
                print('Student with id '+id+', with name '+name+', was just assessed on the subject name '+subject+', with '+str(marks)+' marks')
                print('Student passed the exam, the final grade is 6')
        elif(marks>=60 and marks<=69):
                print('Student with id '+id+', with name '+name+', was just assessed on the subject name '+subject+', with '+str(marks)+' marks')
                print('Student passed the exam, the final grade is 7')
        elif(marks>=70 and marks<=79):
                print('Student with id '+id+', with name '+name+', was just assessed on the subject name '+subject+', with '+str(marks)+' marks')
                print('Student passed the exam, the final grade is 8')
        elif(marks>=80 and marks<=89):
                print('Student with id '+id+', with name '+name+', was just assessed on the subject name '+subject+', with '+str(marks)+' marks')
                print('Student passed the exam, the final grade is 9')
        elif(marks>=90 and marks<=100):
                print('Student with id '+id+', with name '+name+', was just assessed on the subject name '+subject+', with '+str(marks)+' marks')
                print('Student passed the exam, the final grade is 10')
    else:
        print('Student was not asessed yet!')
        
else:
    print('Student was not present')
        