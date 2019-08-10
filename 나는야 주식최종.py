import random
import time
import threading

from tkinter import *

global CG_lists_2
#매수 체결 변수
CG_lists_1 = int(0)
CG_lists_2 = int(0)



#매수 변수
buy_real = int(0)
buy_buy = int(0)
buy_buy_2 = int(0)

#내돈b
money = int(1000000)


#주가 초기값
samsung = int(11000)
apple = int(13000)
dusan = int(7000)
spg = int(5500)
jungmin = int(12000)


#랜덤 머니
random_money = [100,500,1000,700,150,1200]



#보유 주식 변수
samsung_lists = int(0)
apple_lists =int(0)
dusan_lists = int(0)
spg_lists = int(0)
jungmin_lists = int(0)

lists = 0
lists_2 = 0
point = 0

# 매수 함수 TK
def timer_buy_1():
    global buy_real
    global buy_buy
    global buy_buy_2
    buy_buy = int(buy_buy)
    buy_real = buy_buy * buy_buy_2
    buy_real = int(buy_real)








#주가 변동 함수
def samsungju():
    global samsung
    random_money_1 = random.choice(random_money)
    random_money_1 = int(random_money_1)
    random_updown_1 = random.randrange(1,3)

    if random_updown_1 == 1:
        samsung = samsung + random_money_1

    if random_updown_1 == 2:
        samsung = samsung - random_money_1

    if samsung <= 0 :
        samsung = '종이쪼가리'
        return
    
    threading.Timer(1,samsungju).start()

def appleju():
    global apple
    random_money_2 = random.choice(random_money)
    random_money_2 = int(random_money_2)
    random_updown_2 = random.randrange(1,3)

    if random_updown_2 == 1:
        apple = apple + random_money_2

    if random_updown_2 == 2:
        apple = apple - random_money_2

    if apple <= 0 :
        apple = '종이쪼가리'
        return
    
    threading.Timer(1,appleju).start()


def dusanju():
    global dusan
    random_money_3 = random.choice(random_money)
    random_money_3 = int(random_money_3)
    random_updown_3 = random.randrange(1,3)

    if random_updown_3 == 1:
        dusan = dusan + random_money_3

    if random_updown_3 == 2:
        dusan = dusan - random_money_3

    if dusan <= 0 :
        dusan = '종이쪼가리'
        return
    
    threading.Timer(1,dusanju).start()


def spgju():
    global spg
    random_money_4 = random.choice(random_money)
    random_money_4 = int(random_money_4)
    random_updown_4 = random.randrange(1,3)

    if random_updown_4 == 1:
        spg = spg + random_money_4

    if random_updown_4 == 2:
        spg = spg - random_money_4

    if spg <= 0 :
        spg = '종이쪼가리'
        return
    threading.Timer(1,spgju).start()


def jungminju():
    global jungmin
    random_money_5 = random.choice(random_money)
    random_money_5 = int(random_money_5)
    random_updown_5 = random.randrange(1,3)

    if random_updown_5 == 1:
        jungmin = jungmin + random_money_5

    if random_updown_5 == 2:
        jungmin = jungmin - random_money_5

    if jungmin <= 0 :
        jungmin = '종이쪼가리'
        return
    threading.Timer(1,jungminju).start()

    

'''
#주가 확인 함수##########################################
def jusic():
    print('삼성 : ',samsung,'원')
    print('애플 : ',apple , '원')
    print('두산 : ',dusan , '원')
    print('삼립 : ',spg, '원')
    print('정민 : ',jungmin,'원')

#########################################################


#주식 매수 함수########################################################################################

def buy (name,money_buy):
    global money
    global lists
    print(name,'의 현재가는',money_buy,'원 입니다.')
    if money_buy == '종이쪼가리':
        print('회사가 망해서 구입할수없습니다.')
        return
    stock_num = int(input('몇 주 구매하시겠습니까? : '))
    if (stock_num * money_buy) > money :
        print('잔고가 부족합니다.')
        return

    print(name,'의 주식을',stock_num,'주 매수하시면 ', (stock_num * money_buy),'원 입니다.')
    money = money - (stock_num * money_buy)
    lists = stock_num
    print('매수가 완료되었습니다')
    print('현재 잔고는 ',money,'원 입니다.')

#주식 매도 함수

def sell (name2,money_sell,stock_lists_2):
    global money
    global lists_2
    print(name2,'의 보유주식은',stock_lists_2,'주 입니다')
    print(name2,'의 현재가는' , money_sell,'원 입니다')
    if money_sell == '종이쪼가리':
        print('주식이 망해서 돈을 받지 못합니다')
        return
    pop = int(input('몇 주 판매하시겠습니까? : '))
    if pop > stock_lists_2 :
        print('보유한 주식이 부족합니다.')
        return
    lists_2 = pop
    money = money + (pop * money_sell)
    print(pop,'주 판매하셔서' , (pop * money_sell),'원 입금되었습니다.')

    




#보유 주식 확인 함수

def stock_check():
    print('삼성 : ',samsung_lists,'주')
    print('애플 : ',apple_lists,'주')
    print('두산 : ',dusan_lists,'주')
    print('삼립 : ',spg_lists,'주')
    print('정민 : ',jungmin_lists,'주')
#####################################################################################################3
'''

