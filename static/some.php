<?php
$Animal_Type=filter_input(INPUT_POST, 'Animal_Type');
$No_Of_Counts=filter_input(INPUT_POST,'No_Of_Counts');
$Breed_Name=filter_input(INPUT_POST,'Breed_Name');
$Type_Images=filter_input(INPUT_POST,'Type_Images');
$Owner_Name=filter_input(INPUT_POST,'Owner_Name');
if(!empty($Animal_Type)){
	 if(!empty($No_Of_Counts)){
		 if(!empty($Breed_Name)){
			 if(!empty($Type_Images)){
				 if(!empty($Owner_Name)){
					  $host="localhost";
					 $dbusername="root";
					 $dbpassword="";
					 $dbname="Desii_Catlle";
					 //create connection
					 $conn = new mysqli($host,$dbusername,$dbpassword,$dbname);
					 if(mysqli_connect_error()){
						 die('connect error('.mysqli_connect_errno().')'
						 .mysqli_connect_error());
					 }
					 else
					 {
						 $sql="INSERT INTO Owner_Details(Animal_Type,No_Of_Counts,Breed_Name,Type_Images,Owner_Name)
					 values('$Animal_Type','$No_Of_Counts','$Breed_Name','$Type_Images','$Owner_Name')";
					 if($conn->query($sql))
					 {
						 echo "New record is inserted succeessfully";
					 }
					 else
					 {
						 echo "error:".$sql ."<br>".$conn->error;
					 }
					 $conn->close();
					 }
				 }
				  else{
					 echo "trainer_address should not be empty";
					 die();
				 }
			 }
			 else{
					 echo "trainer_id should not be empty";
					 die();
		 }
		 }
		 else{
					 echo "trainer_phonenumber should not be empty";
					 die();
		 }
	 }else{
					 echo "trainer_email should not be empty";
	                 die();
	 }
 }
 else{
					 echo "trainer_name should not be empty";
					 die();
 }
 











?>
