score= int(input("Enter numeric score:"))

if score>= 80 and score <= 100:
    print("Grade A")
elif score >= 70 and score < 79:
    print("Grade B")
elif score >= 60 and score < 69:
    print("Grade C")
elif score >= 50 and score < 59:
    print("Grade D")
elif score >= 0 and score < 50:
    print("Grade F")
else:
    print("invalid score(must be between 0 and 100)")

