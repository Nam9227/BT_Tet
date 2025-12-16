from tkinter import *
from tkinter import messagebox
import json
tt=["msv","ten","m1","m2","m3","m4"]
ds=[]
def capnhat():
    global ds
    try:
        with open("dulieu.json", "r", encoding="utf-8") as f:
            ds = json.load(f)
    except FileNotFoundError:
        ds = []
        with open("dulieu.json", "w", encoding="utf-8") as f:
            json.dump(ds, f, ensure_ascii=False, indent=4)
def luuthaydoi():
    with open("dulieu.json", "w", encoding="utf-8") as f:
            json.dump(ds, f, ensure_ascii=False, indent=4)
class cs_xoa():
    def xoacs(self):
        for i in self.kq.winfo_children():
            i.destroy()
    def xoa(self):
        BG_FRAME = '#B0D7C6' 
        FG_DARK = '#1E5E40'      
        BTN_BG = '#F0F5F0'        
        EXIT_BG = '#F46060'
        self.xoacs()
        global ds
        trt=False
        k=self.msv.get()
        for i in ds:
            if i[tt[0]]==k:
                trt=True
                ds.remove(i)
                luuthaydoi()
                print(f"✨ Đã xóa hồ sơ: {k}")
                t=Label(self.kq,text=f"✨ Đã Xóa Sinh Viên {k}",font=('Arial',10),fg=FG_DARK,bg=BG_FRAME)
                t.pack(anchor='n', padx=1, pady=1)
                break
        if trt==False:
            t=Label(self.kq,text=f"Không tìm thấy {k} !",font=('Arial',10),fg=EXIT_BG,bg=BG_FRAME)
            t.pack(anchor='n', padx=1, pady=1)

    def dong_het(self):
        self.home.destroy()
    def thoat(self):
        self.cs.destroy()
        self.home.deiconify()
    def __init__(self,home):
        capnhat()
        self.home=home
        self.home.withdraw()
        cs=Toplevel()
        cs.protocol("WM_DELETE_WINDOW", self.dong_het)
        cs.resizable(False, False)
        BG_FRAME = '#B0D7C6' 
        FG_DARK = '#1E5E40'      
        BTN_BG = '#F0F5F0'        
        EXIT_BG = '#F46060' 
        cs['bg']=BG_FRAME
        cs.geometry('250x280')

        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=14)
        luu=Button(ten_1,text='Quay Lại',bg=BTN_BG,fg=FG_DARK,width=10,height=1,font=('Arial',10),command=self.thoat)
        luu.pack(side='left', padx=(5,150))

        t=Label(cs,text="Xóa Sinh Viên",font=('Arial',15),fg=FG_DARK,bg=BG_FRAME)
        t.pack(anchor='n', padx=30, pady=5)
        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=9)
        a=Label(ten_1,text= "Mã Sinh Viên : ",font=('Arial',12),fg=FG_DARK,bg=BG_FRAME)
        self.msv=Entry(ten_1,font=('Arial',12))
        a.pack(side='left', padx=(0, 5))
        self.msv.pack(side='right', padx=(0, 5))

        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=9)
        self.kq=Frame(cs,bg=BG_FRAME)
        self.kq.pack(anchor='n', padx=15, pady=7)
        a=Button(ten_1,text= "Xóa",font=('Arial',12),bg="#CC6666",command=self.xoa,fg="#FFFFFF")
        a.pack(side='left', padx=(120,10))
        
        setattr(self, "cs", cs)
if __name__ == "__main__":
    root = Tk()
    root.title("Cửa Sổ Chính")
    root.geometry("600x400")
    
    def mo_cs_them():
        cs_xoa(root)
    btn_them = Button(root, text="Mở Cửa Sổ Thêm", command=mo_cs_them)
    btn_them.pack(pady=50)
    root.mainloop()