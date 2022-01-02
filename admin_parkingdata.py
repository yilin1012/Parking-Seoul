#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:21:53 2021

@author: yerim
"""

# =============================================================================
# 필요 모듈 Import
# =============================================================================

# 파이썬 GUI  라이브러리인 tkinter 임포트 
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
import time

def create_parking(window):
    
    
    def save(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22) :
        
        data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv', encoding='euc-kr')
        
        now = time.localtime()
        col_now = "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        new = pd.DataFrame({'주차장코드':[c1.get()],'주차장명':[c2.get()],'주소':[c3.get()],'주차장 종류':[c4.get()],
                  '주차장 종류명':[c5.get()],'운영구분':[c6.get()],'운영구분명':[c7.get()],'전화번호':[c8.get()],
                  '총 주차면':[c9.get()],'유무료구분':[c10.get()],'유무료구분명':[c11.get()],'야간무료개방여부':[c12.get()],
                  '야간무료개방여부명':[c13.get()],'평일 운영 시작시각(HHMM)':[c14.get()],'평일 운영 종료시각(HHMM)':[c15.get()],
                  '최종데이터 동기화 시간':[col_now],'기본 주차 요금':[c16.get()] ,'기본 주차 시간(분 단위)':[c17.get()],'추가 단위 요금':[c18.get()],
                  '추가 단위 시간(분 단위)':[c19.get()],'일 최대 요금':[c20.get()],'구':[c21.get()],'행정동':[c22.get()]})
        
        # 만일 주차장 코드가 겹치면, 해당 데이터를 수정하는 것
        modify = data[data['주차장코드'] == c1.get()]
        
        
        # 만일 주차장 코다가 겹치지 않는다면, 새로운 주차장 데이터를 추가하는 것
        if len(modify) < 1 :
    
            new_data = pd.concat([data, new], axis=0)
            new_data.to_csv('/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv', index=False, encoding='euc-kr')
        
        else :
            idx = data[data['주차장코드'] == c1.get()].index
            data = data.drop(idx)
            new_data = pd.concat([data, new], axis=0)
            new_data.to_csv('/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv', index=False, encoding='euc-kr')
            
    
    v1,v2, v3,v4, v5 = IntVar(), StringVar(), StringVar(), StringVar(), StringVar()
    v6,v7,v8,v9,v10 = IntVar(), StringVar(), StringVar(), IntVar(), StringVar()
    v11,v12,v13,v14,v15 = StringVar(), StringVar(), StringVar(), IntVar(), IntVar()
    v16,v17,v18,v19,v20 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
    v21,v22 = StringVar(), StringVar()
    

    f1 = Frame(window)
    f1.grid(column=2,row=5)
    
    l_1 = Label(f1, text='주차장코드', width=15)
    l_1.grid(column=0, row=3)
    e_1 = Entry(f1, textvariable = v1, width = 15)
    e_1.grid(column=1, row=3)
    
    l_2 = Label(f1, text='주차장명')
    l_2.grid(column=0, row=4)
    e_2 = Entry(f1, textvariable = v2, width = 15)
    e_2.grid(column=1, row=4)
    
    l_3 = Label(f1, text='주소')
    l_3.grid(column=0, row=5)
    e_3 = Entry(f1, textvariable = v3, width = 15)
    e_3.grid(column=1, row=5)
    
    l_4 = Label(f1, text='주차장 종류')
    l_4.grid(column=0, row=6)
    e_4 = Entry(f1, textvariable = v4, width = 15)
    e_4.grid(column=1, row=6)
    
    l_5 = Label(f1, text='주차장 종류명')
    l_5.grid(column=0, row=7)
    e_5 = Entry(f1, textvariable = v5, width = 15)
    e_5.grid(column=1, row=7)
    
    l_6 = Label(f1, text='운영구분')
    l_6.grid(column=0, row=8)
    e_6 = Entry(f1, textvariable = v6, width = 15)
    e_6.grid(column=1, row=8)
    
    l_7 = Label(f1, text='운영구분명')
    l_7.grid(column=0, row=9)
    e_7 = Entry(f1, textvariable = v7, width = 15)
    e_7.grid(column=1, row=9)
    
    l_8 = Label(f1, text='전화번호')
    l_8.grid(column=0, row=10)
    e_8 = Entry(f1, textvariable = v8, width = 15)
    e_8.grid(column=1, row=10)
    
    l_9 = Label(f1, text='총 주차면')
    l_9.grid(column=0, row=11)
    e_9 = Entry(f1, textvariable = v9, width = 15)
    e_9.grid(column=1, row=11)
    
    l_10 = Label(f1, text='유무료구분')
    l_10.grid(column=0, row=12)
    e_10 = Entry(f1, textvariable = v10, width = 15)
    e_10.grid(column=1, row=12)
    
    l_11 = Label(f1, text='유무료구분명')
    l_11.grid(column=0, row=13)
    e_11 = Entry(f1, textvariable = v11, width = 15)
    e_11.grid(column=1, row=13)
    
    l_12 = Label(f1, text='야간무료개방여부')
    l_12.grid(column=2, row=3)
    e_12 = Entry(f1, textvariable = v12, width = 15)
    e_12.grid(column=3, row=3)
    
    l_13 = Label(f1, text='야간무료개방여부명')
    l_13.grid(column=2, row=4)
    e_13 = Entry(f1, textvariable = v13, width = 15)
    e_13.grid(column=3, row=4)
    
    l_14 = Label(f1, text='평일 운영 시작시각(HHMM)')
    l_14.grid(column=2, row=5)
    e_14 = Entry(f1, textvariable = v14, width = 15)
    e_14.grid(column=3, row=5)
    
    l_15 = Label(f1, text='평일 운영 종료시각(HHMM)')
    l_15.grid(column=2, row=6)
    e_15 = Entry(f1, textvariable = v15, width = 15)
    e_15.grid(column=3, row=6)
    
    l_16 = Label(f1, text='기본 주차 요금')
    l_16.grid(column=2, row=7)
    e_16 = Entry(f1, textvariable = v16, width = 15)
    e_16.grid(column=3, row=7)
    
    l_17 = Label(f1, text='기본 주차 시간(분 단위)')
    l_17.grid(column=2, row=8)
    e_17 = Entry(f1, textvariable = v17, width = 15)
    e_17.grid(column=3, row=8)
    
    l_18 = Label(f1, text='추가 단위 요금')
    l_18.grid(column=2, row=9)
    e_18 = Entry(f1, textvariable = v18, width = 15)
    e_18.grid(column=3, row=9)
    
    l_19 = Label(f1, text='추가 단위 시간(분 단위)')
    l_19.grid(column=2, row=10)
    e_19 = Entry(f1, textvariable = v19, width = 15)
    e_19.grid(column=3, row=10)
    
    l_20 = Label(f1, text='일 최대 요금')
    l_20.grid(column=2, row=11)
    e_20 = Entry(f1, textvariable = v20, width = 15)
    e_20.grid(column=3, row=11)
    
    l_21 = Label(f1, text='구')
    l_21.grid(column=2, row=12)
    e_21 = Entry(f1, textvariable = v21, width = 15)
    e_21.grid(column=3, row=12)
    
    l_22 = Label(f1, text='행정동')
    l_22.grid(column=2, row=13)
    e_22 = Entry(f1, textvariable = v22, width = 15)
    e_22.grid(column=3, row=13)
    
    b_save = Button(f1, text='저장', command=lambda:save(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22))
    b_save.grid(column=2, row=14)
    

def read_data() :
    data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv', encoding='euc-kr')
    
    subset = data[["주차장코드", "주차장명", "주소"]]
    subset_list = []

    subset_list = [tuple(x) for x in subset.to_numpy()]
    
    return subset_list


def admin_parkingdata() :
    
    # 윈도우 생성
    w_pd = Tk()
    w_pd.geometry('800x800')
    w_pd.title('주차장 정보 조회/수정')
    
    #라벨 생성
    l_info = Label(w_pd, text = '주차장 정보 조회 / 수정')
    l_info.grid(column=2, row=0)
    
    
    #버튼
    b_commit = Button(w_pd, text='새로생성', command=lambda:create_parking(w_pd))
    b_commit.grid(column=2, row=1)
    
    treeview=ttk.Treeview(w_pd, columns=["주차장코드","주차장명", "주소"], 
                                  displaycolumns=["주차장코드","주차장명", "주소"])
    treeview.grid(column=2, row=2)
    

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("주차장코드", width=100, anchor="center")
    treeview.heading("주차장코드", text="주차장코드", anchor="center")
    
    treeview.column("주차장명", width=150, anchor="center")
    treeview.heading("주차장명", text="주차장명", anchor="center")

    treeview.column("주소", width=200, anchor="center")
    treeview.heading("주소", text="주소", anchor="center")

    # 표에 삽입될 데이터
    treelist = read_data()
    
    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i)+"번")
    
    #프레임생성
    f2 = Frame(w_pd)
    f2.grid(column=2, row =3)
    
    # 라벨 2 : 구체적인 값을 출력 할 영역
    l_value_1 = Label(f2, text=" ")
    l_value_1.grid(column=0,row=0)
    l_value_2 = Label(f2, text=" ")
    l_value_2.grid(column=0, row=1)
    l_value_3 = Label(f2, text=" ")
    l_value_3.grid(column=0, row=2)
    l_value_4 = Label(f2, text=" ")
    l_value_4.grid(column=0, row=3)
    l_value_5 = Label(f2, text=" ")
    l_value_5.grid(column=0, row=4)
    l_value_6 = Label(f2, text=" ")
    l_value_6.grid(column=0, row=5)
    l_value_7 = Label(f2, text=" ")
    l_value_7.grid(column=0, row=6)
    l_value_8 = Label(f2, text=" ")
    l_value_8.grid(column=1, row=0)
    l_value_9 = Label(f2, text=" ")
    l_value_9.grid(column=1,row=1)
    l_value_10 = Label(f2, text=" ")
    l_value_10.grid(column=1, row=2)
    l_value_11 = Label(f2, text=" ")
    l_value_11.grid(column=1, row=3)
    l_value_12 = Label(f2, text=" ")
    l_value_12.grid(column=1, row=4)
    l_value_13 = Label(f2, text=" ")
    l_value_13.grid(column=1, row=5)
    l_value_14 = Label(f2, text=" ")
    l_value_14.grid(column=1, row=6)
    l_value_15 = Label(f2, text=" ")
    l_value_15.grid(column=2, row=0)
    l_value_16 = Label(f2, text=" ")
    l_value_16.grid(column=2, row=1)
    l_value_17 = Label(f2, text=" ")
    l_value_17.grid(column=2,row=2)
    l_value_18 = Label(f2, text=" ")
    l_value_18.grid(column=2,row=3)
    l_value_19 = Label(f2, text=" ")
    l_value_19.grid(column=2,row=4)
    l_value_20 = Label(f2, text=" ")
    l_value_20.grid(column=2,row=5)
    l_value_21 = Label(f2, text=" ")
    l_value_21.grid(column=2,row=6)
    l_value_22 = Label(f2, text=" ")
    l_value_22.grid(column=2,row=7)
    l_value_23 = Label(f2, text=" ")
    l_value_23.grid(column=2,row=8)
    
    
    
    # 테이블 항목 클릭시 click_item 호출 
    def click_item(event): 
        
        # 클릭한 항목
        selectedItem = treeview.focus() 
        
        # 클릭한 항목의 "주차장코드"만 추출
        selectedItem_code = treeview.item(selectedItem).get('values')[0]
        
        # 주차장 정보 파일 열기
        data = pd.read_csv("/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv", encoding="euc-kr")
        
        
        # 파일에서 '주차장코드' 속성이 selectedItem_code인 것 추출 (PK임)
        data = data[data['주차장코드'] == selectedItem_code]

        # 상세 값
        value_1 = "주차장코드 : " + str(data['주차장코드'].values[0])
        value_2 = "주차장명 : " + str(data['주차장명'].values[0])
        value_3 = "주소 : " + str(data['주소'].values[0])
        value_4 = "주차장 종류 : " + str(data['주차장 종류'].values[0])
        value_5 = "주차장 종류명 : " + str(data['주차장 종류명'].values[0])
        value_6 = "운영구분 : " + str(data['운영구분'].values[0])
        value_7 = "운영구분명 : " + str(data['운영구분명'].values[0]) 
        value_8 = "총 주차면 : " + str(data['총 주차면'].values[0])
        value_9 = "유무료구분 : " + str(data['유무료구분'].values[0])
        value_10 = "유무료구분명 : " + str(data['유무료구분명'].values[0])
        value_11 = "평일 운영 시작시각(HHMM) : " + str(data['평일 운영 시작시각(HHMM)'].values[0])
        value_12 = "평일 운영 종료시각(HHMM) : " + str(data['평일 운영 종료시각(HHMM)'].values[0])
        value_13 = "최종 데이터 동기화 시간: " + str(data['최종데이터 동기화 시간'].values[0])
        value_14 = "기본 주차 요금 : " + str(data['기본 주차 요금'].values[0])
        value_15 = "기본 주차 시간(분 단위) : " + str(data['기본 주차 시간(분 단위)'].values[0])
        value_16 = "추가 단위 요금 : " + str(data['추가 단위 요금'].values[0])
        value_17 = "추가 단위 시간(분 단위) : " + str(data['추가 단위 시간(분 단위)'].values[0])
        value_18 = "일 최대 요금 : " + str(data['일 최대 요금'].values[0])
        value_19 = "구 : " + str(data['구'].values[0])
        value_20 = "행정동 : " + str(data['행정동'].values[0])
        value_21 = "전화번호 : " + str(data['전화번호'].values[0])
        value_22 = "야간무료개방여부 : " + str(data['야간무료개방여부'].values[0])
        value_23 = "야간무료개방여부명 : " + str(data['야간무료개방여부명'].values[0])
        
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
        l_value_14.configure(text=value_14)
        l_value_15.configure(text=value_15)
        l_value_16.configure(text=value_16)
        l_value_17.configure(text=value_17)
        l_value_18.configure(text=value_18)
        l_value_19.configure(text=value_19)
        l_value_20.configure(text=value_20)
        l_value_21.configure(text=value_21)
        l_value_22.configure(text=value_22)
        l_value_23.configure(text=value_23)

    
    treeview.bind('<ButtonRelease-1>', click_item)
    
    w_pd.mainloop()
    

#admin_parkingdata()
    