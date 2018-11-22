import MySQLdb
doc=open('output.txt','w')
db=MySQLdb.connect(host='localhost',
                   user='root',
                   passwd='Zch700805zch',
                   db='mini2_sample')
cur=db.cursor()
cur.execute("select * from question")
doc.write('\n')
doc.write("Question 1")
doc.write('\n')
for row in cur.fetchall():
    print row
    print>> doc,format((row))
cur.execute("insert ignore into result"
            "(select u.name,88,u.A*u.B+88"
            " from question as u "
            "where u.name='Zhang, Chenghao')")
db.commit()
doc.write('\n')
doc.write("Question 3")
doc.write('\n')
cur.execute("select w.name, w.result from result as w where w.name='Zhang, Chenghao'")
for row in cur.fetchall():
    print row
    print>> doc, format((row))
db.close
doc.close