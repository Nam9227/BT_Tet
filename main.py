from tkinter import *
from tkinter import messagebox
from them import cs_them
from tim import cs_tim
from xoa import cs_xoa
import json
try:
    with open("dulieu.json", "r", encoding="utf-8") as f:
        ds = json.load(f)
except FileNotFoundError:
    ds = []
    with open("dulieu.json", "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=4)
def luufile():
    if messagebox.askyesno("Thoát", "Bạn có chắc chắn muốn thoát ứng dụng?"):
        home.destroy()
def them():
    cs_them(home)
def tim():
    cs_tim(home)
def full():
    cs=Toplevel()
    d1=Label(cs,text="Mã Sinh viên",font=('',15))
    msv=Entry(cs,width=22,font=('',15))
    d1.place(x=10 ,y= 10)
    msv.place(x=10 ,y= 10)
def xoa():
    cs_xoa(home)
def thong_tin():
    messagebox.showinfo(
    "Thông tin",
    "Phần mềm quản lý dữ liệu lớp học v1.3\n"
    "Tác giả: Văn Nam, Đình Phú , Thế Công\n"
    "Năm phát hành: 2025\n"
)
home=Tk()
home.resizable(False, False)
home.attributes("-topmost",True)
home.title("Hệ Thống Kiểm Soát Điểm CS5")
home.geometry('277x320')
home.resizable(False, False)
BG_FRAME = '#B0D7C6'     
FG_DARK = '#1E5E40'       
BTN_BG = '#F0F5F0'        
EXIT_BG = '#F46060'       
WHITE_FG = '#FFFFFF'      
home['bg']=BG_FRAME
a = Label(
    home,
    text='Menu Quản Lý Dữ Liệu Lớp Học',
    font=('Arial', 13),
    bg=BG_FRAME,          
    fg=FG_DARK            
)
a.place(relx=0.5, y=10, anchor="n")
btn_width = 0.6  
btn_h = 40       
t1 = Button(home, text='Thêm Sinh viên', font=('Arial', 11), command=them, bg=BTN_BG, fg=FG_DARK)
t2 = Button(home, text='Tìm Kiếm Sinh Viên', font=('Arial', 11), command=tim, bg=BTN_BG, fg=FG_DARK)
t3 = Button(home, text='Hiển Thị Toàn Bộ Điểm', font=('Arial', 10), command=full, bg=BTN_BG, fg=FG_DARK)
t4 = Button(home, text='Xóa Dữ Liệu Bằng MSV', font=('Arial', 11), command=xoa, bg=BTN_BG, fg=FG_DARK)
t5 = Button(home, text='Thoát', font=('Arial', 10, 'bold'), command=luufile, bg=EXIT_BG, fg=WHITE_FG)
t6 = Button(home, text='Thông Tin', font=('Arial', 10), command=thong_tin, bg=BTN_BG, fg=FG_DARK)
t1.place(relx=0.5, y=48, anchor="n", relwidth=btn_width, height=btn_h)
t2.place(relx=0.5, y=104, anchor="n", relwidth=btn_width, height=btn_h)
t3.place(relx=0.5, y=159, anchor="n", relwidth=btn_width, height=btn_h)
t4.place(relx=0.5, y=212, anchor="n", relwidth=btn_width, height=btn_h)
t5.place(relx=0.75, y=270, anchor="n", relwidth=0.4, height=35)
t6.place(relx=0.25, y=270, anchor="n", relwidth=0.4, height=35)
home.mainloop()