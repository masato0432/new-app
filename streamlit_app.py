from datetime import datetime

def get_weekday_of_birthday():
    # ユーザーに誕生日を入力してもらう
    birthday_input = input("誕生日を入力してください（YYYY-MM-DD形式）: ")

    try:
        # 入力された文字列をdatetimeオブジェクトに変換
        birthday = datetime.strptime(birthday_input, "%Y-%m-%d")
        
        # 曜日の名前を取得
        weekday_name = birthday.strftime("%A")
        
        # 結果を表示
        print(f"あなたの誕生日は {weekday_name} です。")
    except ValueError:
        print("無効な日付形式です。正しい形式で入力してください。")

if __name__ == "__main__":
    get_weekday_of_birthday()