#주가 변동 함수 실행
dusanju()
spgju()
jungminju()    
appleju()
samsungju()
#체결 완료 TK
def OK_sell():

    ok_sell = Tk()

    ok_sell.title("체결창")
    ok_sell.geometry("300x100+100+100")
    ok_sell.resizable(False, False)

    CG_LB_1 = Label(ok_sell , text = buy_real)
    CG_LB_1.place( x = 30, y = 20 , width = 100 , height = 30 )

    CG_LB_2 = Label(ok_sell , text = '원에 매도 완료했습니다.')
    CG_LB_2.place( x = 130 , y = 20 , width = 130 , height = 30)    
    #창닫기
    def close_CG():
        ok_sell.quit()
        ok_sell.destroy()



    global CG_lists_1
    global CG_lists_2
    global samsung_lists
    global apple_lists
    global dusan_lists
    global spg_lists
    global jungmin_lists
    global money

        
    CG_btn_1 = Button(ok_sell , text = '확인' ,command = close_CG )
    CG_btn_1.place(x = 100 , y = 60 , width = 100 , height = 30 )

    money = money + buy_real
    



    ok_sell.mainloop()



#체결 불가. TK
def NO_sell() :
    no_sell = Tk()
    no_sell.title("결제 오류창")
    no_sell.geometry("300x100+100+100")
    no_sell.resizable(False,False)

    NON_CG_LB = Label(no_sell,text='보유 주식이 부족합니다.')
    NON_CG_LB.place(x = 0 , y = 20 , width = 300 , height = 30)

    def close_NON_CG():
        no_sell.quit()
        no_sell.destroy()

    NON_CG_btn = Button(no_sell, text = '확인',command = close_NON_CG)
    NON_CG_btn.place(x = 100 , y = 60 , width = 100, height = 30 )    
    no_sell.mainloop()



#매도 확인 창 TK 함수 
def CG_sell():

    global buy_real
    global buy_buy_2
    global buy_buy
    global money
    global CG_lists_1
    global CG_lists_2
    global samsung_lists
    global apple_lists
    global spg_lists
    global dusan_lists
    global jungmin_lists
    

    if CG_lists_2 == 1 :
        if samsung_lists < buy_buy_2 :
            NO_sell()
        else :
            OK_sell()
            samsung_lists = samsung_lists - buy_buy_2

    if CG_lists_2 == 2 :
        if apple_lists < buy_buy_2 :
            NO_sell()
        else :
            OK_sell()
            apple_lists = apple_lists - buy_buy_2

    if CG_lists_2 == 3 :
        if dusan_lists < buy_buy_2 :
            NO_sell()
        else :
            OK_sell()
            dusan_lists = dusan_lists - buy_buy_2
            

    if CG_lists_2 == 4 :
        if spg_lists < buy_buy_2 :
            NO_sell()
        else :
            OK_sell()
            spg_lists = spg_lists - buy_buy_2

    if CG_lists_2 == 5 :
        if jungmin_lists < buy_buy_2 :
            NO_sell()
        else :
            OK_sell()
            jungmin_lists = jungmin_lists - buy_buy_2
            





# 매수 확인 창 TK함수 # window_4

