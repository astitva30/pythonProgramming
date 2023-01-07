def volOfCone():
	radius = (float)(input("Enter radius:"));
	height = (float)(input("Enter height:"));
	vol = 3.14*radius*radius*height/3;
	print("Volume of cone is: ",vol);

def volOfSphere():
	radius = (float)(input("Enter the radius:"));
	vol = 3.14*radius*radius*radius*1.33;
	print("Volume of sphere is: ",vol);

def volOfCylinder():
	radius = (float)(input("Enter radius:"));
	height = (float)(input("Enter height:"));
	vol = 3.14*radius*radius*height;
	print("Volume of cylinder is: ",vol);

print("1 to find volume of cone.");
print("2 to find volume of sphere.");
print("3 to find volume of cylinder.");
choice = (int)(input("Enter your choice: "));

if choice==1 :
	volOfCone();
elif choice==2 :
	volOfSphere();
elif choice==3 :
	volOfCylinder();
else :
	print("Enter a valid Choice.");