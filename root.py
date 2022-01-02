#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:36:23 2021

@author: yerim
"""


# =============================================================================
# 필요 모듈 Import
# =============================================================================

# 파이썬 GUI  라이브러리인 tkinter 임포트 
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
import open_search_window
import open_charge_window
import login_admin


# =============================================================================
# 메인 페이지
# =============================================================================


# 메인 페이지 윈도우 생성
w_main = Tk() # 메인페이지의 윈도우 명 : w_main
w_main.geometry('300x300') # 메인 윈도우 페이지의 크기를 800x800 으로 설정.
w_main.title("파킹서울_메인페이지") # 메인 윈도우 페이지의 제목 : 파킹서울_메인페이지

# 이미지로드
photo = PhotoImage(file="/Users/yerim/Desktop/parkingseoul/img/manager.png")



# 메인 페이지 라벨
l_main_title = Label(w_main, text="<파킹 서울>") 
l_main_title.pack()


# 메인 페이지 버튼
b_main_1 = Button(w_main, text="주차장 찾기", command=open_search_window.open_search_window)
b_main_1.pack()
b_main_2 = Button(w_main, text="주차 요금 조회 / 결제", command=open_charge_window.open_charge_window)
b_main_2.pack()
b_main_3 = Button(w_main, image=photo, command=login_admin.login_admin)
b_main_3.pack()



#w_main.mainloop()

