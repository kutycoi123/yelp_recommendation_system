import sqlite3
file = "review.db"
user_table = "usertable"
conn = sqlite3.connect(file)
c = conn.cursor()
set_foreign_key_query = ''' PRAGMA foreign_keys=off;

                            BEGIN TRANSACTION;

                            ALTER TABLE {} RENAME TO _table1_old;

                            CREATE TABLE {}(   
                                "index" BIGINT,
                                review_count BIGINT,
                                user_id TEXT PRIMARY KEY
                            );

                            INSERT OR IGNORE INTO {} SELECT * FROM _table1_old;

                            COMMIT;

                            PRAGMA foreign_keys=on;'''.format(user_table, user_table, user_table)
                
print (set_foreign_key_query)
c.executescript(set_foreign_key_query)
conn.commit()
c.close()