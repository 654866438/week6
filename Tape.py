import os,sys

def mergeData(L):
    """合并数据"""
    max_length = 0#找出最长的子列表
    for i in L:
        i_length = len(i)
        if i_length > max_length:
            max_length = i_length

    #补齐较短的列表：
    newL = []
    for i in L:
        i_length = len(i)
        if i_length < max_length:
            i.extend(["    "]*(max_length - i_length))
        newL.append(i)

    for i in zip(*newL):
        print("\t".join(i))
    

def readTextFile(filePath):
    """读取文本文件"""
    f = open(filePath, "r")
    data_list = f.read().splitlines()#splitlines()将文本内容按行存入一个列表
    f.close()
    return data_list
    

def main():
    """主函数"""
    parameter_list = sys.argv
    length = len(parameter_list)

    #print(parameter_list)

    if length > 1:#判断正确的命令格式
        L = []
        for i in parameter_list[1:]:
            if os.path.exists(i):#判断有效的文件：
                L.append(readTextFile(i))
            else:
                print("Unable to load file {}".format(i))
                
        mergeData(L)#合并
        

if __name__ == "__main__":
    main()

