This is a small project built to learn recommendation system using Machine Learning techniques. 
Team members: Lam Nguyen, Khang Bui, Phan Bui.

Pre-process dataset:
 - Download dataset from yelp.ca/dataset
 - Extract the dataset to get 6 json files. We need two files (yelp_academic_dataset_user.json and yelp_academic_dataset_review.json) and put them inside the src folder.
 - Install python3 (3.x.x version) and pip.
 - Install Git bash to run shell script on your Window computer.
 - Open Git bash on your clone folder and run these following commands:
 	```
	cd src
	./run.sh
	```
- Now we have:
	+ a review.csv file which contains 1500 unique users, 3000 unique businesses and 100000 reviews. 
	+ a user_business_matrix.csv file which consists of user-business matrix. The first row is the id of businesses, and the second column is the id of users.
- First-time training:
	```
	python3 training_with_keras.py
	```
- Predict with saved model:
	```
	python3 predict_with_model.py
	```
