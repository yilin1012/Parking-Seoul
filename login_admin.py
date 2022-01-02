#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:10:31 2021

@author: yerim
"""
# 파이썬 GUI  라이브러리인 tkinter 임포트 
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
import admin_parkingdata
import admin_car_inout
import admin_cardata


def open_admin_page(user_id, window) :
    
    window.destroy() # 로그인 창 닫기
    # 창 생성
    w_admin_main = Tk()
    w_admin_main.geometry('300x300') # 창 크기
    w_admin_main.title("관리자 모드 메인 화면")
    
    #라벨 생성
    l_admin_main_title = Label(w_admin_main, text = "관리자 모드 메인 화면입니다.")
    l_admin_main_title.pack()
    l_admin_user = Label(w_admin_main, text = 'current user : '+ str(user_id))
    l_admin_user.pack()
    
    b_admin1 = Button(w_admin_main, text = "주차장정보 조회/수정", command=admin_parkingdata.admin_parkingdata)
    b_admin1.pack()
    b_admin2 = Button(w_admin_main, text = "차량 입/출차", command=admin_car_inout.admin_car_inout)
    b_admin2.pack()
    b_admin3 = Button(w_admin_main, text = "차량정보 조회/수정", command=admin_cardata.admin_cardata)
    b_admin3.pack()
    
    w_admin_main.mainloop()
    

# 관리자 파일을 읽어오는 함수
def read_data():
    data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/data modify/admin_info.csv' , encoding='utf-8')
    
    return data # 관리자 파일 리턴
    

# 사용자 id와 password를 비교하는 함수
def check_data(user_id, password,w):
    
    # 파일 읽어오기
    data = read_data()

    
    print(user_id.get())
    print(password.get())
 
    try :
        # 사용자가 입력한 ID, pw가 유효하지 확인
        get_id = data[data['id'] == user_id.get()]
        print(get_id)
        get_pw = get_id[get_id['pw'] == password.get()]
        print(get_pw)
        
        # 유효한 id, pw 이면 로그인 성공
        if len(get_pw) > 0 :
             print("Logged IN Successfully")
             open_admin_page(user_id.get(),w)
             
             
        
        else : 
            # 유효하지 않은 경우 오류 팝업
            w_alert = Tk()
            w_alert.geometry('100x100')
            w_alert.title('오류 팝업')
            l_alert = Label(w_alert, text =" 아이디 혹은 비밀번호가 틀렸습니다. 다시 확인하세요. ")
            l_alert.pack()
    
    except :
        pass
            

# 관리자 모드 로그인
def login_admin() :
    w_admin = Tk()
    w_admin.geometry('300x300') # 메인 윈도우 페이지의 크기를 800x800 으로 설정.
    w_admin.title("파킹서울_관리자모드") # 메인 윈도우 페이지의 제목 : 파킹서울_메인페이지
    
    # 사용자 id와 password를 저장하는 변수 생성
    user_id, password = StringVar(), StringVar()

    # 변수 생성
    car_number = StringVar()
    parking_number = IntVar()


    # 관리자 모드 로그인 페이지 라벨
    l_admin_title = Label(w_admin, text="<파킹 서울 관리자 모드 로그인>") 
    l_admin_title.grid(column=1, row=0)
        
    l_admin_id = Label(w_admin, text="id")
    l_admin_id.grid(column=0,row=2)
        
    l_admin_pw = Label(w_admin, text="pw")
    l_admin_pw.grid(column=0, row=3)
        
    # 사용자 id 와 password를 입력 받는 곳
    input_text_1 = Entry(w_admin, textvariable = user_id, width=30) 
    input_text_1.grid(column=1, row=2) 
    input_text_2 = Entry(w_admin, textvariable = password, width=30)
    input_text_2.config(show = "*")   # 입력되는 것을 *로 보이게 하기 
    input_text_2.grid(column=1, row=3)
        
    button = Button(w_admin, text="로그인", command = lambda:check_data(user_id, password,w_admin))
    button.grid(column=1, row=4)


    w_admin.mainloop()

#login_admin()