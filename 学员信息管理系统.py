# -*- coding: utf-8 -*-

student = []


def add_man():
    stu = raw_input("请输入名字")
    student.append(stu)


def edit_man():
    point = input("请输入查找的学号")
    student[point] = raw_input("请输入名字")


def sea_man():
    ty = input("1.序号查询       2.所有学员")
    if ty == 1:
        point = input("请输入查找的学号")
        print "此人名字是：", student[point]
    else:
        for i in range(len(student)):
            print "此人序号：", i+1, "此人名字：", student[i]


def del_man():
    point = input("请输入删除的学号")
    for i in range(point, len(student)):
        student[i] = student[i+1]
    print "删除成功"


def main():
    while 1:
        print "------学员信息管理系统------"
        print "1>添加学员        2>修改学员"
        print "3>查询学员        4>删除学员"
        print "----------0>退出----------"
        cho = input("请输入命令：")
        if cho == 0:
            exit(0)
        elif cho == 1:
            add_man()
        elif cho == 2:
            edit_man()
        elif cho == 3:
            sea_man()
        elif cho == 4:
            del_man()


main()
