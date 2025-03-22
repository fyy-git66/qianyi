import random

WORDS = [
    "RimWrold",
    "NierAutomatic",
    "Knight",
    "EldenRing",
    "Cyberpunk"
    ]

def guess():
    #抽取一个单词，并随机其抽取单词的位置
    result = random.choice(WORDS)
    #res2 = random.randint(1,len(result))
    jumble = []
    jumble.append(result)

    #将单词打乱成字符，方便打乱
    char_ch = [char for x in jumble for char in x]
    
    #猜词
    random.shuffle(char_ch)
    #join函数拼接单个字符
    jumble_plus = "".join(char_ch)
    print(jumble_plus)

    #异常模块，在输入错误后，令程序继续运行
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            #基础错误判断
            guess = input("请输入单词：")
            if not guess:
                raise ValueError("\n请不要空输入！")
            if not guess.isalpha():
                raise ValueError("\n输入必须是字母！")

            #正确判断及错误提示
            if guess == result:
                print("恭喜你猜出正确答案")
                break
            else:
                print
                attempts += 1
                print(f"答案错误,你还有{max_attempts - attempts}次机会")
        except ValueError as e:
            print(f"请再试一次{e}")
            attempts += 1
            print(f"你还有{max_attempts - attempts}次机会")
    if attempts == max_attempts:
        print("机会用光，游戏失败")
guess()

#异常模块，在输入错误后，令程序继续运行
#捕获所有异常
##try:
##    print(guess())
##except Exception as e:
##    print(e)



    

















    
    
