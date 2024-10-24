import streamlit as st
import datetime

def get_day_of_week(date):
    days = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return days[date.weekday()]

st.title('誕生日の曜日アプリ')

year = st.number_input('年を入力してください', min_value=1900, max_value=2100, value=2000)
month = st.number_input('月を入力してください', min_value=1, max_value=12, value=1)
day = st.number_input('日を入力してください', min_value=1, max_value=31, value=1)

if st.button('曜日を表示'):
    try:
        date = datetime.date(year, month, day)
        day_of_week = get_day_of_week(date)
        st.success(f'{year}年{month}月{day}日は{day_of_week}です。')
    except ValueError:
        st.error('無効な日付です。正しい日付を入力してください。')