def CG_buy():

    global buy_real
    global buy_buy_2
    global buy_buy
    global money
    global CG_lists_1
    global CG_lists_2
    global samsung_lists
    #보유 금액 미달        
    if buy_real > money :
        window_4 = Tk()
        window_4.title("결제 오류창")
        window_4.geometry("300x100+100+100")
        window_4.resizable(False,False)

        NON_CG_LB = Label(window_4,text='잔액이 부족합니다.')
        NON_CG_LB.place(x = 0 , y = 20 , width = 300 , height = 30)

        def close_NON_CG():
            window_4.quit()
            window_4.destroy()

        NON_CG_btn = Button(window_4, text = '확인',command = close_NON_CG)
        NON_CG_btn.place(x = 100 , y = 60 , width = 100, height = 30 )

        
        window_4.mainloop()
    
    #체결 완료 #window_3
    if buy_real < money :

        window_3 = Tk()
        window_3.title("체결창")
        window_3.geometry("300x100+100+100")
        window_3.resizable(False, False)

        CG_LB_1 = Label(window_3 , text = buy_real)
        CG_LB_1.place( x = 30, y = 20 , width = 100 , height = 30 )

        CG_LB_2 = Label(window_3 , text = '원에 매수 완료했습니다.')
        CG_LB_2.place( x = 130 , y = 20 , width = 130 , height = 30)



        #창닫기
        def close_CG():
            window_3.quit()
            window_3.destroy()
        global CG_lists_1
        global CG_lists_2
        global samsung_lists
        global apple_lists
        global dusan_lists
        global spg_lists
        global jungmin_lists


        
        CG_btn_1 = Button(window_3 , text = '확인' ,command = close_CG )
        CG_btn_1.place(x = 100 , y = 60 , width = 100 , height = 30 )

        #돈 줄이기
        money = money - buy_real

        #보유 주식 늘리기 
        if CG_lists_2 == int(1) :
            samsung_lists = samsung_lists + CG_lists_1

        if CG_lists_2 == int(2) :
            apple_lists = apple_lists + CG_lists_1

        if CG_lists_2 == int(3) :
            dusan_lists = dusan_lists + CG_lists_1

        if CG_lists_2 == int(4) :
            spg_lists = spg_lists + CG_lists_1

        if CG_lists_2 == int(5) :
            jungmin_lists = jungmin_lists + CG_lists_1

            
        
    


        window_3.mainloop()
    



    



