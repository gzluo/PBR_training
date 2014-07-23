import sys

def read_print_file(filename):
    for line in open(filename):
        print line,
#------END read_print_file--------------------------

#main函数及其调用部分是我个人写程序的固定格式，照搬就可以
def main(): #一般主程序会包含在main函数中，在文件的最后调用main函数即可运行程序
    if len(sys.argv) < 2:  #如果命令行参数不足两个，则提示操作
        print >>sys.stderr, "Usage: python %s filename" % sys.argv[0] #一般提示信息输出到标准错误
        sys.exit(0)
    file = sys.argv[1]
    read_print_file(file)
#--------END main------------------
if __name__ == '__main__': #这句话是说只有次文件被执行时才调用main函数。如果这个文件被其它文件调用，则不执行main函数。
    main()