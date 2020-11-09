import requests
from lxml import etree
import csv
import pymysql
#获取请求
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
def get_response(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36'}
    response = requests.get(url,headers=headers)
    response.encoding = 'gbk'
    return response.text

#分析源码，获取信息所属块状位置
def get_html(html):
    html = etree.HTML(html)
    infos = html.xpath('//div[@class="el"]')[4:]
    info = []
    for i in infos:
        key = {}
        keylist=[]
        key['job_name'] = str(i.xpath('.//p[@class="t1 "]//a/@title')).strip("[']")
        key['company_name'] = str(i.xpath('.//span[@class="t2"]/a/text()')).strip("[']")
        key['work_space'] = str(i.xpath('.//span[@class="t3"]/text()')).strip("[']")
        key['work_pay'] = str(i.xpath('.//span[@class="t4"]/text()')).strip("[']")

        info.append(key)
        keylist.append(key['job_name'])
        keylist.append(key['company_name'])
        keylist.append(key['work_space'])
        keylist.append(key['work_pay'])
        info.append(keylist)
        print(key)
        print(keylist)
    print(info)
    return info

#保存数据至CSV文件中
def save_data(info):
    headers = ['职位名称','公司名称','工作地点','薪资']
    with open('qianchengwuyou.csv','a+',encoding='UTF-8',newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        for key in info:
            writer.writerow([key['job_name'],key['company_name'],key['work_space'],key['work_pay']])

def insert(value):
    db = pymysql.connect(host='localhost',db='qianchengwuyou',user='root',password='root',charset='utf8')

    cursor = db.cursor()
    sql="insert into qiancheng values(%s,%s,%s,%s)"
    try:
        cursor.executemany(sql,value)
        db.commit()
        print('插入数据成功')
    except:
        db.rollback()
        print("插入数据失败")
    db.close()

if __name__ == '__main__':
    urls = ['https://search.51job.com/list/120200,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=%EF%BC%89'.format(i) for i in range(1,9)]
    for url in urls:
        html = get_response(url)
        info = get_html(html)
        insert(info)
        save_data(info)
        for i in info:
            print(i)
            insert(i)

