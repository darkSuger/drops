# coding=utf-8

while True:
    a = int(input('请输入公里数'))
    if a <= 0:
        print "请输入正确的公里数！"
        exit(0)
    a = a-2
    if a <= 0:
        print "付费8块"
        continue
    b = a-10
    if b <= 0:
        c = 8+a*1.2
        print "付费", c, "元"
        continue
    else:
        print "付费", 8+1.2*10+b*1.5, "元"