'''
def CH_Sam ():
    SamText.set(samsung)
    appleText.set(apple)
'''
#주식 매도하기 함수 TK #주식 매도하기 Tk창 window_5
def sell_JU ():
    window_5 = Tk()
    window_5.title("주식 매도하기")
    window_5.geometry("480x400+100+100")
    window_5.resizable(False,False)

    buy_Text = StringVar(window_5)
    buy_Text.set("주식명")

    buy_LB_3 = Label(window_5, textvariable = buy_Text,relief = "solid" )
    buy_LB_3.place(x = 100 , y = 240 , width = 70 ,height = 30 )        

    buy_LB_4 = Label(window_5 , text = '을')
    buy_LB_4.place(x = 180 , y = 240 , width = 20 , height = 30 )

    buy_Text_2 = StringVar(window_5)
    buy_Text_2.set(int(0))

    buy_LB_5 = Label(window_5, textvariable = buy_Text_2 , relief = "solid")
    buy_LB_5.place(x= 230 , y= 240 , width = 40 , height = 30 )

    buy_LB_6 = Label(window_5 , text = '주 매도하시면')
    buy_LB_6.place(x = 285 , y = 240 , width = 100, height = 30 )

    def buy_num_1():
        global buy_real
        global buy_buy
        global buy_buy_2
        global CG_lists_1
        buy_Text_2.set(buy_ety_1.get())
        buy_buy_2 = int(buy_ety_1.get())
        timer_buy_1()
        CG_lists_1 = int(buy_buy_2)
        



    
    def buy_sam():
        global buy_buy
        global CG_lists_1
        global CG_lists_2
        buy_Text.set('Samsung')
        buy_buy = samsung
        CG_lists_2 = int(1) 
        

    def buy_apple():
        global buy_buy
        global CG_lists_1
        global CG_lists_2
        buy_Text.set('Apple')
        buy_buy = int(apple)
        CG_lists_2 = int(2)
        
    def buy_dusan():
        global buy_buy
        buy_Text.set('Dusan')
        buy_buy = int(dusan)
        global CG_lists_1
        global CG_lists_2
        CG_lists_2 = int(3)
        
    def buy_spg():
        global buy_buy
        buy_Text.set('SPG')
        buy_buy = int(spg)
        global CG_lists_1
        global CG_lists_2
        CG_lists_2 = int(4)
        
        

    def buy_JM():
        global buy_buy
        buy_Text.set('JungMin')
        buy_buy = int(jungmin)
        global CG_lists_1
        global CG_lists_2
        CG_lists_2 = int(5)


    buy_LB_1 = Label(window_5 ,relief = "solid", text = '주식 매도 화면 입니다.')
    buy_LB_1.place(x = 0, y = 0 , width = 480 , height = 50)

    buy_LB_2 = Label(window_5 , text = '매도할 주식을 선택해 주세요.')
    buy_LB_2.place( x = 0 , y = 70 , width = 480 , height = 30 )
    
    buy_sam_btn = Button(window_5 , text = 'Samsung',command = buy_sam )
    buy_sam_btn.place( x = 50 , y =110, width = 60 , height = 30  )

    buy_apple_btn = Button(window_5 , text = 'Apple',command = buy_apple )
    buy_apple_btn.place(x = 130, y = 110 ,width = 60 , height = 30 )

    buy_dusan_btn = Button(window_5 , text = 'Dusan',command = buy_dusan)
    buy_dusan_btn.place(x = 210 , y = 110 ,width = 60 , height = 30 )

    buy_spg_btn = Button(window_5 , text = 'SPG',command = buy_spg)
    buy_spg_btn.place(x = 290 , y = 110 , width = 60 , height = 30 )

    buy_JM_btn = Button(window_5 , text = 'JungMin',command = buy_JM)
    buy_JM_btn.place(x = 370 , y = 110 , width = 60 , height = 30 )

    buy_LB_3 = Label(window_5 , text = '매도 할 수량을 입력하세요.')
    buy_LB_3.place(x = 0 , y = 150 , width = 480 , height = 30 )

    buy_ety_1 = Entry(window_5)
    buy_ety_1.place( x = 180 , y = 190 , width = 90 , height = 30 )

    buy_num_btn = Button(window_5 , text ='확인',command = buy_num_1)
    buy_num_btn.place(x = 280 , y = 190 , width = 35 , height = 30 )



    buy_real = int(0)

    def buy_timer():
        global buy_real
        buy_Text_3.set(buy_real)
        window_5.after(1000,buy_timer)





    buy_Text_3 = StringVar(window_5)
    buy_Text_3.set(buy_real)

    buy_LB_7 = Label(window_5 , textvariable = buy_Text_3 )
    buy_LB_7.place( x = 110 , y = 280 , width = 100 , height = 30 )

    buy_timer()


        



    buy_LB_8 = Label(window_5 , text = '원 입니다. 매도하시겠습니까? ')
    buy_LB_8.place ( x = 200 , y = 280 , width = 250 , height = 30 )

    buy_CG_btn = Button(window_5 , text = '체결',command = CG_sell)
    buy_CG_btn.place( x = 180 , y = 330 , width = 120 , height = 50 ) 

    window_5.mainloop()






