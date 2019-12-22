import tkinter as tk
import Calculator

#화면과 화면의 이름,크기 생성
clac=tk.TK()
calc.title('Calculator')
calc.geometry('300*300')

display=tk.Entry(calc,width=20) #display라는 이름의 출력창 추가. 폭20.
display.pack()


calc.mainloop()