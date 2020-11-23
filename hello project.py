from flask import Flask,render_template
from flask import request
import pymysql
conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        database='test',
        charset='utf8'
    )
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    sql1 = """
    select bigname from shouye1
    """
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql1)
    ret1 = cursor.fetchall()
    b=[]
    for i in range(len(ret1)):
        a = ret1[i]
        for i in a.keys():
            b.append(a[i])
    return render_template('h.html',job=b)
@app.route('/hi')
def wangye1():
    sql1 = """
    select smallname from chaolianjie
    """
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql1)
    ret1 = cursor.fetchall()
    b=[]
    sname = "Aa"
    for i in range(len(ret1)):
        a = ret1[i]
        for i in a.keys():
            b.append(a[i])
    return render_template('w.html',name=b,Sname=sname)

# def wangye2():
#     sql1 = """
#     select smallname from chaolianjie11
#     """
#     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     cursor.execute(sql1)
#     ret1 = cursor.fetchall()
#     b=[]
#     SSname = "Bb"
#     for i in range(len(ret1)):
#         a = ret1[i]
#         for i in a.keys():
#             b.append(a[i])
#     return render_template('w.html',name1=b,SSname=SSname)
#
# def wangye3():
#     sql1 = """
#     select smallname from chaolianjie111
#     """
#     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     cursor.execute(sql1)
#     ret1 = cursor.fetchall()
#     b=[]
#     SSSname = "Cc"
#     for i in range(len(ret1)):
#         a = ret1[i]
#         for i in a.keys():
#             b.append(a[i])
#     return render_template('w.html',name2=b,SSSname=SSSname)



if __name__ == '__main__':
    app.run()

