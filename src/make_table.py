import sqlite3
import pandas as pd

# This script is made for creating a table which contains all users who have friends
# The reason why we only need users who have friends is just because we want to use relevant rating information among users and this might reduce the sparsity of data
# We create a table for this data since it will help to speed up the computation and queries later in project
conn = sqlite3.connect("review.db")
c = conn.cursor()
query = 'SELECT user_id FROM usertable WHERE friends != "None"'
user_with_friends = c.execute(query).fetchall()
drop_tb = '''DROP TABLE IF EXISTS SubUsers;'''
create_tb = '''CREATE TABLE SubUsers(user_id TEXT PRIMARY KEY);'''
c.execute(drop_tb)
c.execute(create_tb)
insert = ''' INSERT INTO SubUsers(user_id) VALUES (?)'''
c.executemany(insert, user_with_friends)
conn.commit()

conn.close()