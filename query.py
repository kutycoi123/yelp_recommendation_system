import sqlite3
import pandas as pd
import time
import os
conn = sqlite3.connect("review.db")

# This script is made to create a csv file which contains 100000 records of user_id, business_id and rating stars


c = conn.cursor()


reviews = 0
users = {}
user_review_stars = []
businesses = {}
start = time.time()
query = 'SELECT SubUsers.user_id as userID, reviewtable.business_id as businessID, reviewtable.stars as stars FROM SubUsers INNER JOIN reviewtable ON SubUsers.user_id=reviewtable.user_id'
response = c.execute(query).fetchall()
print (len(response))
for i in response:
    temp = []
    temp.append(i[0])
    temp.append(i[1])
    temp.append(i[2])
    businesses[i[1]] = True
    user_review_stars.append(temp)
    reviews += 1
    users[i[0]] = True
    print ("{} {} {}".format(i[0], i[1], i[2]))
    if (reviews == 100000):
        break

print ("Total number of reviews: {}".format(reviews))
print ("Total unique users: {}".format(len(users)))
print ("Total unique businesses: {}".format(len(businesses)))
columns = ['user_id', 'business_id', 'stars']
print ("Saving results in csv file.....")
df = pd.DataFrame(user_review_stars, columns=columns)
p = "review.csv"
if os.path.exists(p):
    os.remove(p)
df.to_csv(p, encoding='utf-8')

end = time.time()
print ("Finished after {} mins and {} seconds".format(int((end - start)/60), int((end - start) % 60)))

conn.close()











