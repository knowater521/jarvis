import os


def run(driver,data):
    sum = eval(data[0])
    print("计算结果为：{}".format(sum))
    os.system('say "计算结果为：{}"'.format(sum))
