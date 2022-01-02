#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:27:19 2021

@author: yerim
"""

# 파이썬 GUI  라이브러리인 tkinter 임포트 
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
import time
from datetime import datetime


def car_out(window) :
    def complete_out(car) :
        car_data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', encoding='euc-kr')
        new_car_data = car_data[car_data['차량번호'] == car.get()]

        idx = car_data[car_data['차량번호'] == car.get()].index
        car_data = car_data.drop(idx)
        car_data.to_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', encoding='euc-kr', index=False)
    
    
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

    def save_out(car,frame) :
        car_data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', encoding='euc-kr')
        parking_data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv', encoding='euc-kr')
        new_car_data = car_data[car_data['차량번호'] == car.get()]
        
        #현재시간
        now = datetime.now()

        
        # 결제 여부 확인
        if new_car_data['결제정보'].values[0] =='Y' :
            l_fin = Label(frame, text='결제가 완료되어 출차합니다.\n 출차성공!')
            l_fin.grid(column=0, row=5) 
            idx = car_data[car_data['차량번호'] == car.get()].index
            car_data = car_data.drop(idx)
            car_data.to_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv',encoding='euc-kr', index=False)
        
        # 결제하지 않았으면 결제 요금 확인
        else :
            new_parking_data=parking_data[parking_data['주차장코드']==new_car_data['주차장코드'].values[0]]
        
            # 주차요금 계산을 위해 필요한 변수
            v_stand = new_parking_data['기본 주차 요금'].values[0]
            v_stand_time = new_parking_data['기본 주차 시간(분 단위)'].values[0]
            v_add = new_parking_data['추가 단위 요금'].values[0]
            v_add_time = new_parking_data['추가 단위 시간(분 단위)'].values[0]
            v_fee_limit = new_parking_data['일 최대 요금'].values[0]
        
            # 얼마나 오래 주차했는지 계산 (현재시간 - 입차시간)
            col_time = datetime.strptime(new_car_data['입차시간'].values[0], "%Y/%m/%d %H:%M:%S")
            v_parking_time = now-col_time
            
            # 주차요금 계산
            result = calcate_charge(v_stand, v_stand_time, v_add, v_add_time, v_parking_time, v_fee_limit)
            
            #라벨 생성
            l_result = Label(frame, text='결제하지 않았습니다.\n 결제요금 : ' + str(result) + '원')
            l_result.grid(column=0, row=3)
            
            #버튼 생성
            b_result = Button(frame, text='결제 확인 및 출차' , command=lambda:[l_result.grid_forget(),b_result.grid_forget(),complete_out(car)])
            b_result.grid(column=0, row=4)
            
            
    
    #프레임
    f3 = Frame(window)
    f3.grid(column=1, row=2)
    
    
    #변수생성
    carnumber = StringVar()
    carnumber.set('차량번호')

    
    #변수값 입력 받기
    input_car = Entry(f3, textvariable=carnumber,width=15)
    input_car.grid(column=0,row=0)

    
    #버튼
    b_commit = Button(f3,text='출차 등록',command=lambda:save_out(carnumber, f3))
    b_commit.grid(column=0,row=2)
    
    

def car_in(window) :
    def save_in(car,parking) :
        car_data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', encoding='euc-kr')
        parking_data = pd.read_csv('/Users/yerim/Desktop/parkingseoul/final_data/parking_data.csv', encoding='euc-kr')
        new_parking_data = parking_data[parking_data['주차장코드'] == parking.get()]
        
        # 현재시간
        now = time.localtime()
        col_now = "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        
        # 입력할 데이터
        newline = pd.DataFrame({'차량번호':[car.get()], '주차장코드':[parking.get()], '입차시간':[col_now], '결제요금':[new_parking_data['기본 주차 요금'].values[0]], '결제정보':['N']}) 
        
        new_data = pd.concat([car_data, newline], axis=0)
        new_data.to_csv('/Users/yerim/Desktop/parkingseoul/final_data/car_data.csv', encoding='euc-kr', index=False)
        
        
        
    #프레임
    f2 = Frame(window)
    f2.grid(column=0, row=2)
    
    
    #변수생성
    carnumber = StringVar()
    parknumber = IntVar()
    carnumber.set('차량번호')
    parknumber.set('주차장코드')
    
    #변수값 입력 받기
    input_car = Entry(f2, textvariable=carnumber,width=15)
    input_car.grid(column=0,row=0)
    input_park = Entry(f2, textvariable=parknumber, width=15)
    input_park.grid(column=0, row=1)
    
    #버튼
    b_commit = Button(f2,text='입차 등록',command=lambda:save_in(carnumber, parknumber))
    b_commit.grid(column=0,row=2)

    

def admin_car_inout() :
    w_carinout = Tk()
    w_carinout.geometry('300x300')
    w_carinout.title('차량입/출차')
    
    #프레임
    f1=Frame(w_carinout)
    f1.grid(column=0, row=1)
    
    #버튼
    b_in = Button(f1, text='입차', command=lambda:car_in(w_carinout))
    b_out = Button(f1, text='출차', command=lambda:car_out(w_carinout))
    b_in.grid(column=0,row=1)
    b_out.grid(column=1, row=1)
    
    w_carinout.mainloop()

#admin_car_inout()
    