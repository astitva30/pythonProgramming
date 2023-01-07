def areaOfCircle():
	radius = (float)(input("Enter the radius:"));
	area = 3.14*radius*radius;
	print("Area of circle is: ",area);

def areaOfTriangle():
	base = (float)(input("Enter base:"));
	height = (float)(input("Enter height:"));
	area =0.5*base*height;
	print("Area of triangle is: ",area);

def areaOfRectangle():
	length = (float)(input("Enter length:"));
	bredth = (float)(input("Enter bredth:"));
	area = length*bredth;
	print("Area of rectangle is: ",area);

print("1 to find area of circle.");
print("2 to find area of triangle.");
print("3 to find area of rectangle.");
choice = (int)(input("Enter your choice: "));

if choice==1 :
	areaOfCircle();
elif choice==2 :
	areaOfTriangle();
elif choice==3 :
	areaOfRectangle();
else :
	print("Enter a valid Choice.");