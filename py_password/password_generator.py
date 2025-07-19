"""
项目 7：密码生成器
目标：生成指定长度的随机密码（包含字母、数字、特殊字符）。
功能要求：
用户输入密码长度。
随机组合字符生成密码。
可选择是否包含特殊字符。
核心知识点：字符串操作、随机选择（random.choice）。
"""
import random
import string

def generate_password(length, include_special=True):
    """
    生成指定长度的密码
    :param length: 密码长度
    :param include_special: 是否包含特殊字符
    :return: 生成的密码
    """
    # 密码字符集
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation
        # 添加特殊字符

    # 随机选择字符生成密码
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    length = int(input("请输入密码长度："))
    include_special = input("是否包含特殊字符？（是/否）").lower() == "是"

    password = generate_password(length, include_special)
    print(f"生成的密码是：{password}")
if __name__ == "__main__":
    main()  
