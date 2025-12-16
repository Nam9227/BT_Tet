from tkinter import *
from tkinter import messagebox
import json
from tkinter import ttk
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
class cs_full():

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
        BG_FRAME = '#B0D7C6' 
        FG_DARK = '#1E5E40'      
        BTN_BG = '#F0F5F0'        
        EXIT_BG = '#F46060' 
        cs.title("Bảng điểm sinh viên")
        cs.geometry('900x400')
        cs['bg']=BG_FRAME
        bang1 = Frame(cs, bg=BG_FRAME)
        bang1.pack(fill=BOTH, expand=True, padx=0, pady=0)
        bang2 = Frame(cs,bg='white')
        bang2.pack(side=BOTTOM, fill=X)
        cot = ('msv','ten','gt','tthcm','tdtt','dstt')
        b = ttk.Treeview(bang1, columns=cot, show="headings")
        b.heading("msv", text="Mã SV")
        b.heading("ten", text="Họ tên")
        b.heading('gt', text='Giải Tích')
        b.heading("tthcm", text="Tư Tưởng Hồ Chí Minh")
        b.heading("tdtt", text="Tư Duy Tính Toán")
        b.heading('dstt', text='Đại Số Tuyến Tính')
        b.column("msv", width=80,  anchor=W, stretch=False)
        b.column("ten", width=200, minwidth=150, anchor=W, stretch=True)
        b.column("gt", width=100,  anchor=CENTER)
        b.column("tthcm", width=180, minwidth=180, stretch=True,anchor=CENTER)
        b.column("tdtt", width=150, anchor=CENTER)
        b.column("dstt", width=150, anchor=CENTER)
        for sv in ds:
            b.insert(
                "", END,
                values=(sv["msv"], sv["ten"], sv["m1"], sv["m2"], sv["m3"], sv["m4"])
            )
        scroll_y = Scrollbar(bang1, orient=VERTICAL, command=b.yview)
        b.configure(yscrollcommand=scroll_y.set)
        b.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")

        bang1.grid_rowconfigure(0, weight=1)
        bang1.grid_columnconfigure(0, weight=1)
        t = Button(bang2, text='Quay lại', command=self.thoat,bg=FG_DARK,fg='white',width=10,height=2)
        t.pack(side=RIGHT, padx=(10, 50), pady=10)
        setattr(self, "cs", cs)
if __name__ == "__main__":
    root = Tk()
    root.title("Cửa Sổ Chính")
    root.geometry("600x400")
    def mo_cs_them():
        cs_full(root)
    btn_them = Button(root, text="Mở Cửa Sổ Thêm", command=mo_cs_them)
    btn_them.pack(pady=50)
    root.mainloop()
