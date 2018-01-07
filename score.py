#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = input("请输入姓名：")
score1 = float(input("please input your score of last year:"))
score2 = float(input("please input your score of this year:"))

tmp =(score2-score1)/score1*100
print("成绩变化：%.2f %%" % tmp)
if tmp > 0:
    print('hello,今年%s的成绩提高了%.2f%%' %(name,tmp))
else:
    print('hello,今年%s的成绩降低了%.2f%%' %(name,-tmp))
