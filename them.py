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
def kt2(a):
    try:
        float(a)
        return True
    except:
        return False
def kt5(msv):
    capnhat()
    for i in ds:
        if i['msv']==msv:
            return False
    return True
def kt(a):
    for i,j in a.items():
        if j=='':
            return False
        if len(i)==2 and i[0]=='m' and kt2(j):
            if 0<= float(j) <=10:
                continue
            else:
                return False
    return True
def kt4(a):
    sv_moi={}
    j=0
    for i in tt:
        sv_moi[i]=a[j]
        j+=1
    if kt(sv_moi) == True:
        ds.append(sv_moi)
        print("✔️ Thêm Dữ Liệu",sv_moi["msv"], "Thành Công ")
        with open("dulieu.json", "w", encoding="utf-8") as f:
            json.dump(ds, f, ensure_ascii=False, indent=4)
        return True
    return False
class cs_them():
    def thoat(self):
        self.cs.destroy()
        self.home.deiconify()
    def luu(self):
        a=[]
        a.append(self.msv.get())
        a.append(self.ten.get())
        a.append(self.m1.get())
        a.append(self.m2.get())
        a.append(self.m3.get())
        a.append(self.m4.get())
        self.msv.delete(0, END)
        self.ten.delete(0, END)
        self.m1.delete(0, END)
        self.m2.delete(0, END)
        self.m3.delete(0, END)
        self.m4.delete(0, END)
        if kt5(a[0])==False:
            messagebox.showerror("Lỗi", f"{a[0]} Đã Tồn Tại !")
        elif kt4(a):
            messagebox.showinfo("Thành công", f"Đã lưu dữ liệu cho MSV: {a[0]}")
        else:
            messagebox.showerror("Lỗi", "Có Lỗi Trong Quá Trình Lưu Dữ Liệu !")
        
    def dong_het(self):
        self.home.destroy()
    def __init__(self,home):
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
        cs.geometry('320x370')


        t=Label(cs,text="Thêm Sinh Viên",font=('Arial',20),fg=FG_DARK,bg=BG_FRAME)
        t.pack(anchor='n', padx=15, pady=15)
        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=7)
        a=Label(ten_1,text= "Mã Sinh Viên : ",font=('Arial',12),fg=FG_DARK,bg=BG_FRAME)
        self.msv=Entry(ten_1,font=('Arial',12))
        a.pack(side='left', padx=(0, 5))
        self.msv.pack(side='right', padx=(0, 5))

        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=7)
        a=Label(ten_1,text= "Tên Sinh Viên : ",font=('Arial',12),fg=FG_DARK,bg=BG_FRAME)
        self.ten=Entry(ten_1,font=('Arial',12))
        a.pack(side='left', padx=(0, 5))
        self.ten.pack(side='right', padx=(0, 5))

        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=7)
        a=Label(ten_1,text= "Điểm Giải Tích : ",font=('Arial',12),fg=FG_DARK,bg=BG_FRAME)
        self.m1=Entry(ten_1,font=('Arial',12))
        a.pack(side='left', padx=(0, 5))
        self.m1.pack(side='right', padx=(0, 5))

        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=7)
        a=Label(ten_1,text= "Điểm Tư Tưởng HCM : ",font=('Arial',12),fg=FG_DARK,bg=BG_FRAME)
        self.m2=Entry(ten_1,font=('Arial',12))
        a.pack(side='left', padx=(0, 5))
        self.m2.pack(side='right', padx=(0, 5))

        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=7)
        a=Label(ten_1,text= "Điểm Tư Duy TT : ",font=('Arial',12),fg=FG_DARK,bg=BG_FRAME)
        self.m3=Entry(ten_1,font=('Arial',12))
        a.pack(side='left', padx=(0, 5))
        self.m3.pack(side='right', padx=(0, 5))

        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=7)
        a=Label(ten_1,text= "Điểm Đại Số : ",font=('Arial',12),fg=FG_DARK,bg=BG_FRAME)
        self.m4=Entry(ten_1,font=('Arial',12))
        a.pack(side='left', padx=(0, 5))
        self.m4.pack(side='right', padx=(0, 5))

        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=14)
        luu=Button(ten_1,text='Lưu',bg=BTN_BG,fg=FG_DARK,width=8,height=1,font=('Arial',12),command=self.luu)
        t=Button(ten_1,text="Quay Lại",command=self.thoat,bg=BTN_BG,fg=FG_DARK,width=8,height=1,font=('Arial',12)) 


        luu.pack(side='left', padx=(5, 35))
        t.pack(side='left', padx=(35, 5))
        
        setattr(self, "cs", cs)
if __name__ == "__main__":
    root = Tk()
    root.title("Cửa Sổ Chính")
    root.geometry("600x400")
    
    def mo_cs_them():
        cs_them(root)
    btn_them = Button(root, text="Mở Cửa Sổ Thêm", command=mo_cs_them)
    btn_them.pack(pady=50)
    root.mainloop()