#주식 매수하기 함수 TK # 주식 매수가하기 TK 창 #window_2
def buy_JU ():




    


    window_2 = Tk()
    window_2.title("주식 매수하기")
    window_2.geometry("480x400+100+100")
    window_2.resizable(False, False)






    buy_Text = StringVar(window_2)
    buy_Text.set("주식명")

    buy_LB_3 = Label(window_2, textvariable = buy_Text,relief = "solid" )
    buy_LB_3.place(x = 100 , y = 240 , width = 70 ,height = 30 )        

    buy_LB_4 = Label(window_2 , text = '을')
    buy_LB_4.place(x = 180 , y = 240 , width = 20 , height = 30 )

    buy_Text_2 = StringVar(window_2)
    buy_Text_2.set(int(0))

    buy_LB_5 = Label(window_2, textvariable = buy_Text_2 , relief = "solid")
    buy_LB_5.place(x= 230 , y= 240 , width = 40 , height = 30 )

    buy_LB_6 = Label(window_2 , text = '주 매수하시면')
    buy_LB_6.place(x = 285 , y = 240 , width = 100, height = 30 )


    


    
    def buy_num_1():
        global buy_real
        global buy_buy
        global buy_buy_2
        global CG_lists_1
        buy_Text_2.set(buy_ety_1.get())
        buy_buy_2 = int(buy_ety_1.get())
        timer_buy_1()
        CG_lists_1 = int(buy_buy_2)
        



    
    def buy_sam():
        global buy_buy
        global CG_lists_1
        global CG_lists_2
        buy_Text.set('Samsung')
        buy_buy = samsung
        CG_lists_2 = int(1) 
        

    def buy_apple():
        global buy_buy
        global CG_lists_1
        global CG_lists_2
        buy_Text.set('Apple')
        buy_buy = int(apple)
        CG_lists_2 = int(2)
        
    def buy_dusan():
        global buy_buy
        buy_Text.set('Dusan')
        buy_buy = int(dusan)
        global CG_lists_1
        global CG_lists_2
        CG_lists_2 = int(3)
        
    def buy_spg():
        global buy_buy
        buy_Text.set('SPG')
        buy_buy = int(spg)
        global CG_lists_1
        global CG_lists_2
        CG_lists_2 = int(4)
        
        

    def buy_JM():
        global buy_buy
        buy_Text.set('JungMin')
        buy_buy = int(jungmin)
        global CG_lists_1
        global CG_lists_2
        CG_lists_2 = int(5)


    

    

    buy_LB_1 = Label(window_2 ,relief = "solid", text = '주식 매수 화면 입니다.')
    buy_LB_1.place(x = 0, y = 0 , width = 480 , height = 50)

    buy_LB_2 = Label(window_2 , text = '매수할 주식을 선택해 주세요.')
    buy_LB_2.place( x = 0 , y = 70 , width = 480 , height = 30 )
    
    buy_sam_btn = Button(window_2 , text = 'Samsung',command = buy_sam )
    buy_sam_btn.place( x = 50 , y =110, width = 60 , height = 30  )

    buy_apple_btn = Button(window_2 , text = 'Apple',command = buy_apple )
    buy_apple_btn.place(x = 130, y = 110 ,width = 60 , height = 30 )

    buy_dusan_btn = Button(window_2 , text = 'Dusan',command = buy_dusan)
    buy_dusan_btn.place(x = 210 , y = 110 ,width = 60 , height = 30 )

    buy_spg_btn = Button(window_2 , text = 'SPG',command = buy_spg)
    buy_spg_btn.place(x = 290 , y = 110 , width = 60 , height = 30 )

    buy_JM_btn = Button(window_2 , text = 'JungMin',command = buy_JM)
    buy_JM_btn.place(x = 370 , y = 110 , width = 60 , height = 30 )

    buy_LB_3 = Label(window_2 , text = '매수 할 수량을 입력하세요.')
    buy_LB_3.place(x = 0 , y = 150 , width = 480 , height = 30 )

    buy_ety_1 = Entry(window_2)
    buy_ety_1.place( x = 180 , y = 190 , width = 90 , height = 30 )

    buy_num_btn = Button(window_2 , text ='확인',command = buy_num_1)
    buy_num_btn.place(x = 280 , y = 190 , width = 35 , height = 30 )



    buy_real = int(0)



        
    def buy_timer():
        global buy_real
        buy_Text_3.set(buy_real)
        window_2.after(1000,buy_timer)





    buy_Text_3 = StringVar(window_2)
    buy_Text_3.set(buy_real)

    buy_LB_7 = Label(window_2 , textvariable = buy_Text_3 )
    buy_LB_7.place( x = 110 , y = 280 , width = 100 , height = 30 )

    buy_timer()


        



    buy_LB_8 = Label(window_2 , text = '원 입니다. 체결하시겠습니까? ')
    buy_LB_8.place ( x = 200 , y = 280 , width = 250 , height = 30 )

    buy_CG_btn = Button(window_2 , text = '체결',command = CG_buy )
    buy_CG_btn.place( x = 180 , y = 330 , width = 120 , height = 50 ) 


    window_2.mainloop()




