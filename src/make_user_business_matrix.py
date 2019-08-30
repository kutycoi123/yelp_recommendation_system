import sqlite3
import csv
import os
import time
import pandas as pd

#Read review.csv to make a hash table with keys as a concatenation of hash_business_id and hash_user_id and values as stars
#This hash table helps to get the rating star of each pair of user and business much faster
review_file = "review.csv"
df = pd.read_csv(review_file)
user_business_hash = {}
hash_user_id = {}
hash_business_id = {}
for index, row in df.iterrows():
    key = str(row['hash_business_id']) + str(row['hash_user_id'])
    user_business_hash[key] = row['stars']
    if (row['stars'] == 0):
        print (row['user_id'])
print ("Total reviews loaded: {}".format(len(user_business_hash.keys())))

# Get all training users and businesses
training_user_file = 'training_user.csv'
training_user = []
df = pd.read_csv(training_user_file)
for index, row in df.iterrows():
    hash_user_id[row['new_id']] = row['id']
    training_user.append(row['new_id'])
print ("Total traning users: {}".format(len(training_user)))
training_business_file = 'training_business.csv'
training_business = []
df = pd.read_csv(training_business_file)
for index, row in df.iterrows():
    hash_business_id[row['new_id']] = row['id']
    training_business.append(row['new_id'])
print ("Total training businesses: {}".format(len(training_business)))

#Make user-business matrix
user_business_matrix = []
count = 0
for u in training_user:
    row = [u]
    for b in training_business:
        k = str(hash_business_id[b]) + str(hash_user_id[u])
        # print (key)
        star = user_business_hash.get(k, 0)
        if (star != 0):
            count += 1
        row.append(star)
    
    user_business_matrix.append(row)
print ("Total non-zero values in user_business matrix: {}".format(count))


#Write the user-business matrix to csv file
columns = [""]
for b in training_business:
    columns.append(b)
df = pd.DataFrame(user_business_matrix, columns=columns)
user_business_matrix_file = 'user_business_matrix.csv'
if os.path.exists(user_business_matrix_file):
    os.remove(user_business_matrix_file)
df.to_csv(user_business_matrix_file, encoding='utf-8')

#
user_business_