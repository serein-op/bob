#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


# 建明镇=%E5%BB%BA%E6%98%8E%E9%95%87
html = getHtml("http://www.zhrczp.com/jobs/jobs_list/trade/9.html")

soup = BeautifulSoup(html, 'lxml')  # 声明BeautifulSoup对象

hrefbox = soup.find_all("div", "td-j-name", True);

links = [];
for href in range(0, len(hrefbox)):
    links.append("http://www.zhrczp.com" + hrefbox[href].contents[0].get('href'));  # 拼接链接

f = open('a.txt', 'w', encoding='utf-8')
for link in links:
    print(link);
    html = getHtml(link)
    soup = BeautifulSoup(html, 'lxml')  # 声明BeautifulSoup对象

    main = soup.find_all("div", "main", True);
    f.write("\n***************************显示招聘信息*************************************\n\n")
    f.write("职位名称:" + main[0].contents[1].contents[5].contents[1].contents[0] + "\n");  # 职位名称
    f.write("发布时间:" + main[0].contents[1].contents[3].contents[1].contents[0] + "\n");  # 发布时间
    f.write("\n--------------------职位待遇--------------------\n");
    f.write("工资:" + main[0].contents[1].contents[7].contents[0] + "\n");  # wage
    f.write("福利：");
    for i in range(1, len(main[0].contents[1].contents[9].contents) - 3):
        f.write(main[0].contents[1].contents[9].contents[i].contents[0] + " ");

    f.write("\n\n--------------------联系方式--------------------\n")
    f.write(main[0].contents[5].contents[3].contents[0].strip() + "\n");  # 联系人 去掉空格
    f.write(main[0].contents[5].contents[7].contents[0] + main[0].contents[5].contents[7].contents[1].contents[
        0] + "\n");  # 联系电话

    f.write("\n--------------------联系描述--------------------\n")
    describe = main[0].contents[7].contents;
    f.write(describe[1].contents[0] + describe[3].contents[0] + "\n");  # 职位描述

    item = soup.find_all("div", "item", True);
    f.write("\n--------------------职位要求--------------------\n");
    f.write(item[0].contents[3].contents[0].contents[0] + ":" + item[0].contents[3].contents[1] + "\n");  # 工作性质
    f.write(item[0].contents[5].contents[0].contents[0] + ":" + item[0].contents[5].contents[1] + "\n");  # 职位类别
    f.write(item[0].contents[7].contents[0].contents[0] + ":" + item[0].contents[7].contents[1] + "\n");  # 招聘人数
    f.write(item[0].contents[11].contents[0].contents[0] + ":" + item[0].contents[11].contents[1] + "\n");  # 学历要求
    f.write(item[0].contents[13].contents[0].contents[0] + ":" + item[0].contents[13].contents[1] + "\n");  # 工作经验
    f.write(item[0].contents[15].contents[0].contents[0] + ":" + item[0].contents[15].contents[1] + "\n");  # 性别要求
    f.write(item[0].contents[19].contents[0].contents[0] + ":" + item[0].contents[19].contents[1] + "\n");  # 年龄要求
    f.write(item[0].contents[21].contents[0].contents[0] + ":" + item[0].contents[21].contents[1] + "\n");  # 招聘部门
    f.write(item[0].contents[25].contents[0].contents[0] + ":" + item[0].contents[25].contents[1] + "\n");  # 招聘部门

    company = soup.find_all("div", "cominfo link_gray6", True);
    f.write("\n--------------------公司信息--------------------\n");
    f.write(company[0].contents[3].contents[1].contents[0] + "\n");  # 公司名称
    f.write(company[0].contents[5].contents[0].contents[0] + ":" + company[0].contents[5].contents[1] + "\n");  # 公司性质
    f.write(company[0].contents[7].contents[0].contents[0] + ":" + company[0].contents[7].contents[1] + "\n");  # 公司行业
    f.write(company[0].contents[9].contents[0].contents[0] + ":" + company[0].contents[9].contents[1] + "\n");  # 公司规模
    f.write(company[0].contents[11].contents[0].contents[0] + ":" + company[0].contents[11].contents[1] + "\n");  # 公司地区

    f.write("\n***************************结束招聘信息*************************************\n")
f.close();