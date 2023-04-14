import random

# 1. ランダムな数字を生成する
answer = random.randint(1, 100)
guess = 0
guess_count = 0

# 2. プレイヤーに数字を入力してもらう
while guess != answer:
    guess = int(input("1から100までの数字を入力してください："))
    guess_count += 1

    # 3. 入力された数字をチェックする
    if guess < answer:
        print("もっと大きな数字です")
    elif guess > answer:
        print("もっと小さな数字です")
    else:
        print("正解！{}回で当てました".format(guess_count))
