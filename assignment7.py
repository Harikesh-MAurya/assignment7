# (question-1)...............................................................................
# months=(1,3,5,7,8,10,12)
# month=int(input("Enter month number : "))
# if month in months:
#     number_of_days=31
#     print("the number of days in month is : %d "%(number_of_days))
# else:
#     months=(4,6,9,11)
#     if month in months:
#         number_of_days=30
#         print("nmber of days in month is : %d  "%(number_of_days))
#     else:
#         if month==2:
#             year=int(input("ENter year : "))
#             number_of_days=29
#             if (year%4==0 and year%100 !=0)or(year%400==0):
#                 print(year,"the number of days in",month,"is : ",number_of_days,"and it is a leap year")
#             else:
#                 number_of_days=28
#                 print(year,"the number of days in",month,"is : ",number_of_days,"and it is a not leap year")


# (question-2)................................................................................
# m,n=int(input("Enter m : ")),int(input("ENter n : "))
# p=str(input("Enter op : "))
# match p:
#     case "add":
#         print(m+n)

#     case "subs":
#         print(m-n)

#     case "mult":
#         print(m*n)

#     case "divide":
#         print(m//n)


# (question-3(a))..........................................................................
# x,y,z=int(input("Enter x : ")),int(input("ENter y : ")),int(input("Enter z : "))
# if (x==y) or (y==z) or (x==z):
#     print("Isosceles trangle")
# else:
#     print("Not Isosceles trangle")  


# (question-3(b))..........................................................................
# import math
# x,y,z=int(input("Enter x : ")),int(input("ENter y : ")),int(input("ENter y : "))
# if z*z==x*x+y*y:
#     print("right angle trangle")
# else:
#     print("not")


# (question-4)..........................................................................
# x,y,z=int(input("Enter x : ")),int(input("ENter y : ")),int(input("Enter z : "))
# if (x==y)and (y==z)and(z==x):
#     print("Equilatiral trangle")
# else:
#     print("Not Equilatiral trangle")  



# (question-5)..................................................................................
# age=int(input("Enter age : "))
# if age<10:
#     print("kids")
# elif 10<age or age<20:
#     print("Teen")
# elif 20<age or age<40:
#     print("Young")
# elif 40<age or age<60:
#     print("Experienced")
# elif age>60:
#     print("Senior citizine")
# else:
#     print("Error")



# (question-6)...................................................................................
# s=input("Enter string : ")
# if len(s.split(" "))>1:
#     print("Mutiword string")
# else:
#     print("Singleword string")


# (question-9).................................................................
from math import fabs


feverate_color=input("what is your feverate color : ")
if feverate_color.capitalize()==("Red"):
    print("Satureday")
elif feverate_color.capitalize()==("Yellow"):
    print("Monday")
elif feverate_color.capitalize()==("Blue"):
    print("Tuesday")
elif feverate_color.capitalize()==("White"):
    print("Thursday")
elif feverate_color.capitalize()==("Black"):
    print("Friday")
elif feverate_color.capitalize()==("All other colour"):
    print("Sunday")
else:
    print("error")