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
def tik(k):
    trt=False
    sv=[]
    for i in ds:
        if i[tt[0]]==k:
            trt=True
            print("✨ Đã tìm thấy hồ sơ: ")
            t=0
            for j in range(1,6):
                sv.append(i[tt[j]])
            break
    if trt == False:
        return False
    else:
        return sv
class cs_tim():
    def timk(self):
        BG_FRAME = '#B0D7C6' 
        FG_DARK = '#1E5E40'      
        BTN_BG = '#F0F5F0'        
        EXIT_BG = '#F46060' 
        self.xoa()
        msv=self.msv.get()
        sv=tik(msv)
        if sv==False:

            t=Label(self.kq,text=f" Không Tìm Thấy {msv} !",font=('Arial',12),fg=EXIT_BG,bg=BG_FRAME)
            t.pack(anchor='n', padx=30, pady=1)
        else:
            text = (
                        f"Họ và tên: {sv[0]}\n"
                        f"Điểm Giải Tích: {sv[1]}\n"
                        f"Điểm Tư Tưởng HCM: {sv[2]}\n"
                        f"Điểm Tư Duy Tính Toán: {sv[3]}\n"
                        f"Điểm Đại Số Tuyến Tính: {sv[4]}"
                    )

            Label(
                self.kq,
                text=text,
                justify='left',
                font=('Arial', 12),
                bg=BG_FRAME,
                fg=FG_DARK
                ).pack(padx=0, pady=0)
            

    def xoa(self):
        for i in self.kq.winfo_children():
            i.destroy()
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
        cs.geometry('280x320')

        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=14)
        luu=Button(ten_1,text='Quay Lại',bg=BTN_BG,fg=FG_DARK,width=10,height=1,font=('Arial',10),command=self.thoat)
        luu.pack(side='left', padx=(5,150))

        t=Label(cs,text="Tìm Kiếm Sinh Viên ",font=('Arial',15),fg=FG_DARK,bg=BG_FRAME)
        t.pack(anchor='n', padx=30, pady=1)
        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=7)
        a=Label(ten_1,text= "Mã Sinh Viên : ",font=('Arial',12),fg=FG_DARK,bg=BG_FRAME)
        self.msv=Entry(ten_1,font=('Arial',12))
        a.pack(side='left', padx=(0, 5))
        self.msv.pack(side='right', padx=(0, 5))

        ten_1=Frame(cs,bg=BG_FRAME)
        ten_1.pack(anchor='n', padx=15, pady=7)
        self.kq=Frame(cs,bg=BG_FRAME)
        self.kq.pack(anchor='n', padx=15, pady=7)
        a=Button(ten_1,text= "Tìm Kiếm",font=('Arial',12),fg=BTN_BG,bg="#1e5e40",command=self.timk)
        a.pack(side='left', padx=(60,100))
        
        setattr(self, "cs", cs)
#if __name__ == "__main__":
    #root = Tk()
    #root.title("Cửa Sổ Chính")
    #root.geometry("600x400")
    
    #def mo_cs_them():
        #cs_tim(root)
    #btn_them = Button(root, text="Mở Cửa Sổ Thêm", command=mo_cs_them)
    #btn_them.pack(pady=50)
    #root.mainloop()