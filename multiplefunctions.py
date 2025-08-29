class multiplefunctions:
    def Subfields():
        print("Sub-fields in AI are:")
        list = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for subfield in list:
            print(subfield)

    def OddEven():
        num = int(input("Enter the number:"))
        if (num%2==1):
            print(num," is Odd")
        else:    
            print(num," is Even")

    def eligible():
        gender = input("Your gender:")
        age = int(input("Your age:"))
        if age >= 21 and gender == "Male":
            print("Eligible")
        elif age >=18 and gender == "Female":
            print("Eligible")
        else:
            print("Not Eligible")

    def percentage():
        Sub1 = int(input("Subject1 ="))
        Sub2 = int(input("Subject2 ="))
        Sub3 = int(input("Subject3 ="))
        Sub4 = int(input("Subject4 ="))
        Sub5 = int(input("Subject5 ="))
        Total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
        Percentage = Total/500*100
        print("Total:",Total)
        print("Percentage:",Percentage)

    def triangle():
        Height1 = int(input("Enter height1 of the triangle"))
        Breadth = int(input("Enter Breadth of the trainge"))
        Height2 = int(input ("Enter height2 of the triange:"))
        area = Height1*Breadth/2
        perimeter = Height1+Height2+Breadth
        print("Area of the triangle:", area)
        print("Perimeter of the triange:",perimeter)        