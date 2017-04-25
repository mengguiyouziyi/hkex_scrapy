# coding:utf-8
import codecs
import os
import os.path

root_folder = os.getcwd()
for parent, dirnames, filenames in os.walk(root_folder):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dirname in dirnames:  # 输出文件夹信息
        print("parent is:" + parent)
        print("dirname is:" + dirname)
    for filename in filenames:  # 输出文件信息
        print("parent is:" + parent)
        print("filename is:" + filename)
        print("the full name of the file is:" + os.path.join(parent, filename))

