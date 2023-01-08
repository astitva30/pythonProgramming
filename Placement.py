password = input("Enter password");

FEEDBACK = 0;
RESULT = 0;
RANK = 0;
if password=="abc":
	candidateName = input("Enter Candidate Name: ");
	courseName = input("Enter Course Name: ");
	branch = input("Enter Branch Name: ");
	year = (int)(input("Enter Year: "));
	sem = (int)(input("Enter Semester: "));
	per10 = (float)(input("Enter 10th percentage: "));
	per12 = (float)(input("Enter 12th percentage: "));

	if per10>65 && per12>65:
	
		trainingStatus = (int)(input("Enter 1 if you are self-trained else enter 2 if you are trained by someone : "));
		trainingMode = (int)(input("Enter 1 if you got offline training else enter 2 if you got online trianing : "));

		acadStatus = input("Enter 1 if you have good academic status else enter 0: ");
		placementPrep = input("Enter 1 if you have good placement prepration else enter 0: ");
	
		if trainingStatus==1 and trainingMode==1:  #self trained offline

				if acadStatus==1 and placementPrep==1 :
					RANK=8;
				elif acadStatus==1 and placementPrep==0 :
					RANK=5;
				elif acadStatus==0 and placementPrep==1 :
					RANK=7;
				elif acadStatus==0 and placementPrep==0 :
					RANK=0;
				else :
					RANK=0;

		elif trainingStatus==1 and trainingMode==2:	#self trained online

				if acadStatus==1 and placementPrep==1 :
					RANK=8;
				elif acadStatus==1 and placementPrep==0 :
					RANK=5;
				elif acadStatus==0 and placementPrep==1 :
					RANK=7;
				elif acadStatus==0 and placementPrep==0 :
					RANK=0;
				else :
					RANK=0;

		elif trainingStatus==2 and trainingMode==1:	#trained by someone offline

				if acadStatus==1 and placementPrep==1 :
					RANK=10;
				elif acadStatus==1 and placementPrep==0 :
					RANK=8;
				elif acadStatus==0 and placementPrep==1 :
					RANK=7;
				elif acadStatus==0 and placementPrep==0 :
					RANK=2;
				else :
					RANK=0;

		elif trainingStatus==2 and trainingMode==2:	#trained by someone online

				if acadStatus==1 and placementPrep==1 :
					RANK=9;
				elif acadStatus==1 and placementPrep==0 :
					RANK=7;
				elif acadStatus==0 and placementPrep==1 :
					RANK=7;
				elif acadStatus==0 and placementPrep==0 :
					RANK=1;
				else :
					RANK=0;
	else:
		trainingStatus = (int)(input("Enter 1 if you are self-trained else enter 2 if you are trained by someone : "));
		trainingMode = (int)(input("Enter 1 if you got offline training else enter 2 if you got online trianing : "));

		acadStatus = input("Enter 1 if you have good academic status else enter 0: ");
		placementPrep = input("Enter 1 if you have good placement prepration else enter 0: ");

		if trainingStatus==1 and trainingMode==1:  #self trained offline

				if acadStatus==1 and placementPrep==1 :
					RANK=7;
				elif acadStatus==1 and placementPrep==0 :
					RANK=4;
				elif acadStatus==0 and placementPrep==1 :
					RANK=6;
				elif acadStatus==0 and placementPrep==0 :
					RANK=0;
				else :
					RANK=0;

		elif trainingStatus==1 and trainingMode==2:	#self trained online

				if acadStatus==1 and placementPrep==1 :
					RANK=7;
				elif acadStatus==1 and placementPrep==0 :
					RANK=4;
				elif acadStatus==0 and placementPrep==1 :
					RANK=6;
				elif acadStatus==0 and placementPrep==0 :
					RANK=0;
				else :
					RANK=0;

		elif trainingStatus==2 and trainingMode==1:	#trained by someone offline

				if acadStatus==1 and placementPrep==1 :
					RANK=9;
				elif acadStatus==1 and placementPrep==0 :
					RANK=7;
				elif acadStatus==0 and placementPrep==1 :
					RANK=6;
				elif acadStatus==0 and placementPrep==0 :
					RANK=1;
				else :
					RANK=0;

		elif trainingStatus==2 and trainingMode==2:	#trained by someone online

				if acadStatus==1 and placementPrep==1 :
					RANK=8;
				elif acadStatus==1 and placementPrep==0 :
					RANK=6;
				elif acadStatus==0 and placementPrep==1 :
					RANK=6;
				elif acadStatus==0 and placementPrep==0 :
					RANK=0;
				else :
					RANK=0;
		
print("Your Placement Prediction Rank is: ", RANK);