#수익률 계산 TK
def money_plus ():
    doss = Tk()
    doss.title ("수익률 확인창")
    doss.geometry("300x200+100+100")
    doss.resizable(False, False)

    global money
    money_2 = money
    money_2 = float(money)
    money_3 = money_2 / 1000000
    money_4 = money_3 * 100
    real_money = round(money_4,2)

    money_LB_1 = Label (doss, text = '수익률 확인창 입니다.',relief = "solid")
    money_LB_1.place(x = 0 , y = 0 , width = 300 , height = 50 )


    money_LB_2 = Label(doss, text = real_money)
    money_LB_2.place(x = 150 ,y = 70 ,width = 50 , height = 30 )
    
    money_LB_3 = Label (doss,text = '수익률 : ')
    money_LB_3.place(x = 100 , y = 70 , width = 50 , height =30 )

    money_LB_4 = Label (doss  , text = '%')
    money_LB_4.place(x = 200 , y = 70 , width= 20 , height = 30 )

    money_5 = money
    money_5 = int(money_5)
    money_5 = 3000000 - money_5

    money_LB_5 = Label(doss , text = '게임 승리시 까지 ')
    money_LB_5.place(x = 30 , y = 120 , width = 150 , height = 30 )

    money_LB_6 = Label(doss, text = money_5)
    money_LB_6.place(x = 150 , y = 120 , width = 70 , height = 30)

    money_LB_7 = Label(doss,text='원')
    money_LB_7.place(x = 220 , y = 120 , width = 20 , height = 30 )

    money_LB_8 = Label(doss, text='남았습니다.')
    money_LB_8.place(x = 0 , y = 150 , width = 300 , height = 30 )
    
    
    doss.mainloop()








#주가 타이머 함수
def sam_timer():
    SamText.set(samsung)
    window.after(1000,sam_timer)
    
def apple_timer():
    appleText.set(apple)
    window.after(1000,apple_timer)

def dusan_timer():
    dusanText.set(dusan)
    window.after(1000,dusan_timer)

def spg_timer():
    spgText.set(spg)
    window.after(1000,spg_timer)

def JM_timer():
    JMText.set(jungmin)
    window.after(1000,JM_timer)


#보유 주식 타이머

def sam_timer_2():
    SamText_2.set(samsung_lists)
    window.after(1000,sam_timer_2)

def apple_timer_2 ():
    appleText_2.set(apple_lists)
    window.after(1000,apple_timer_2)

def dusan_timer_2 ():
    dusanText_2.set(dusan_lists)
    window.after(1000,dusan_timer_2)

def spg_timer_2 ():
    spgText_2.set(spg_lists)
    window.after(1000,spg_timer_2)

def JM_timer_2():
    JMText_2.set(jungmin_lists)
    window.after(1000,JM_timer_2)




#보유잔고 타이머

def money_timer():
    moneyText.set(money)
    window.after(1000,money_timer)





    
#TK 메인 화면 루프 (UI)

window = Tk()

window.title("나는야 주식왕")
window.geometry("700x500+100+100")
window.resizable(False, False)

label = Label(window,relief = "solid" ,text = "JM투자증권에 오신 것을 환영합니다")
label.place(x = 0 , y = 0 , width = 700 , height = 100 )

#TK 보유잔고
moneyLB_1 = Label(window,text = '보유 잔고 : ' )
moneyLB_1.place(x = 500 , y = 150 , width = 80 , height = 50)

moneyText = StringVar()
moneyText.set(money)

moneyLB_2 = Label(window,textvariable = moneyText)
moneyLB_2.place(x = 600 , y = 150 , width = 50 , height = 50)

money_timer()

won_money = Label(window,text='원')
won_money.place(x = 650 , y = 150 , width = 30 , height =50 )


#라벨 주가
Main_LB = Label(window ,text = '현재 주가',relief = "solid")
Main_LB.place(x = 110 , y = 170 , width = 80 , height = 30 )

Main_LB_2 = Label(window , text = '보유 주식' , relief = "solid")
Main_LB_2.place(x = 320 , y = 170 , width = 80 , height = 30 )

#삼성 보유 주식 표기

SamText_2 = StringVar()
SamText_2.set(samsung_lists)

have_sam_1 = Label(window,text = '보유 주식 : ')
have_sam_1.place(x = 280 , y = 200 , width = 80 , height = 30 )

have_sam_2 = Label(window,textvariable = SamText_2)
have_sam_2.place(x = 370 , y = 200 , width = 80 , height = 30 )

sam_timer_2()

#애플 보유 주식 표기
appleText_2 = StringVar()
appleText_2.set(apple_lists)

have_apple_1 = Label(window , text = '보유 주식 : ')
have_apple_1.place(x = 280 , y = 230 , width = 80 , height = 30)

