#switch statement

#basic of switch statement 
letter="N"

match letter:
    case "A":
        print('The letter A was typed')
    case "B":
        print('Letter B was typed')
    case "C":
        print('The letter C was typed')
    case "D":
        print('The letter D was typed')
    case "E":
        print('The letter E was selected')
    case _:                                     #it represents the default like in java
        print("No letter was typed")
    
    