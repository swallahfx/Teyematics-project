# import psycopg2, csv

# def connections():
#     conn = psycopg2.connect(host= 'localhost',
#             database='startingup',
#             user='postgres',
#             password=1234,
#             port= 5432
            
            
#         )
#     # cur = conn.cursor() 
#     return conn

# def create_sqlite():
  
    
#     sql = """
#     CREATE TABLE posts (
#         userId SMALLINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#         id SMALLINT NOT NULL UNIQUE,
#         title VARCHAR(25),
#         body VARCHAR(25),
    
#          );

#     CREATE TABLE comments (
#         postId SMALLINT NOT NULL,
#         id SMALLINT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 101 INCREMENT BY 1),
#         name VARCHAR(25),
#         email VARCHAR(25),
#         body VARCHAR(25),
#         FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE,
#         PRIMARY KEY (id)
# );"""
#     cur = connections().cursor() 
#     cur.execute(sql)
    
# def post_save():
#     with open('posts.csv','r') as fin: 
#         comments_file = csv.DictReader(fin)
#         print(comments_file) 
#         # to_database = [(i['userId'], i['id'],i['title'],i['body']) for i in comments_file]
#         # return to_database
    
# def comments_save():
#     with open('comments.csv','r') as fin: 
#         comments_file = csv.DictReader(fin) 
#         to_database = [(i['postId'],i['id'],i['name'],i['email'], i['body']
#                     ) for i in comments_file]
#         return to_database
    
# def insert_to_db():
#             cur = connections().cursor()
#             cur.executemany('''INSERT INTO posts ('userId', 
#                             'id', title, body) 
#                             VALUES (?, ?, ?, ?);''',post_save())
#             cur.executemany('''INSERT INTO comments ('postId',
#                             'id' title, body) 
#                             VALUES (?, ?, ?, ?);''',comments_save())
#             connections().commit()
# post_save()
# # insert_to_db()


# import csv, json
# csvfile = 'comments.csv'
# jsonfile = 'comments.json'

    
# data = {}
    
# with open(csvfile) as file:
#     csvreader = csv.DictReader(file)
#     for rows in csvreader:
#             id = rows['id']
#             data[id] = rows
            
# with open(jsonfile, 'w') as jsfile:
#         jsfile.write(json.dumps(data, indent=4))