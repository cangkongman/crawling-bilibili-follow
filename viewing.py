import json
import os
import xlwt
import re


def viewing(path):
    alignment = xlwt.Alignment()
    style = xlwt.XFStyle()

    alignment.wrap = 1
    alignment.horz = 2
    alignment.vert = 1

    style.alignment = alignment

    filename = os.listdir(path)
    work = xlwt.Workbook(encoding='utf-8', style_compression=2)
    sht = work.add_sheet('关注者列表')
    # 设置冻结为真
    sht.set_panes_frozen('1')
    # 水平冻结
    sht.set_horz_split_pos(1)

    sht.write(0, 3, 'Up Name', style)
    sht.write(0, 4, 'Up Uid', style)
    sht.write(0, 5, 'Up Sign', style)

    sht.col(3).width = 6666
    sht.col(4).width = 3333
    sht.col(5).width = 9999

    num = 1

    for i in filename:
        if not(re.search("json", i)):
            continue
        os.chdir(path)
        with open(i, 'r', encoding='utf-8')as fp:
            file = json.load(fp)
        data = file['data']
        ups = data['list']
        for j in ups:
            sht.write(num, 3, j['uname'], style)
            sht.write(num, 4, j['mid'], style)
            sht.write(num, 5, j['sign'], style)
            print(str(num) + j['uname'])
            num += 1

    work.save('关注者列表.xlsx')
    print('录入完毕！！！')
