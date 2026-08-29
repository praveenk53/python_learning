marks = int(input("Enter your marks (<= 100): "))
if marks >= 90 and marks <= 100:
    print("Grade: A")

elif marks <=89 and marks >= 80:
        print("Grade: B")

elif marks <=79 and marks >= 70:
        print("Grade: C")

elif marks <=69 and marks >= 60:
        print("Grade: D")

elif marks <=59 and marks >= 0:
        print("Grade: F")
        
else: 
     print("Invalid marks entered. Please enter a value between 0 and 100.")
    