# 三种文本进度条
import time

def progress_bar_style1(scale=50):
    """
    样式1：带有百分比、进度符号和时间的进度条
    """
    print("执行开始".center(scale // 2, '-'))
    start = time.perf_counter()
    for i in range(scale + 1):
        a = '*' * i
        b = '.' * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        # 使用 f-string 格式化，更现代且易读
        print(f"\r{c:^3.0f}%[{a}->{b}]{dur:.2f}s", end='')
        time.sleep(0.1)
    print("\n" + "执行结束".center(scale // 2, '-'))

def progress_bar_style2(scale=50):
    """
    样式2：纯数字百分比进度条
    """
    print("执行开始".center(scale // 2, '-'))
    for i in range(scale + 1):
        percent = (i / scale) * 100
        print(f"\r{percent:.0f}%", end='')
        time.sleep(0.1)
    print("\n" + "执行结束".center(scale // 2, '-'))

def progress_bar_style3(scale=50):
    """
    样式3：简单的加载条，没有百分比和时间
    """
    print("执行开始".center(scale // 2, '-'))
    for i in range(scale + 1):
        loading_str = "#" * i + " " * (scale - i)
        print(f"\r[{loading_str}]", end='')
        time.sleep(0.1)
    print("\n" + "执行结束".center(scale // 2, '-'))


if __name__ == "__main__": # 推荐使用这种方式来组织主执行代码
    print("请输入需要查看的样式\n 1.列表 2.纯数字 3.加载条")
    
    # 循环直到用户输入有效选择
    while True:
        choice = input("你的选择是: ")
        if choice == '1':
            progress_bar_style1()
            break # 跳出循环
        elif choice == '2':
            progress_bar_style2()
            break
        elif choice == '3':
            progress_bar_style3()
            break
        else:
            print("输入无效，请重新输入 1、2 或 3。")

