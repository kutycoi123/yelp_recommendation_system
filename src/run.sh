#!/bin/bash
echo "Installing dependecies..."
pip install --user -U -r requirements.txt
echo "Finished installation!!!"
echo "Running script..."
python3 json_to_csv_converter.py yelp_academic_dataset_user.json
python3 json_to_csv_converter.py yelp_academic_dataset_review.json
python3 make_review_DB.py
python3 make_user_DB.py
#python3 update_review_DB.py #Optional
#python3 update_user_DB.py   #Optional
python3 make_table.py
python3 query_v2.py
python3 make_user_business_matrix.py
echo "Finished script"