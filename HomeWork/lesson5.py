from psycopg2 import connect

conn = connect('postgresql://belbank:belbank@localhost:5432/bank')
# with conn.cursor() as cur:
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS users(
#             id BIGSERIAL PRIMARY KEY,
#             name VARCHAR(64) NOT NULL,
#             email VARCHAR(128) UNIQUE NOT NULL
#         );
#     ''')

#защита от sql иньекции
# with conn.cursor() as cur:
#     cur.execute('''
#         INSERT INTO users(name, email) VALUES(%s, %s);
#     ''',('vasya', 'vasya@email.com'))
#     conn.commit()

# with conn.cursor() as cur:
#     cur.execute('''
#         SELECT * FROM users;
#     ''')
#     print(cur.fetchall()) #список кортеджей


from psycopg2.extras import NamedTupleCursor
with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
    cur.execute('''
        SELECT * FROM users;
    ''')
    #print(cur.fetchall())#  список  nametapov
    #print(cur.fetchall()[0].name) #
    for i in cur:
        print(i)

