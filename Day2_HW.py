#Q2. PASSWORD STRENGTH VALIDATOR
password = input("Enter your password: ")

upper = any(c.isupper() for c in password)
lower = any(c.islower() for c in password)

length = len(password)

if length > 8 and upper and lower :
    print("Strong Password")
elif length == 8:
    print("Moderate Password")
else:
    print("Weak Password")

#Q3.NESTED GRADE EVALUATION WITH ATTENDANCE
def exam_Result(marks, attendance):
        if marks >= 50 and attendance >= 75:
            print("pass")
        elif marks < 50 and attendance < 75:
            print("fail due to both")
        elif marks < 50:
            print("fail due to marks")
        elif attendance < 75:
            print("fail due to attendance")
exam_Result(0,80)

#Q4. TRAFFIC FINE CALCULATOR
def fine_calculator(car_spd, truck_spd, bike_spd):
    if car_spd > 60:
        if car_spd <= 70:
            print("500 fine") 
        elif car_spd < 80:
            print("1000 fine")
        else:
            print("2000 fine + license ban")
    if truck_spd > 60:
        if truck_spd <= 70:
            print("1000 fine") 
        elif truck_spd < 75:
            print("2000 fine")
        else:
            print("4000 fine + license ban")
    if bike_spd > 60:
        if bike_spd <= 70:
            print("250 fine") 
        elif bike_spd < 85:
            print("500 fine")
        else:
            print("1000 fine + license ban")

fine_calculator(70,65,65)

#Q5. MULTI LOAN ELIGIBILTY CHECKER
age = int(input("enter your age: "))
income = int(input("enter your income: "))
credit_score = int(input("enter your credit_score: "))

if (age >= 21 and age <= 60) and income >= 25000 and (credit_score >= 600 and credit_score <= 850):
    print("approve loan")
elif (age < 21 or age > 60) and income < 25000 and (credit_score < 600 or credit_score > 850):
    print("rejected due to multiple reasons")
elif (age < 21 or age > 60):
    print("rejected due to age")
elif income < 25000:
    print("rejected due to low income")
elif credit_score < 600 or credit_score > 850:
    print("rejected due to poor credit")  