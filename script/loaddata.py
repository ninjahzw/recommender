import MySQLdb

db  = MySQLdb.connect(host="localhost", # your host, usually localhost
    user="root", # your username
    passwd="123", # your password
    db="recommender") # name of the data base
cur = db.cursor() 

with open("librec-1m") as f:
    for line in f:
        uid, mid, ori_rat, biasedmf, regsvd, bpmf, itemknn, hyb = line.split()
        sql = "INSERT INTO hyb (uid, mid, ori_rat, biasedmf, regsvd, bpmf, itemknn, hyb, algo) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        args = (uid, mid, ori_rat, biasedmf, regsvd, bpmf, itemknn, hyb, 1)
        cur.execute(sql, args)

# NOTE have to commit before close.
db.commit()
db.close()