have_apple_2 = Label (window , textvariable = appleText_2)
have_apple_2.place(x = 370 , y = 230 , width = 80 , height = 30 )

apple_timer_2()

#두산 보유 주식 표기

dusanText_2 = StringVar()
dusanText_2.set(dusan_lists)

have_dusan_1 = Label(window , text = '보유 주식 : ')
have_dusan_1.place(x = 280 , y = 260 , width = 80 , height = 30)

have_dusan_2 = Label(window , textvariable = dusanText_2)
have_dusan_2.place(x = 370 , y = 260 , width= 80 , height = 30 )

dusan_timer_2()

#spg 보유 주식 표기

spgText_2 = StringVar()
spgText_2.set(spg_lists)

have_spg_1 = Label(window, text = '보유 주식 : ')
have_spg_1.place(x = 280 , y = 290 , width = 80 , height = 30 )

have_spg_2 = Label(window , textvariable = spgText_2)
have_spg_2.place(x = 370 , y = 290 , width=80 , height = 30 )

spg_timer_2()

#정민 보유 주식 표기

JMText_2 = StringVar()
JMText_2.set(jungmin_lists)

have_JM_1 = Label(window , text = '보유 주식 : ')
have_JM_1.place(x = 280 , y = 320 , width = 80 , height = 30 )

have_JM_2 = Label(window , textvariable = JMText_2)
have_JM_2.place(x = 370 , y = 320 , width = 80 , height = 30 )

JM_timer_2()






#TK  삼성주가
SamText = StringVar()
SamText.set(samsung)

samLB_1 = Label(window,text = 'Samsung : ')
samLB_1.place(x = 50 , y = 200 , width = 80 , height = 30)

samLB_2 = Label(window,textvariable = SamText)
samLB_2.place(x = 170 , y = 200 , width = 80 , height = 30 )

sam_timer()

#TK 애플 주가

appleText = StringVar()
appleText.set(apple)

appleLB_1 = Label(window,text = 'Apple : ')
appleLB_1.place(x = 50 , y = 230 , width = 80 , height = 30 )

appleLB_2 = Label(window,textvariable = appleText)
appleLB_2.place(x = 170 , y = 230, width = 80 , height = 30 )

apple_timer()

#TK 두산 주가

dusanText = StringVar()
dusanText.set(dusan)

dusanLB_1 = Label(window,text = 'Dusan : ')
dusanLB_1.place(x = 50 , y = 260 , width = 80 , height = 30 )

dusanLB_2 = Label(window,textvariable = dusanText)
dusanLB_2.place(x = 170 , y = 260  ,width = 80 , height = 30)

dusan_timer()

#Tk spg 주가

spgText = StringVar()
spgText.set(spg)

spgLB_1 = Label(window,text='SPG : ')
spgLB_1.place(x = 50 , y = 290 , width = 80 , height = 30)

spgLB_2 = Label(window , textvariable = spgText)
spgLB_2.place(x = 170 , y = 290 , width = 80 , height = 30 )

spg_timer()

#TK 정민 주가

JMText = StringVar()
JMText.set(jungmin)

JMLB_1 = Label(window , text = 'JungMin : ')
JMLB_1.place(x = 50 , y = 320, width = 80 , height = 30)

JMLB_2 = Label(window, textvariable = JMText)
JMLB_2.place(x = 170 , y = 320 , width = 80 , height = 30)

JM_timer()

#매수 버튼

buy_btn = Button(window,text = '주식 매수하기',command = buy_JU)
buy_btn.place(x = 100 , y = 370 , width = 100 , height = 50 )

#매도 버튼
sell_btn = Button(window,text = '주식 매도하기',command = sell_JU)
sell_btn.place(x = 300 , y = 370 , width = 100 , height = 50 )


#수익률 계산 버튼
money_btn = Button(window , text = '수익률 확인',command = money_plus)
money_btn.place(x = 500 , y = 370 , width = 100 , height =50 )


def win_game():
    W_game = Tk()

    W_game.title("게임 승리")
    W_game.geometry("200x100+100+100")

    W_LB = Label(W_game,text = '게임에서 승리했습니다.')
    W_LB.place(x = 0 , y = 10 , width = 200 , height = 30 )

    W_LB_2 = Label (W_game, text = '게임은 계속 진행됩니다.')
    W_LB_2.place(x = 0  , y = 40 , width = 200, height = 30 )

    W_btn_1 = Button(W_game, text= '확인')
    W_btn_1.place(x = 50 , y = 70 ,width = 100 , height = 20)

    W_game.mainloop()


