#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:10:44 2021

@author: yerim
"""

# 파이썬 GUI  라이브러리인 tkinter 임포트 
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd


def search_gu(gu) :
    
    # 표를 채우는데 필요한 데이터 뽑아내기
    def gu_list(gu) :
    
        # 주차장 정보 파일 열기
        data = pd.read_csv("/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv", encoding="euc-kr")
        
        # 파일에서 '구' 속성이 gu인 것 추출
        data = data[data['구']== gu]
        
        # 출력하고자 하는 리스트 
        gu_list = []
        subset= data[['행정동','주차장명', '주소', '총 주차면', '주차장코드']]
     
        gu_list = [tuple(x) for x in subset.to_numpy()]

    
        return gu_list
    
    # 체크박스를 위한 데이터 뽑아내기
    def dong_list(gu) :
        
        # 주차장 정보 파일 열기
        data = pd.read_csv("/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv", encoding="euc-kr")
        
        # 파일에서 '구' 속성이 gu인 것 추출
        data = data[data['구']== gu]
        
        dong_list = data['행정동'].unique()
        
        return dong_list
    

    # 선택한 checkbox 뽑아내기
    def is_checked(i) :
        print("CheckVariet_", i , " : ", CheckVariety_i.get())
    
  
    #구 기준으로 주차장 조회 하는 페이지 생성
    w_search_gu = Tk() # 구를 기준으로 주차장 조회하는 결과 윈도우 명 : w_search_gu
    w_search_gu.geometry('800x800')
    w_search_gu.title("파킹서울_주차장 조회 페이지") # 주차장 찾기 조회 결과 상세

    # 라벨 1 : 구 이름
    l_gu_name = Label(w_search_gu, text=gu)
    l_gu_name.grid(column=1, row=0)  
    
    # 프레임 생성
    f_search_gu_1=Frame(w_search_gu, width=800, height = 200)
    f_search_gu_1.grid(column=1, row=1)
    
    
    treeview=ttk.Treeview(f_search_gu_1, columns=["행정동","주차장명", "주소", "총 주차면", "주차장코드"], 
                                  displaycolumns=["행정동","주차장명", "주소", "총 주차면", "주차장코드"])
    treeview.pack()
    

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("행정동" ,width=50, anchor="center")
    treeview.heading("행정동", text="행정동", anchor="center")

    treeview.column("주차장명", width=150, anchor="center")
    treeview.heading("주차장명", text="주차장명", anchor="center")

    treeview.column("주소", width=200, anchor="center")
    treeview.heading("주소", text="주소", anchor="center")

    treeview.column("총 주차면", width=50, anchor="center")
    treeview.heading("총 주차면", text="총 주차면", anchor="center")
    
    treeview.column("주차장코드", width=50, anchor="center")
    treeview.heading("주차장코드", text="주차장코드", anchor="center")
    
    # 테이블 스크롤바 표시 
    scroll = ttk.Scrollbar(f_search_gu_1, orient="vertical", command=treeview.yview) 
    scroll.pack(side='right', fill='y') 
    treeview.configure(yscrollcommand=scroll.set)

    # 표에 삽입될 데이터
    treelist = gu_list(gu)
    

    #프레임 생성
    f2 = Frame(w_search_gu)
    f2.grid(column=0, row=1)
    f3 = Frame(w_search_gu)
    f3.grid(column=1, row=2)
    
    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i)+"번")
    
    # 체크박스를 구의 행정동 갯수만큼 만들기
    dong_list = dong_list(gu)
    for i , dong in enumerate(dong_list) :
        CheckVariety_i = IntVar()
        
        checkbutton_i = Checkbutton(f2, text=dong, variable=CheckVariety_i, command=lambda:is_checked(i))
        
        checkbutton_i.pack()

    
    # 라벨 2 : 구체적인 값을 출력 할 영역
    l_value_1 = Label(f3, text=" ")
    l_value_1.pack()
    l_value_2 = Label(f3, text=" ")
    l_value_2.pack()
    l_value_3 = Label(f3, text=" ")
    l_value_3.pack()
    l_value_4 = Label(f3, text=" ")
    l_value_4.pack()
    l_value_5 = Label(f3, text=" ")
    l_value_5.pack()
    l_value_6 = Label(f3, text=" ")
    l_value_6.pack()
    l_value_7 = Label(f3, text=" ")
    l_value_7.pack()
    l_value_8 = Label(f3, text=" ")
    l_value_8.pack()
    l_value_9 = Label(f3, text=" ")
    l_value_9.pack()
    l_value_10 = Label(f3, text=" ")
    l_value_10.pack()
    l_value_11 = Label(f3, text=" ")
    l_value_11.pack()
    l_value_12 = Label(f3, text=" ")
    l_value_12.pack()
    l_value_13 = Label(f3, text=" ")
    l_value_13.pack()
    

    
    
    # 테이블 항목 클릭시 click_item 호출 
    def click_item(event): 
        
        # 클릭한 항목
        selectedItem = treeview.focus() 
        
        # 클릭한 항목의 "주차장코드"만 추출
        selectedItem_code = treeview.item(selectedItem).get('values')[4]
        
        # 주차장 정보 파일 열기
        data = pd.read_csv("/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv", encoding="euc-kr")
        
        # 차량 정보 파일 열기
        data2 = pd.read_csv("/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv", encoding="euc-kr")
        
        # 파일에서 '주차장코드' 속성이 selectedItem_code인 것 추출 (PK임)
        data = data[data['주차장코드'] == selectedItem_code]
        data2 = data2[data2['주차장코드'] == selectedItem_code]

        # 상세 값
        value_1 = "행정동 : " + str(data['행정동'].values[0])
        value_2 = "주차장명 : " + str(data['주차장명'].values[0])
        value_3 = "주소 : " + str(data['주소'].values[0])
        value_4 = "주차장 종류명 : " + str(data['주차장 종류명'].values[0])
        value_5 = "운영 구분 : " + str(data['운영구분명'].values[0])
        value_6 = "유 무료 여부 : " + str(data['유무료구분명'].values[0])
        value_7 = "평일 운영 시간 : " + str(data['평일 운영 시작시각(HHMM)'].values[0]) + "  ~  " + str(data['평일 운영 종료시각(HHMM)'].values[0]) 
        value_8 = "기본 주차 요금 : " + "기본" + str(data['기본 주차 시간(분 단위)'].values[0]) + "분" + "     " + str(data['기본 주차 요금'].values[0]) + "원"
        value_9 = "추가 요금 : " + str(data['추가 단위 시간(분 단위)'].values[0]) + " 분 당 " + "     " + str(data['추가 단위 요금'].values[0]) + "원"
        value_10 = "일 최대 : " + str(data['일 최대 요금'].values[0])
        value_11 = "문의 전화 : " + str(data['전화번호'].values[0])
        value_12 = "총 주차면 : "  + str(data['총 주차면'].values[0])
        value_13 = "이용중 : " + str(len(data2)) + ", 주차 가능 : " + str(data['총 주차면'].values[0] - len(data2))
        
        
        # 라벨 내용 바꾸어 출력하기
        l_value_1.configure(text=value_1)
        l_value_2.configure(text=value_2)
        l_value_3.configure(text=value_3)
        l_value_4.configure(text=value_4)
        l_value_5.configure(text=value_5)
        l_value_6.configure(text=value_6)
        l_value_7.configure(text=value_7)
        l_value_8.configure(text=value_8)
        l_value_9.configure(text=value_9)
        l_value_10.configure(text=value_10)
        l_value_11.configure(text=value_11)
        l_value_12.configure(text=value_12)
        l_value_13.configure(text=value_13)

        
    
    treeview.bind('<ButtonRelease-1>', click_item)

    
    # GUI 실행
    w_search_gu.mainloop()


def open_search_window() :
    #w_main.destroy() # 메인 페이지 닫기

    # 주차장 찾기 페이지 생성
    w_search = Tk() # 주차장 찾기 페이지의 윈도우 명 : w_search
    w_search.geometry('800x800') # 주차장 찾기 페이지의 크기를 800x800 으로 설정.
    w_search.title("파킹서울_주차장 조회 페이지") # 주차장 찾기 페이지의 제목 : 파킹서울_주차장 조회 페이지
    

    # 주차장 찾기 페이지 프레임 생성
    f_search_1=Frame(w_search, width=800, height = 100)
    f_search_1.pack()
    f_search_2=Frame(w_search, width=800, height = 600)
    f_search_2.pack()
    f_search_3=Frame(w_search, width=800, height = 100)
    f_search_3.pack()
    
    #주차장 찾기 페이지 라벨
    l_search_title = Label(f_search_1, text="조회하고 싶은 구를 선택하세요.")
    l_search_title.pack()
    
    #주차장 찾기 페이지  버튼 생성
    
    # 구 선택 버튼 
    # tkinter 의 button command 옵션으로 인수를 전달하고자 할 때는 lambda 함수를 사용한다.
    b_search_1 = Button(f_search_2, text="강남구" ,width=5, command=lambda:search_gu('강남구') )
    b_search_1.grid(row=0, column=0)
    
    b_search_2 = Button(f_search_2, text="강동구" ,width=5, command=lambda:search_gu('강동구') )
    b_search_2.grid(row=0, column=1)
    
    b_search_3 = Button(f_search_2, text="강서구" ,width=5, command=lambda:search_gu('강서구') )
    b_search_3.grid(row=0, column=2)
    
    b_search_4 = Button(f_search_2, text="강북구" ,width=5, command=lambda:search_gu('강북구') )
    b_search_4.grid(row=0, column=3)
    
    b_search_5 = Button(f_search_2, text="관악구" ,width=5, command=lambda:search_gu('관악구') )
    b_search_5.grid(row=0, column=4)
    
    b_search_6 = Button(f_search_2, text="광진구" ,width=5, command=lambda:search_gu('광진구') )
    b_search_6.grid(row=1, column=0)
    
    b_search_7 = Button(f_search_2, text="구로구" ,width=5, command=lambda:search_gu('구로구') )
    b_search_7.grid(row=1, column=1)
    
    b_search_8 = Button(f_search_2, text="금천구" ,width=5, command=lambda:search_gu('금천구') )
    b_search_8.grid(row=1, column=2)
    
    b_search_9 = Button(f_search_2, text="노원구" ,width=5, command=lambda:search_gu('노원구') )
    b_search_9.grid(row=1, column=3)
    
    b_search_10 = Button(f_search_2, text="동대문구" ,width=5, command=lambda:search_gu('동대문구') )
    b_search_10.grid(row=1, column=4)
    
    b_search_11 = Button(f_search_2, text="도봉구" ,width=5, command=lambda:search_gu('도봉구') )
    b_search_11.grid(row=2, column=0)
    
    b_search_12 = Button(f_search_2, text="동작구" ,width=5, command=lambda:search_gu('동작구') )
    b_search_12.grid(row=2, column=1)
    
    b_search_13 = Button(f_search_2, text="마포구" ,width=5, command=lambda:search_gu('마포구') )
    b_search_13.grid(row=2, column=2)
    
    b_search_14 = Button(f_search_2, text="서대문구" ,width=5, command=lambda:search_gu('서대문구') )
    b_search_14.grid(row=2, column=3)
    
    b_search_15 = Button(f_search_2, text="성동구" ,width=5, command=lambda:search_gu('성동구') )
    b_search_15.grid(row=2, column=4)
    
    b_search_16 = Button(f_search_2, text="성북구" ,width=5, command=lambda:search_gu('성북구') )
    b_search_16.grid(row=3, column=0)
    
    b_search_17 = Button(f_search_2, text="서초구" ,width=5, command=lambda:search_gu('서초구') )
    b_search_17.grid(row=3, column=1)
    
    b_search_18 = Button(f_search_2, text="송파구" ,width=5, command=lambda:search_gu('송파구') )
    b_search_18.grid(row=3, column=2)
    
    b_search_19 = Button(f_search_2, text="영등포구" ,width=5, command=lambda:search_gu('영등포구') )
    b_search_19.grid(row=3, column=3)
    
    b_search_20 = Button(f_search_2, text="용산구" ,width=5, command=lambda:search_gu('용산구') )
    b_search_20.grid(row=3, column=4)
    
    b_search_21 = Button(f_search_2, text="양천구" ,width=5, command=lambda:search_gu('양천구') )
    b_search_21.grid(row=4, column=0)
    
    b_search_22 = Button(f_search_2, text="은평구" ,width=5, command=lambda:search_gu('은평구') )
    b_search_22.grid(row=4, column=1)
    
    b_search_23 = Button(f_search_2, text="종로구" ,width=5, command=lambda:search_gu('종로구') )
    b_search_23.grid(row=4, column=2)
    
    b_search_24 = Button(f_search_2, text="중구" ,width=5, command=lambda:search_gu('중구') )
    b_search_24.grid(row=4, column=3)
    
    b_search_25 = Button(f_search_2, text="중랑구" ,width=5, command=lambda:search_gu('중랑구') )
    b_search_25.grid(row=4, column=4)
    
    

    
    w_search.mainloop()

#open_search_window()