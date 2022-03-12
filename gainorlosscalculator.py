a=float(input("Enter your entry price : "))
b=float(input("Enter your exit price : "))
c=((b-a)/a)*100
if(b>a):
    print(c,"% gain")
elif(a>b):
    print(c , "% loss")