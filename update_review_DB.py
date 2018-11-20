import sqlite3
file = "review.db"
review_table = "reviewtable"
conn = sqlite3.connect(file)
c = conn.cursor()
set_foreign_key_query = ''' PRAGMA foreign_keys=off;

                            BEGIN TRANSACTION;

                            ALTER TABLE {} RENAME TO _table1_old;

                            CREATE TABLE {}(   
                                "index" BIGINT,
                                user_id TEXT,
                                review_id TEXT PRIMARY KEY,
                                business_id TEXT,
                                stars BIGINT
                            );

                            INSERT OR IGNORE INTO {} SELECT * FROM _table1_old;

                            COMMIT;

                            PRAGMA foreign_keys=on;'''.format(review_table, review_table, review_table)
                
print (set_foreign_key_query)
c.executescript(set_foreign_key_query)
conn.commit()
c.close()