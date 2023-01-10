soldProducts = (int)(input("Enter the number of products sold: "));

if soldProducts>=10 :
	print("Your total salary including incentive is: ", 10000+(soldProducts*100));
else :
	print("Your total salary including incentive is: ", 10000+(soldProducts*50));
