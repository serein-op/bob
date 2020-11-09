import pymysql

def create_table():
    db = pymysql.connect(host='localhost',db='qianchengwuyou',user='root',password='root',charset='utf8')
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS qiancheng")
    sql = """create table qiancheng (
            job_name varchar(50),
            company_name varchar(30),
            work_space varchar(15),
            work_pay varchar(15)
    )
    """

    cursor.execute(sql)
    db.close()

if __name__ == '__main__':
    create_table()
