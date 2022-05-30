#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tkinter as tk
import requests
import json
import datetime

#OpenWeatherサイトで入手したAPIキーを入力
API_key = ""

#メインウインドウ作成
canvas = tk.Tk()
canvas.geometry("500x500")    #ウインドウサイズ
canvas.title("Today's Weather")    #アプリ名
a = ("Arial black", 20, "bold")    #最高・最低気温を表す文字フォント
b = ("Arial black", 40)    #都市入力・天気の結果を表すフォント

canvas.config(bg = 'silver')  #ウインドウ設定

frame1 = tk.Frame(canvas, bg = 'silver', pady=20)  #都市名入力フレーム
frame2 = tk.Frame(canvas, height=350, width=400, bd=5, relief="ridge")  #気象情報を表示するフレームの外枠
frame3 = tk.Frame(frame2)  #気象情報を表示するフレーム

#お天気情報を得るためのgetWeather関数
def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_key+"&lang=ja"
    
    json_data = requests.get(api).json()
    weather = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)    #摂氏表記に変更
    min_temp = int(json_data['main']['temp_min'] - 273.15)    #最低気温(摂氏)
    max_temp = int(json_data['main']['temp_max'] - 273.15)    #最高気温(摂氏)
    
    #【追加部分】都市の時間
    city_time = datetime.datetime.fromtimestamp(int(json_data['dt']))
    
    #アプリに表示する項目
    final_info = weather + "\n" + str(temp) + "℃"
    final_data = "\n" + "最低気温:" + str(min_temp) + "℃" + "\n" + "最高気温:" + str(max_temp) + "℃"
    label1.config(text = city_time)　   #【追加部分】
    label2.config(text = final_info)
    label3.config(text = final_data)
    
#テキストボックス作成
textField = tk.Entry(master=frame1, justify='center', width = 15, font = b)
textField.pack()
textField.bind('<Return>', getWeather)    #APIの天気情報を返す（表示）

frame1.pack()     #【追加部分】
frame2.pack()     #【追加部分】
frame3.place(x=75, y=50) 　   #【追加部分】

label1 = tk.Label(frame3, font = a)
label1.pack()
label2 = tk.Label(frame3, font = b)
label2.pack()
label3 = tk.Label(frame3, font = a) 　   #【追加部分】
label3.pack() 　   #【追加部分】

canvas.mainloop()    #canvasをウインドウに待機


# In[ ]:




