import pandas as pd
from sqlalchemy import create_engine

csv_file = "yelp_academic_dataset_user.csv"
user_data_file = "user.csv"
reviewDB = create_engine('sqlite:///review.db')


chunksize = 100000
i = 0
j = 1
df = pd.read_csv(csv_file, chunksize=chunksize)
## Convert TextFileReader to Dataframe
full_data = pd.concat(df, ignore_index = True)
cols = ["user_id", "review_count", "friends"]
deleted_cols = []
for c in full_data.columns:
      if (not (c in cols)):
            deleted_cols.append(c.replace(' ', ''))
## Drop unnecessary columns
full_data = full_data.drop(deleted_cols, axis=1)

## Have a look at 100 rows in dataframe
count = 0
for index, row in full_data.iterrows():
      # print (row['user_id'], row['name'], row['friends'])
      print (row)
      count = count + 1
      if (count == 10):
            break

## Make database
print ("Making sqlite database for dataset...")
full_data.to_sql('usertable', reviewDB, if_exists='append')



