import sqlite3
file = "user.db"
user_table = "usertable"
review_table = "reviewtable"
business_table = "businesstable"
conn = sqlite3.connect(file)
c = conn.cursor();
t = ('reviewtable', 'usertable')
set_foreign_key_query = '''PRAGMA foreign_keys=off;

                            BEGIN TRANSACTION;

                            ALTER TABLE {} RENAME TO _table1_old;

                            CREATE TABLE {}
                            (   "index" BIGINT,
                                text TEXT,
                                user_id TEXT,
                                date TEXT,
                                funny BIGINT,
                                review_id TEXT PRIMARY KEY,
                                cool BIGINT,
                                business_id TEXT,
                                stars BIGINT,
                                useful BIGINT,

                                CONSTRAINT fk_user
                                    FOREIGN KEY(user_id)
                                    REFERENCES {}(user_id)
                            );

                            INSERT INTO {} SELECT * FROM _table1_old;

                            COMMIT;

                            PRAGMA foreign_keys=on;
                                                        '''.format(review_table,review_table, user_table, review_table)
                
print (set_foreign_key_query)
c.executescript(set_foreign_key_query)

c.close()