import os
import re

"""
跟模式匹配遍历目录中所有文件
"""
prog = re.compile('(\w*)\.py')

def ls(root=""):
    rootDir = root
    if len(rootDir) == 0 :
        print("root dir is empty %s" % os.getcwd())
        rootDir = os.getcwd()

    for lists in os.listdir(rootDir): 
        if prog.fullmatch(lists) != None:
            # todo: handle the file
            print (lists) 

        path = os.path.join(rootDir, lists) 
        if os.path.isdir(path): 
            ls(path) 


ls();
os.system("pause");
