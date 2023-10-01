from db_config import WeightManege


def main():
    user_name = input("ユーザー名を入力してください > ")

    weight = input("体重を入力してください > ")

    WeightManege.create(name=user_name, weight=weight)

    for msg in WeightManege.select():
        # print(f"{msg.id} {msg.user} {msg.content} {msg.pub_date}")
        # 今回の表示なら以下でもOK
        # print(msg.id, msg.user, msg.content, msg.pub_date)


if __name__ == "__main__":
    main()