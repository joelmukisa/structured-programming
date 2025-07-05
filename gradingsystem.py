print("welcome to Grading System ST Joseph's College Ombaci")
marks= int(input("please enter marks between 0 and 100: "))
if marks >= 91 and marks <= 100:
    print("Grade D1")  
elif marks >= 81 and marks <= 90:
    print("Grade D2")  
elif marks >= 71 and marks <= 80:
    print("Grade C3")   
elif marks >= 61 and marks <= 70:
    print("Grade C4")
elif marks >= 51 and marks <= 60:
    print("Grade C5")
elif marks >= 41 and marks <= 50:
    print("Grade C6")
elif marks >= 31 and marks <= 40:
    print("Grade P7")
elif marks >= 21 and marks <= 30:
    print("Grade P8")
elif marks >= 0 and marks <= 20:
    print("Grade F9")   
else:
    print("Invalid, please enter marks between 0 and 100")
    