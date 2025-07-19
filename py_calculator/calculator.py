def add(x,y):
    return x+y
"""
加法函数
"""
def sub(x,y):
    return x-y 
"""
减法函数
"""
def mul(x,y):
    return x*y
"""
乘法函数
"""
def div(x,y):
    return x/y  
"""
除法函数
"""
def calculate():
    while True:
        try:
            #提示用户输入第一个数字
            num1 = float(input("请输入第一个数字："))
            operator = input("请输入运算符(+/-/*//)：")
            num2 = float(input("请输入第二个数字："))
            if operator == '+':
                result = add(num1,num2)
            elif operator == '-':
                result = sub(num1,num2)
            elif operator == '*':
                result = mul(num1,num2)
            elif operator == '/':
                result = div(num1,num2)
            else:
                print("输入错误")
                continue
            print(f"计算结果：{num1} {operator} {num2} = {result}")
            choice = input("是否继续计算？(输入y继续，其他键退出)：")
            if choice.lower() != 'y':
                break

        except ValueError:
            print("输入错误")
        except ZeroDivisionError:
            print("除数不能为零")

        if choice != 'y':
            break
    print("感谢使用")
if __name__ == '__main__':
        calculate()
        # 运行程序