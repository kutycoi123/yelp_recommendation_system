import pandas as pd
from sqlalchemy import create_engine

file = "yelp_academic_dataset_business.csv";
userDB = create_engine('sqlite:///user.db')


chunksize = 100000
i = 0
j = 1
for df in pd.read_csv(file, chunksize=chunksize, iterator=True):
      df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) 
      df.index += j
      i+=1
      df.to_sql('businesstable', userDB, if_exists='append')
      j = df.index[-1] + 1
# query = """SELECT * FROM usertable where user_id = {}""".format('\'TxVnXwb1lNcGKz0LSNIscg\'')
# df = pd.read_sql_query(query, userDB)
# print (df)