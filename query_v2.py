import sqlite3
import pandas as pd
import time
import csv
import os

def BusinessCmp(b):
    return unique_businesses[b['id']]
def UsersCmp(b):
    return unique_users[b['id']]
def Find(userID, businessID, response):
    for u in response:
        if (u[0] == userID and u[1] == businessID):
            return [u[0], u[1], u[2]]
    return []
conn = sqlite3.connect("review.db")
c = conn.cursor()

q = '''SELECT user_id, business_id FROM reviewtable'''
response = c.execute(q).fetchall()
users = {}
for i in response:
    users[i[0]] = users.get(i[0], 0) + 1
users_10 = []
reviews = 0
for i in users:
    if (users[i] >= 10):
        reviews += users[i]
        tup = (i,)
        users_10.append(tup)
drop_tb = '''DROP TABLE IF EXISTS Sub2Users;'''
create_tb = '''CREATE TABLE Sub2Users(user_id TEXT PRIMARY KEY);'''
c.execute(drop_tb)
c.execute(create_tb)
insert = ''' INSERT INTO Sub2Users(user_id) VALUES (?)'''
c.executemany(insert, users_10)
conn.commit()
start = time.time()
query = 'SELECT Sub2Users.user_id as userID, reviewtable.business_id as businessID, reviewtable.stars as stars FROM Sub2Users INNER JOIN reviewtable ON Sub2Users.user_id=reviewtable.user_id'
response = c.execute(query).fetchall()
list_stars = {}
list_of_top_business = []
list_of_top_users = []
unique_users = {}
unique_businesses = {}
a = []
for u in response:
    list_stars[u[0] + u[1]] = u[2]
    unique_users[u[0]] = unique_users.get(u[0], 0) + 1
    unique_businesses[u[1]] = unique_businesses.get(u[1], 0) + 1
user_index = 0
business_index = 0
for u in unique_users:
    list_of_top_users.append({'new_id': user_index, 'id': u})
    user_index += 1
for u in unique_businesses:
    list_of_top_business.append({'new_id': business_index, 'id': u})
    business_index += 1
list_of_top_users = sorted(list_of_top_users, key=UsersCmp, reverse=True)[0:1500]
list_of_top_business = sorted(list_of_top_business, key=BusinessCmp, reverse=True)[0:3000]
with open("training_user.csv", 'w', encoding='utf-8') as fout:
    csv_file = csv.writer(fout)
    csv_file.writerow(['new_id', 'id'])
    for u in list_of_top_users:
        csv_file.writerow([u['new_id'], u['id']])
with open("training_business.csv", 'w', encoding='utf-8') as fout:
    csv_file = csv.writer(fout)
    csv_file.writerow(['new_id', 'id'])
    for u in list_of_top_business:
        csv_file.writerow([u['new_id'], u['id']])
user_business_stars = []
reviews = 0
for u in list_of_top_users:
    for i in list_of_top_business:
        stars = list_stars.get(u['id'] + i['id'], -1)
        if (stars != -1):
            print ("{} {} {}".format(u['new_id'], i['new_id'], stars))
            res = [u['new_id'], i['new_id'], stars]
            reviews += 1
            user_business_stars.append(res)

print ("Total number of reviews: {}".format(reviews))
print ("Total unique users: {}".format(len(list_of_top_users)))
print ("Total unique unique_businesses: {}".format(len(list_of_top_business)))
columns = ['user_id', 'business_id', 'stars']
print ("Saving results in csv file.....")
df = pd.DataFrame(user_business_stars, columns=columns)
p = "review.csv"
if os.path.exists(p):
    os.remove(p)
df.to_csv(p, encoding='utf-8')

end = time.time()
print ("Finished after {} mins and {} seconds".format(int((end - start)/60), int((end - start) % 60)))

conn.close()