def lose_game():
    L_game = Tk()

    L_game.title("게임 승리")
    L_game.geometry("200x100+100+100")

    L_LB = Label(L_game,text = '게임에서 패배했습니다.')
    L_LB.place(x = 0 , y = 10 , width = 200 , height = 30 )

    L_LB_2 = Label (L_game, text = '당신은 쫄딱 망했습니다.')
    L_LB_2.place(x = 0  , y = 40 , width = 200, height = 30 )

    def close():
        L_game.quit()

        L_game.destroy()

    
    L_btn_1 = Button(L_game, text= '확인',command = close)
    L_btn_1.place(x = 50 , y = 70 ,width = 100 , height = 20)

    L_game.mainloop()

if money >= 3000000 :
    win_game()

if money <= 50000 :
    lose_game()
    window.quit()





    


window.mainloop()


















#######################################################################################################
'''
#메인 메뉴 (Text)
while True :
    print('★나는 투자왕★')
    print('--------메뉴--------')
    print('1. 계좌 확인하기')
    print('2. 주가 확인하기')
    print('3. 주식 매수하기')
    print('4. 주식 매도하기')
    print('5. 수익률 보기')
    print('6. 보유중인 주식 확인')
    print('7. 종료')
    re = int(input('메뉴를 선택하세요 : '))

#예외처리
    if re == 7 :
        break

#보유 잔고
    if re == 1 :
        print('보유중인 잔고 : ',money,'원')
        continue

#주가 조회
    if re == 2 :
        jusic()

#매수하기
    if re == 3 :
        print('1. 삼성 2. 애플 3. 두산 4. 삼립 5. 정민')
        re2 = int(input('매수할 주식의 번호를 입력해주세요. : '))

        if re2 == 1 :
            buy('삼성',samsung)
            global stock_num
            samsung_lists = samsung_lists + lists

        if re2 == 2 :
            buy('애플',apple)
            global stock_num
            apple_lists = apple_lists + lists

        if re2 == 3 :
            buy('두산',dusan)
            global stock_num
            dusan_lists = dusan_lists + lists

        if re2 == 4 :
            buy('삼립',spg)
            global stock_num
            spg_lists = spg_lists + lists

        if re2 == 5 :
            buy('정민',jungmin)
            global stock_num
            jungmin_lists = jungmin_lists + lists



#매도 하기
    if re == 4 :
        stock_check()
        print('1.삼성 2.애플 3.두산 4.삼립 5.정민')
        re_1 = int(input('매도할 주식을 선택해주세요 : '))
        if re_1 == 1 :
            sell('삼성',samsung,samsung_lists)
            samsung_lists = samsung_lists - lists_2

        if re_1 == 2 :
            sell('애플',apple,apple_lists)
            apple_lists = apple_lists - lists_2

        if re_1 == 3 :
            sell('두산',dusan,dusan_lists)
            dusan_lists = dusan_lists - lists_2

        if re_1 == 4 :
            sell('삼립',spg,spg_lists)
            spg_lists = spg_lists - lists_2

        if re_1 == 5 :
            sell('정민',jungmin,jungmin_lists)
            jungmin_lists = jungmin_lists - lists_2

        else :
            print('잘못입력하셨습니다')
            continue

#수익률 보기

    if re == 5 :
        point = money/1000000
        if point > 1 :
            print('당신이 번 돈은',(money - 1000000),'원 이고,')
            print('당신의 수익률은 ', (point * 100 ), '% 입니다.')
            continue
        if point < 1 :
            print('당신이 잃은 돈은' (1000000 - money),'원 이고,')
            print('당신은 처음 돈의',(point * 100 ), '% 만 가지고 있습니다.')
            continue

        if point == 1 :
            print('당신은 원금을 가지고 있습니다.')
            continue




#보유 주식 확인

    if re == 6 :
        stock_check()
        continue


    #게임의 끝

    if money == 3000000:
        print("당신은 수익률 300%의 주식왕!!")
        break

    if money <= 0 :
        print("쫄딱 망했습니다 ㅠㅠ")
        break
###############################################################################################
'''

        
        
        
    
