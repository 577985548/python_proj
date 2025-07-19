import random
def guess_number_game():
    print("欢迎来玩猜数字游戏！数字范围是1-100，我会提示你猜大了还是小了，直到猜对为止。")
    number = random.randint(1, 100)
    guess_count = 0
    while True:
        try: 
            guess = int(input("请输入你的猜测："))
            if guess == number:
                print("恭喜你猜对了！")
                print(f"你一共猜了{guess_count}次")
                break
            elif guess > number:
                print("猜大了")
                guess_count += 1
            else:
                print("猜小了")
                guess_count += 1
        except ValueError:
            print("输入错误")
    print("游戏结束！")

if __name__ == "__main__":
    guess_number_game()
