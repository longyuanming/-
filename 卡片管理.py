# -*- coding:utf-8 -*-
card=[] #全局变量
def Functional_hints():  #程序的功能提示
    '''功能提示'''
    print("1.添加")
    print("2.删除")
    print("3.修改")
    print("4.查询")
    print("5.显示所有")
    print("6.退出")
def add_to():  #添加新的卡片
    new_name=input("输入姓名：")
    new_qq=input("输入QQ号码：")
    new_weixin=input("输入微信号：")
    new_adress=input("输入家庭地址：")
    new_card={}
    new_card['name']=new_name
    new_card['QQ']=new_qq
    new_card['weixin']=new_weixin
    new_card['address']=new_adress
    global card
    card.append(new_card)
def del_card(): #对卡片进行删除
    name=input("请输入所要删除的姓名：")
    global card
    i=0
    for name_1 in card:
        i+=1
        if name in name_1['name']:
            print("已找到删除的卡片！")
            break
        else:
            print("卡片不存在")
    del card[(i-1)]
def Information_modification(): #对卡片进行修改
    name=input("请输入要修改的名字：")
    global card
    for name_2 in card:
        if name in name_2['name']:
            name_2['name']=input("请输入新的名字：")
            name_2['QQ']=input("请输入新的QQ：")
            name_2['weixin']=input("请输入新的微信：")
            name_2['address']=input("请输入新的地址：")
            print("修改成功！")
        else:
            print("信息不存在！")
def Information_Service(): #查询单个信息
    name=input("请输入要修查询的名字：")
    global card
    for name_3 in card:
        if name in name_3['name']:
            print("姓名\tQQ\t微信\t家庭地址")
            print("%s\t%s\t%s\t%s"%(name_3['name'],name_3['QQ'],name_3['weixin'],name_3['address']))
        else:
            print("查无此人")
def get_all_of_it():#查询全部信息
        i=0
        global card
        print("姓名\tQQ\t微信\t家庭地址")
        for name_3 in card:
                print("%s\t%s\t%s\t%s"%(name_3['name'],name_3['QQ'],name_3['weixin'],name_3['address']))
                i++
        if i=0
           print("数据为空")
def main():
    while True:
        number=input("请输入功能序号：")
        if number==1:
            add_to()
            print("添加成功！")
        elif number==2:
            del_card()
            print ("卡片已删除！")
        elif number==3:
            Information_modification()
        elif number==4:
            Information_Service()
        elif number==5:
            get_all_of_it()
        elif number==6:
            print("exit")
            break
Functional_hints()
main()
