#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:10:53 2021

@author: yerim
"""

# 파이썬 GUI  라이브러리인 tkinter 임포트 
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
from datetime import datetime
import time

# =============================================================================
# 주차요금 조회
# =============================================================================

def calcate_charge(stand,stand_time,add,add_time,parking_time, fee_limit):
    parking_time_string = str(parking_time)
    parking_time_split = parking_time_string.split(':')
    total = (int(parking_time_split[0]) * 60) + (int(parking_time_split[1]))
    fin_charge = stand + (((total - int(stand_time)) / add_time ) * add)
    
    if (fin_charge > fee_limit) & (fee_limit != 0) :
        if int(parking_time_split[0]) > 24 :
            day = int(parking_time_split[0]) / 24
            fin_charge = day * fee_limit
        else :
            fin_charge = fee_limit
   
    return fin_charge
    

def search_charge(Car, window) :
    def update_y(C, result) :
        # 차량정보파일읽기
        data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', encoding='euc-kr')   
    
        #입력한 차량번호에 해당하는 데이터만 뽑기
        car_data = data[data['차량번호'] == C]
        
        # 결제 요금을 reuslt로 업데이트, 결제 정보를 Y로 업데이트
        new_data = pd.DataFrame({'차량번호':[C], '주차장코드':[car_data['주차장코드'].values[0]],'입차시간':[car_data['입차시간'].values[0]],'결제요금':[result],'결제정보':['Y']})
        idx = data[data['차량번호'] == C].index
        data = data.drop(idx)
        data_fin = pd.concat([data,new_data])
        data_fin.to_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', encoding='euc-kr', index=False)
        
        
        
    # 차량정보파일읽기
    data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', encoding='euc-kr')    
    # 주차장파일읽기
    data2 = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv', encoding='euc-kr')
    
    #입력한 차량번호에 해당하는 데이터만 뽑기
    car_data = data[data['차량번호'] == Car.get()]
    
    #현재시간
    now = datetime.now()
    now2= time.localtime()
    
    #만일 차량번호가 유효하지 않으면 경고창 팝업
    if len(car_data) < 1 :
        popup = Tk()
        popup.title('오류')
        l_alert = Label(popup, text ='등록된 차량이 없습니다. 차량번호를 다시 확인하세요')
        l_alert.pack()
    
    #만일 차량번호가 유효하면 주차요금 계산
    else :
        # 주차장정보파일에서 해당 차량이 주차된 주차장 정보를 불러오기
        new_data2 = data2[data2['주차장코드'] == car_data['주차장코드'].values[0]]    
        
        # 주차요금 계산을 위해 필요한 변수
        v_stand = new_data2['기본 주차 요금'].values[0]
        v_stand_time = new_data2['기본 주차 시간(분 단위)'].values[0]
        v_add = new_data2['추가 단위 요금'].values[0]
        v_add_time = new_data2['추가 단위 시간(분 단위)'].values[0]
        v_fee_limit = new_data2['일 최대 요금'].values[0]
        
        # 얼마나 오래 주차했는지 계산 (현재시간 - 입차시간)
        col_time = datetime.strptime(car_data['입차시간'].values[0], "%Y/%m/%d %H:%M:%S")
        v_parking_time = now-col_time
        
        # 주차요금 계산
        result = calcate_charge(v_stand, v_stand_time, v_add, v_add_time, v_parking_time, v_fee_limit)
        final_text = str(result) + ' 원' 
        
        # 라벨
        l_p_name = Label(window, text = new_data2['주차장명'].values[0])
        l_p_name.pack()
        l_c_in = Label(window, text = '입차시간 : ' + str(car_data['입차시간'].values[0]))
        l_c_in.pack()
        l_now = Label(window, text = '현재시간 : ' + "%04d/%02d/%02d %02d:%02d:%02d" % (now2.tm_year, now2.tm_mon, now2.tm_mday, now2.tm_hour, now2.tm_min, now2.tm_sec) )
        l_now.pack()
        l_p_stand = Label(window, text =  '기본 주차 요금 :' + str(v_stand) + '원' + '(기본 주차 시간 :' + str(v_stand_time) + '분 )')
        l_p_stand.pack()
        l_p_add = Label(window, text = '추가 단위 요금 : ' + str(v_add) + '원' + '(' + str(v_add_time) + '분 당)')
        l_p_add.pack()
        l_p_limit = Label(window, text = '일 최대 요금 : ' + str(v_fee_limit))
        l_p_limit.pack()
        l_p_alert = Label(window, text = '일 최대 요금이 NaN인 경우 주차요금을 무한 징수 할수 있으니 주의하세요.')
        l_p_alert.pack()
        l_final = Label(window, text = '최종 주차 요금 : ' + str(result) + '원') # 최종 주차 요금
        l_final.pack()
        
        #버튼
        b_commit = Button(window, text='결제완료', command=lambda:update_y(Car.get(), result))
        b_commit.pack()
    

def open_charge_window() :
    # w_main.destroy() # 메인 페이지 닫기
    print("실행")


    # 주차 요금 조회/결제 페이지 생성
    w_charge = Tk() # 주차 요금/조회 페이지 윈도우 명 : w_charge
    w_charge.geometry('800x800') # 주차요금 조회/결제 페이지의 크기를 800x800 으로 설정.
    w_charge.title("파킹서울_주차 요금 조회 / 결제 페이지") # 주차 요금 조회/결제 페이지의 제목 : 파킹서울_주차 요금 조회 /결제 페이지
    
    # 라벨생성
    l_carnumber = Label(w_charge, text="차량번호를 입력하세요")
    l_carnumber.pack()

    # 변수생성
    carnumber = StringVar()
    
    # 차량번호를 입력 받을 칸
    input_carnumber = Entry(w_charge, textvariable= carnumber, width=30)
    input_carnumber.pack()
    
    #버튼생성
    b_charge = Button(w_charge, text="요금조회", command=lambda:search_charge(carnumber, w_charge))
    b_charge.pack()
    
    
    w_charge.mainloop()

open_charge_window()