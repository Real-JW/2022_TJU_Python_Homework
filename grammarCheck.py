import re

file = 'main.py'

def check(file):
    f = open(file, encoding="utf-8") # 返回一个文件对象
    line = f.readline() # 调用文件的 readline()方法
    i = 1
    wrong = 0
    while line:   
        if "for" in line:
            matchObj = re.match('^(\s*)(.*)(for)(\s*)(.*?)(\s*)(in)(\s*)(.*?)[:]$', line)
            if matchObj == None:
                print("第",i,"行有错误",line, end = '')
                wrong += 1
        if "if" in line:
            matchObj = re.match('^(\s*)(.*)(if)(\s*)(.*?)(\s*)(==|!=|<=|>=|<|>)(\s*)(.*?)[:]$', line)
            if matchObj == None:
                print("第",i,"行有错误",line, end = '')
                wrong += 1
        if "try" in line:
            matchObj = re.match('^(\s*)(.*)(try)(.*?)[:]$', line)
            if matchObj == None:
                print("第",i,"行有错误",line, end = '')
                wrong += 1
            while line:
                if "except" in line:
                    matchObj = re.match('^(\s*)(.*)(except)(.*?)[:]$', line)
                    if matchObj == None:
                        print("第",i,"行有错误",line, end = '')
                        wrong += 1
                    break
                i=i+1
                line = f.readline()
        i=i+1
        line = f.readline()
    return wrong

def getResult(wrong):
    if wrong == 0:
        print("程序正常运行")
    else:
        print("请修改程序中的错误")

def grammarCheck():
    print("Check",file)
    wrong = check(file)
    getResult(wrong)

if __name__ == '__main__':
    grammarCheck()
