This is a small project built for learning recommendation system using Machine Learning techniques. 
Team members: Lam Nguyen, Khang Bui, Phan Bui

Pre-process dataset:
 - Download dataset from yelp.ca/dataset
 - Extract the dataset to get 6 json files. We only need file yelp_academic_dataset_user.json so we can delete other files.
 - Run these following commands:
	+ pip install --user simplejson sqlalchemy
	+ python json_to_csv_converter.py yelp_academic_dataset_user.json
	+ python makeDB.py
	+ python updateDB.py