This is a small project built for learning recommendation system using Machine Learning techniques. 
Team members: Lam Nguyen, Khang Bui, Phan Bui

Pre-process dataset:
 - Download dataset from yelp.ca/dataset
 - Extract the dataset to get 6 json files. We only need file yelp_academic_dataset_user.json and yelp_academic_dataset_review.json so we can delete other files.
 - Install python3 (3.x.x version) and pip
 - Install Git bash to run shell script on your Window computer
 - Open Git bash on your clone folder and run these following commands:
 	```
	cd src
	./run.sh
	```
- Now we have:
	+ a file named review.csv. In this file, there are totally 1500 unique users, 3000 unique businesses and 100000 reviews. 
	+ a file named user_business_matrix.csv. This file contains the user-business matrix. The first row is the id of businesses, the second column is the id of users
- First-time training:
	```
	python3 training_with_keras.py
	```
- Predict with saved model:
	```
	python3 predict_with_model.py
	```
