#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:27:51 2021

@author: yerim
"""

# 파이썬 GUI  라이브러리인 tkinter 임포트 
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd


def create_cardata(window):
    
    
    def save(c1,c2,c3,c4,c5) :
        
        data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', encoding='euc-kr')
        
        new = pd.DataFrame({'차량번호':[c1.get()],'주차장코드':[c2.get()],'입차시간':[c3.get()],'결제요금':[c4.get()],'결제정보':[c5.get()]})
        # 만일 주차장 코드가 겹치면, 해당 데이터를 수정하는 것
        modify = data[data['차량번호'] == c1.get()]
        print(new)
        
        
        # 만일 주차장 코다가 겹치지 않는다면, 새로운 주차장 데이터를 추가하는 것
        if len(modify) < 1 :
            new_data = pd.concat([data, new], axis=0)
            new_data.to_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', index=False, encoding='euc-kr')
        
        else :
            idx = data[data['차량번호'] == c1.get()].index
            data = data.drop(idx)
            new_data = pd.concat([data, new], axis=0)
            new_data.to_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', index=False, encoding='euc-kr')
            
    
    v1,v2, v3,v4, v5 = StringVar(), IntVar(), StringVar(), IntVar(), StringVar()
  

    f1 = Frame(window)
    f1.grid(column=2,row=5)
    
    l_1 = Label(f1, text='차량번호', width=15)
    l_1.grid(column=0, row=3)
    e_1 = Entry(f1, textvariable = v1, width = 15)
    e_1.grid(column=1, row=3)
    
    l_2 = Label(f1, text='주차장코드')
    l_2.grid(column=0, row=4)
    e_2 = Entry(f1, textvariable = v2, width = 15)
    e_2.grid(column=1, row=4)
    
    l_3 = Label(f1, text='입차시간')
    l_3.grid(column=0, row=5)
    e_3 = Entry(f1, textvariable = v3, width = 15)
    e_3.grid(column=1, row=5)
    
    l_4 = Label(f1, text='결제요금')
    l_4.grid(column=0, row=6)
    e_4 = Entry(f1, textvariable = v4, width = 15)
    e_4.grid(column=1, row=6)
    
    l_5 = Label(f1, text='결제정보')
    l_5.grid(column=0, row=7)
    e_5 = Entry(f1, textvariable = v5, width = 15)
    e_5.grid(column=1, row=7)

    
    b_save = Button(f1, text='저장', command=lambda:save(v1,v2,v3,v4,v5))
    b_save.grid(column=1, row=8)
    

def read_data() :
    data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', encoding='euc-kr')
    
    subset = data[["차량번호","주차장코드", "입차시간", "결제요금","결제정보"]]
    subset_list = []

    subset_list = [tuple(x) for x in subset.to_numpy()]
    
    return subset_list


def admin_cardata() :
    
    # 윈도우 생성
    w_cd = Tk()
    w_cd.geometry('800x800')
    w_cd.title('주차 차량 정보 조회/수정')
    
    #라벨 생성
    l_info = Label(w_cd, text = '주차차량 정보 조회 / 수정')
    l_info.grid(column=2, row=0)
    
    
    #버튼
    b_commit = Button(w_cd, text='새로생성', command=lambda:create_cardata(w_cd))
    b_commit.grid(column=2, row=1)
    
    treeview=ttk.Treeview(w_cd, columns=["차량번호","주차장코드", "입차시간", "결제요금","결제정보"], 
                                  displaycolumns=["차량번호","주차장코드", "입차시간", "결제요금","결제정보"])
    treeview.grid(column=2, row=2)
    

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("차량번호", width=100, anchor="center")
    treeview.heading("차량번호", text="차량번호", anchor="center")
    
    treeview.column("주차장코드", width=100, anchor="center")
    treeview.heading("주차장코드", text="주차장코드", anchor="center")

    treeview.column("입차시간", width=100, anchor="center")
    treeview.heading("입차시간", text="입차시간", anchor="center")
    
    treeview.column("결제요금", width=100, anchor="center")
    treeview.heading("결제요금", text="결제요금", anchor="center")
    
    treeview.column("결제정보", width=100, anchor="center")
    treeview.heading("결제정보", text="결제정보", anchor="center")

    # 표에 삽입될 데이터
    treelist = read_data()
    
    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i)+"번")
    
    #프레임생성
    f2 = Frame(w_cd)
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

    
    
    
    # 테이블 항목 클릭시 click_item 호출 
    def click_item(event): 
        
        # 클릭한 항목
        selectedItem = treeview.focus() 
        
        # 클릭한 항목의 "주차장코드"만 추출
        selectedItem_code = treeview.item(selectedItem).get('values')[0]
        
        # 주차장 정보 파일 열기
        data = pd.read_csv("/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv", encoding="euc-kr")
        
        
        # 파일에서 '주차장코드' 속성이 selectedItem_code인 것 추출 (PK임)
        data = data[data['차량번호'] == selectedItem_code]

        # 상세 값
        value_1 = "차량번호 : " + str(data['차량번호'].values[0])
        value_2 = "주차장코드 : " + str(data['주차장코드'].values[0])
        value_3 = "입차시간 : " + str(data['입차시간'].values[0])
        value_4 = "결제요금 : " + str(data['결제요금'].values[0])
        value_5 = "결제정보 : " + str(data['결제정보'].values[0])

        # 라벨 내용 바꾸어 출력하기
        l_value_1.configure(text=value_1)
        l_value_2.configure(text=value_2)
        l_value_3.configure(text=value_3)
        l_value_4.configure(text=value_4)
        l_value_5.configure(text=value_5)


    
    treeview.bind('<ButtonRelease-1>', click_item)
    
    w_cd.mainloop()
    

#admin_cardata()
    