from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time



fak2="#5FB100"
fak1="#21498e"
kkph=90
kkpp=70
popa=100
pope=60
strok=5
xxx=kkph*8
w1 = Tk() 
w1.title("BTS")
w1.minsize(xxx,610)
w1.config(bg=fak1)
w1.iconbitmap("4r(1).ico")
st_sk=["วัดพระศรีมหาธาตุ","กรมทหารราบที่ 11","บางบัว","กรมป่าไม้","ม.เกษตรศาสตร์","เสนานิคม","รัชโยธิน","พหลโยธิน 24","ห้าเเยกลาดพร้าว"\
       ,"หมอชิต","สะพานควาย","อารีย์","สนามเป้า","อนุสาวรีย์ชัยสมรภูมิ","พญาไท","ราชเทวี","สยาม","ชิดลม","เพลินจิต","นานา","อโศก"\
       ,"พร้อมพงษ์","ทองหล่อ","เอกมัย","พระโขนง","อ่อนนุช","บางจาก","ปุณณวิถี","อุดมสุข","บางนา","เเบริ่ง","สำโรง","ปู่เจ้า","ช้างเอราวัณ","โรงเรียนนายเรือ"\
       ,"ปากน้ำ","ศรีนคริณทร์","เเพรกษา","สายลวด","เคหะ"]

sl_sd=["สนามกีฬาเเห่งชาติ","ราชดำริ","ศาลาเเดง","ช่องนนทรี","ศึกษาวิทยา","สุรศักดิ์","สะพานตากสิน","กรุงธนบุรี","วงเวียนใหญ่","โพธิ์นิมิตร","ตลาดพลู","วุฒากาศ","บางหว้า"]


named_tuple = time.localtime()
time = time.strftime("[%m/%d/%Y, %H:%M:%S]", named_tuple)


def WTF():
    try:
        ww=Tk()
        ww.title("Log")
        ww.iconbitmap("1r.ico")
        disp=Text(ww,width=90,height=40)
        opfi=open("log.txt","r",encoding="utf-8")
        ajay=opfi.read()
        disp.insert(END,ajay)
        opfi.close()
        disp.grid()

    except Exception:
        ko=Label(ww,text="กรุณาเลือกสถานีก่อน อย่างน้อย 1 รายการ").grid()

def Tryna():
    tttn=messagebox.askyesno("Clear","คุณต้องการล้างประวิตการใช้งานหรือไม่")
    if tttn == 1:
        tytn=messagebox.askyesno("Hmm","จริงรึ")
        if tytn == 1:
            tymn=messagebox.askyesno("Hmm","แน่นะ")
            if tymn == 1:
                tyjn=messagebox.askyesno("Hmm","ไม่ยั่วนะ")
                if tyjn == 1:
                    typn=messagebox.askyesno("Hmm","คนอวดดี")
                    if typn == 1:
                        tyon=messagebox.askyesno("Hmm","งั้นพี่ไป")
                        if tyon == 1:
                            with open("log.txt","w",encoding="utf-8")as ttf:
                                ttf.write("--------------------------------Clear"+time+"-------------------------------")
                                messagebox.showinfo("successfully","ตอนนี้ ประวัติการใช้งานได้ถูกล้างเรียบร้อยแล้ว")
            
                            
demo=StringVar()
dema=StringVar()

im1=PhotoImage(file="tt1.png")
im2=PhotoImage(file="tt2.png")
im3=PhotoImage(file="tt3.png")
im4=PhotoImage(file="tt4.png")

gg = Menu(w1)
bg = Menu(gg, tearoff=0)
bg.add_command(label="Open Data file",command=WTF)
bg.add_command(label="Clear Data file",command=Tryna)
gg.add_cascade(label="Option", menu=bg)
bg.add_separator()
bg.add_command(label="Exit", command=w1.destroy)


def MicroA(event):
    lb2.config(state="normal")
    lb2.config(state="readonly")
    ffa.config(text=demo.get())
def MicroB(event):
    hh.config(state="normal")
    ffb.config(text=dema.get())


def Stan(event):
    if lb1.get() == "สายสีเขียว":
        sk=ttk.Combobox(sta ,textvariable=demo,value=st_sk,width=19,state="readonly",font=("Angsana New",12))
        sk.bind("<<ComboboxSelected>>",MicroA)
        sk.grid(column=0,row=1,pady=strok)
        sk.set("")
    elif lb1.get() == "สายสีเขียวเข้ม":
        sr=ttk.Combobox(sta ,textvariable=demo,value=sl_sd,width=19,state="readonly",font=("Angsana New",12))
        sr.bind("<<ComboboxSelected>>",MicroA)
        sr.grid(column=0,row=1,pady=strok)
        sr.set("")

def Stbn(event):
    if lb2.get() == "สายสีเขียว":
        sk2=ttk.Combobox(stb ,textvariable=dema,value=st_sk,width=19,state="readonly",font=("Angsana New",12))
        sk2.bind("<<ComboboxSelected>>",MicroB)
        sk2.grid(column=0,row=1,pady=strok)
        sk2.set("")
    elif lb2.get() == "สายสีเขียวเข้ม":
        sr2=ttk.Combobox(stb ,textvariable=dema,value=sl_sd,width=19,state="readonly",font=("Angsana New",12))
        sr2.bind("<<ComboboxSelected>>",MicroB)
        sr2.grid(column=0,row=1,pady=strok)
        sr2.set("")


def Ennn():
    w2=Tk()
    w2.title("Cost")
    w2.minsize(570,kkpp*4)
    w2.config(bg=fak2)
    w2.iconbitmap("3r.ico")
    tot=0
    case=""
    for h in range(39):
        if demo.get() == st_sk[h] and dema.get() == st_sk[h]:
            case="คุณเลือกสถานีปลายทางซ้ำกับต้นทาง"
    for j in range(12):
        if demo.get() == sl_sd[j] and dema.get() == sl_sd[j]:
            case="คุณเลือกสถานีปลายทางซ้ำกับต้นทาง"
    if demo.get() == st_sk[0] and dema.get() == st_sk[10]:
        cost=16
    elif demo.get() == st_sk[0] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[0] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[0] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[0] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[0] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[0] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[10]:
        cost=16
    elif demo.get() == st_sk[1] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[1] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[1] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[1] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[1] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[1] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[10]:
        cost=16
    elif demo.get() == st_sk[2] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[2] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[2] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[2] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[2] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[2] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[10]:
        cost=16
    elif demo.get() == st_sk[3] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[3] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[3] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[3] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[3] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[3] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == st_sk[39]:
        cost=59    
    elif demo.get() == st_sk[4] and dema.get() == st_sk[10]:
        cost=16
    elif demo.get() == st_sk[4] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[4] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[4] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[4] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[4] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[4] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[10]:
        cost=16
    elif demo.get() == st_sk[5] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[5] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[5] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[5] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[5] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[5] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[10]:
        cost=16
    elif demo.get() == st_sk[6] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[6] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[6] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[6] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[6] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[6] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[10]:
        cost=16
    elif demo.get() == st_sk[7] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[7] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[7] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[7] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[7] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[7] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[10]:
        cost=16
    elif demo.get() == st_sk[8] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[8] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[8] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[8] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[8] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[8] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[10]:
        cost=16
    elif demo.get() == st_sk[9] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[9] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[9] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[9] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[9] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[9] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[0]:
        cost=16
    elif demo.get() == st_sk[10] and dema.get() == st_sk[1]:
        cost=16
    elif demo.get() == st_sk[10] and dema.get() == st_sk[2]:
        cost=16
    elif demo.get() == st_sk[10] and dema.get() == st_sk[3]:
        cost=16
    elif demo.get() == st_sk[10] and dema.get() == st_sk[4]:
        cost=16
    elif demo.get() == st_sk[10] and dema.get() == st_sk[5]:
        cost=16
    elif demo.get() == st_sk[10] and dema.get() == st_sk[6]:
        cost=16
    elif demo.get() == st_sk[10] and dema.get() == st_sk[7]:
        cost=16
    elif demo.get() == st_sk[10] and dema.get() == st_sk[8]:
        cost=16
    elif demo.get() == st_sk[10] and dema.get() == st_sk[9]:
        cost=16
    elif demo.get() == st_sk[10] and dema.get() == st_sk[11]:
        cost=23
    elif demo.get() == st_sk[10] and dema.get() == st_sk[12]:
        cost=26
    elif demo.get() == st_sk[10] and dema.get() == st_sk[13]:
        cost=30
    elif demo.get() == st_sk[10] and dema.get() == st_sk[14]:
        cost=33
    elif demo.get() == st_sk[10] and dema.get() == st_sk[15]:
        cost=37
    elif demo.get() == st_sk[10] and dema.get() == st_sk[16]:
        cost=40
    elif demo.get() == st_sk[10] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[0]:#อารีย์
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[1]:
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[2]:
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[3]:
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[4]:
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[5]:
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[6]:
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[7]:
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[8]:
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[9]:
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[10]:
        cost=23
    elif demo.get() == st_sk[11] and dema.get() == st_sk[12]:
        cost=16
    elif demo.get() == st_sk[11] and dema.get() == st_sk[13]:
        cost=23
    elif demo.get() == st_sk[11] and dema.get() == st_sk[14]:
        cost=26
    elif demo.get() == st_sk[11] and dema.get() == st_sk[15]:
        cost=30
    elif demo.get() == st_sk[11] and dema.get() == st_sk[16]:
        cost=33
    elif demo.get() == st_sk[11] and dema.get() == st_sk[17]:
        cost=37
    elif demo.get() == st_sk[11] and dema.get() == st_sk[18]:
        cost=40
    elif demo.get() == st_sk[11] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[0]:#สนามเป้า
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[1]:
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[2]:
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[3]:
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[4]:
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[5]:
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[6]:
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[7]:
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[8]:
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[9]:
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[10]:
        cost=26
    elif demo.get() == st_sk[12] and dema.get() == st_sk[11]:
        cost=16
    elif demo.get() == st_sk[12] and dema.get() == st_sk[13]:
        cost=16
    elif demo.get() == st_sk[12] and dema.get() == st_sk[14]:
        cost=23
    elif demo.get() == st_sk[12] and dema.get() == st_sk[15]:
        cost=26
    elif demo.get() == st_sk[12] and dema.get() == st_sk[16]:
        cost=30
    elif demo.get() == st_sk[12] and dema.get() == st_sk[17]:
        cost=33
    elif demo.get() == st_sk[12] and dema.get() == st_sk[18]:
        cost=37
    elif demo.get() == st_sk[12] and dema.get() == st_sk[19]:
        cost=40
    elif demo.get() == st_sk[12] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == st_sk[12] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[12] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[12] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[12] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[12] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[12] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[0]:#อนุ
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[1]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[2]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[3]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[4]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[5]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[6]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[7]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[8]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[9]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[10]:
        cost=30
    elif demo.get() == st_sk[13] and dema.get() == st_sk[11]:
        cost=23
    elif demo.get() == st_sk[13] and dema.get() == st_sk[12]:
        cost=16
    elif demo.get() == st_sk[13] and dema.get() == st_sk[14]:
        cost=16
    elif demo.get() == st_sk[13] and dema.get() == st_sk[15]:
        cost=23
    elif demo.get() == st_sk[13] and dema.get() == st_sk[16]:
        cost=26
    elif demo.get() == st_sk[13] and dema.get() == st_sk[17]:
        cost=30
    elif demo.get() == st_sk[13] and dema.get() == st_sk[18]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == st_sk[19]:
        cost=37
    elif demo.get() == st_sk[13] and dema.get() == st_sk[20]:
        cost=40
    elif demo.get() == st_sk[13] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == st_sk[13] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[13] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[13] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[13] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[13] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[0]:#พญาไป
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[1]:
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[2]:
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[3]:
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[4]:
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[5]:
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[6]:
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[7]:
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[8]:
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[9]:
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[10]:
        cost=33
    elif demo.get() == st_sk[14] and dema.get() == st_sk[11]:
        cost=26
    elif demo.get() == st_sk[14] and dema.get() == st_sk[12]:
        cost=23
    elif demo.get() == st_sk[14] and dema.get() == st_sk[13]:
        cost=16
    elif demo.get() == st_sk[14] and dema.get() == st_sk[15]:
        cost=16
    elif demo.get() == st_sk[14] and dema.get() == st_sk[16]:
        cost=23
    elif demo.get() == st_sk[14] and dema.get() == st_sk[17]:
        cost=26
    elif demo.get() == st_sk[14] and dema.get() == st_sk[18]:
        cost=30
    elif demo.get() == st_sk[14] and dema.get() == st_sk[19]:
        cost=33
    elif demo.get() == st_sk[14] and dema.get() == st_sk[20]:
        cost=37
    elif demo.get() == st_sk[14] and dema.get() == st_sk[21]:
        cost=40
    elif demo.get() == st_sk[14] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == st_sk[14] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[14] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[14] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[14] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[0]:#ราชาเทวี
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[1]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[2]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[3]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[4]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[5]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[6]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[7]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[8]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[9]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[9]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[10]:
        cost=37
    elif demo.get() == st_sk[15] and dema.get() == st_sk[11]:
        cost=30
    elif demo.get() == st_sk[15] and dema.get() == st_sk[12]:
        cost=26
    elif demo.get() == st_sk[15] and dema.get() == st_sk[13]:
        cost=23
    elif demo.get() == st_sk[15] and dema.get() == st_sk[14]:
        cost=16
    elif demo.get() == st_sk[15] and dema.get() == st_sk[16]:
        cost=16
    elif demo.get() == st_sk[15] and dema.get() == st_sk[17]:
        cost=23
    elif demo.get() == st_sk[15] and dema.get() == st_sk[18]:
        cost=26
    elif demo.get() == st_sk[15] and dema.get() == st_sk[19]:
        cost=30
    elif demo.get() == st_sk[15] and dema.get() == st_sk[20]:
        cost=33
    elif demo.get() == st_sk[15] and dema.get() == st_sk[21]:
        cost=37
    elif demo.get() == st_sk[15] and dema.get() == st_sk[22]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == st_sk[15] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[15] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[15] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[0]:#cen
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[10]:
        cost=40
    elif demo.get() == st_sk[16] and dema.get() == st_sk[11]:
        cost=33
    elif demo.get() == st_sk[16] and dema.get() == st_sk[12]:
        cost=30
    elif demo.get() == st_sk[16] and dema.get() == st_sk[13]:
        cost=26
    elif demo.get() == st_sk[16] and dema.get() == st_sk[14]:
        cost=23
    elif demo.get() == st_sk[16] and dema.get() == st_sk[15]:
        cost=16
    elif demo.get() == st_sk[16] and dema.get() == st_sk[17]:
        cost=16
    elif demo.get() == st_sk[16] and dema.get() == st_sk[18]:
        cost=23
    elif demo.get() == st_sk[16] and dema.get() == st_sk[19]:
        cost=26
    elif demo.get() == st_sk[16] and dema.get() == st_sk[20]:
        cost=30
    elif demo.get() == st_sk[16] and dema.get() == st_sk[21]:
        cost=33
    elif demo.get() == st_sk[16] and dema.get() == st_sk[22]:
        cost=37
    elif demo.get() == st_sk[16] and dema.get() == st_sk[23]:
        cost=40
    elif demo.get() == st_sk[16] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[0]:#ชิด
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[11]:
        cost=37
    elif demo.get() == st_sk[17] and dema.get() == st_sk[12]:
        cost=33
    elif demo.get() == st_sk[17] and dema.get() == st_sk[13]:
        cost=30
    elif demo.get() == st_sk[17] and dema.get() == st_sk[14]:
        cost=26
    elif demo.get() == st_sk[17] and dema.get() == st_sk[15]:
        cost=23
    elif demo.get() == st_sk[17] and dema.get() == st_sk[16]:
        cost=16
    elif demo.get() == st_sk[17] and dema.get() == st_sk[18]:
        cost=16
    elif demo.get() == st_sk[17] and dema.get() == st_sk[19]:
        cost=23
    elif demo.get() == st_sk[17] and dema.get() == st_sk[20]:
        cost=26
    elif demo.get() == st_sk[17] and dema.get() == st_sk[21]:
        cost=30
    elif demo.get() == st_sk[17] and dema.get() == st_sk[22]:
        cost=33
    elif demo.get() == st_sk[17] and dema.get() == st_sk[23]:
        cost=37
    elif demo.get() == st_sk[17] and dema.get() == st_sk[24]:
        cost=40
    elif demo.get() == st_sk[17] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == st_sk[18] and dema.get() == st_sk[0]:#เพิน
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == st_sk[11]:
        cost=40
    elif demo.get() == st_sk[18] and dema.get() == st_sk[12]:
        cost=37
    elif demo.get() == st_sk[18] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == st_sk[18] and dema.get() == st_sk[14]:
        cost=30
    elif demo.get() == st_sk[18] and dema.get() == st_sk[15]:
        cost=26
    elif demo.get() == st_sk[18] and dema.get() == st_sk[16]:
        cost=23
    elif demo.get() == st_sk[18] and dema.get() == st_sk[17]:
        cost=16
    elif demo.get() == st_sk[18] and dema.get() == st_sk[19]:
        cost=16
    elif demo.get() == st_sk[18] and dema.get() == st_sk[20]:
        cost=23
    elif demo.get() == st_sk[18] and dema.get() == st_sk[21]:
        cost=26
    elif demo.get() == st_sk[18] and dema.get() == st_sk[22]:
        cost=30
    elif demo.get() == st_sk[18] and dema.get() == st_sk[23]:
        cost=33
    elif demo.get() == st_sk[18] and dema.get() == st_sk[24]:
        cost=37
    elif demo.get() == st_sk[18] and dema.get() == st_sk[25]:
        cost=40
    elif demo.get() == st_sk[18] and dema.get() == st_sk[26]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[27]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[28]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[29]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[30]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[31]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[32]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[33]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[34]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[35]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[36]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[37]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[38]:
        cost=55
    elif demo.get() == st_sk[18] and dema.get() == st_sk[39]:
        cost=55
    elif demo.get() == st_sk[19] and dema.get() == st_sk[0]:#นานา
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == st_sk[12]:
        cost=40
    elif demo.get() == st_sk[19] and dema.get() == st_sk[13]:
        cost=37
    elif demo.get() == st_sk[19] and dema.get() == st_sk[14]:
        cost=33
    elif demo.get() == st_sk[19] and dema.get() == st_sk[15]:
        cost=30
    elif demo.get() == st_sk[19] and dema.get() == st_sk[16]:
        cost=26
    elif demo.get() == st_sk[19] and dema.get() == st_sk[17]:
        cost=23
    elif demo.get() == st_sk[19] and dema.get() == st_sk[18]:
        cost=16
    elif demo.get() == st_sk[19] and dema.get() == st_sk[20]:
        cost=16
    elif demo.get() == st_sk[19] and dema.get() == st_sk[21]:
        cost=23
    elif demo.get() == st_sk[19] and dema.get() == st_sk[22]:
        cost=26
    elif demo.get() == st_sk[19] and dema.get() == st_sk[23]:
        cost=30
    elif demo.get() == st_sk[19] and dema.get() == st_sk[24]:
        cost=33
    elif demo.get() == st_sk[19] and dema.get() == st_sk[25]:
        cost=37
    elif demo.get() == st_sk[19] and dema.get() == st_sk[26]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[27]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[28]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[29]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[30]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[31]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[32]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[33]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[34]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[35]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[36]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[37]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[38]:
        cost=52
    elif demo.get() == st_sk[19] and dema.get() == st_sk[39]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[0]:#อโศก
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[13]:
        cost=40
    elif demo.get() == st_sk[20] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[20] and dema.get() == st_sk[15]:
        cost=33
    elif demo.get() == st_sk[20] and dema.get() == st_sk[16]:
        cost=30
    elif demo.get() == st_sk[20] and dema.get() == st_sk[17]:
        cost=26
    elif demo.get() == st_sk[20] and dema.get() == st_sk[18]:
        cost=23
    elif demo.get() == st_sk[20] and dema.get() == st_sk[19]:
        cost=16
    elif demo.get() == st_sk[20] and dema.get() == st_sk[21]:
        cost=16
    elif demo.get() == st_sk[20] and dema.get() == st_sk[22]:
        cost=23
    elif demo.get() == st_sk[20] and dema.get() == st_sk[23]:
        cost=26
    elif demo.get() == st_sk[20] and dema.get() == st_sk[24]:
        cost=30
    elif demo.get() == st_sk[20] and dema.get() == st_sk[25]:
        cost=33
    elif demo.get() == st_sk[20] and dema.get() == st_sk[26]:
        cost=37
    elif demo.get() == st_sk[20] and dema.get() == st_sk[27]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[28]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[29]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[30]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[31]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[32]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[33]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[34]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[35]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[36]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[37]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[38]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[39]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[0]:#อโศก
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == st_sk[13]:
        cost=40
    elif demo.get() == st_sk[20] and dema.get() == st_sk[14]:
        cost=37
    elif demo.get() == st_sk[20] and dema.get() == st_sk[15]:
        cost=33
    elif demo.get() == st_sk[20] and dema.get() == st_sk[16]:
        cost=30
    elif demo.get() == st_sk[20] and dema.get() == st_sk[17]:
        cost=26
    elif demo.get() == st_sk[20] and dema.get() == st_sk[18]:
        cost=23
    elif demo.get() == st_sk[20] and dema.get() == st_sk[19]:
        cost=16
    elif demo.get() == st_sk[20] and dema.get() == st_sk[21]:
        cost=16
    elif demo.get() == st_sk[20] and dema.get() == st_sk[22]:
        cost=23
    elif demo.get() == st_sk[20] and dema.get() == st_sk[23]:
        cost=26
    elif demo.get() == st_sk[20] and dema.get() == st_sk[24]:
        cost=30
    elif demo.get() == st_sk[20] and dema.get() == st_sk[25]:
        cost=33
    elif demo.get() == st_sk[20] and dema.get() == st_sk[26]:
        cost=37
    elif demo.get() == st_sk[20] and dema.get() == st_sk[27]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[28]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[29]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[30]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[31]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[32]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[33]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[34]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[35]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[36]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[37]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[38]:
        cost=52
    elif demo.get() == st_sk[20] and dema.get() == st_sk[39]:
        cost=52
    elif demo.get() == st_sk[21] and dema.get() == st_sk[0]:#พร้อมพง
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[13]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == st_sk[14]:
        cost=40
    elif demo.get() == st_sk[21] and dema.get() == st_sk[15]:
        cost=37
    elif demo.get() == st_sk[21] and dema.get() == st_sk[16]:
        cost=33
    elif demo.get() == st_sk[21] and dema.get() == st_sk[17]:
        cost=30
    elif demo.get() == st_sk[21] and dema.get() == st_sk[18]:
        cost=26
    elif demo.get() == st_sk[21] and dema.get() == st_sk[19]:
        cost=23
    elif demo.get() == st_sk[21] and dema.get() == st_sk[20]:
        cost=16
    elif demo.get() == st_sk[21] and dema.get() == st_sk[22]:
        cost=16
    elif demo.get() == st_sk[21] and dema.get() == st_sk[23]:
        cost=23
    elif demo.get() == st_sk[21] and dema.get() == st_sk[24]:
        cost=26
    elif demo.get() == st_sk[21] and dema.get() == st_sk[25]:
        cost=30
    elif demo.get() == st_sk[21] and dema.get() == st_sk[26]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[27]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[28]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[29]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[30]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[31]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[32]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[33]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[34]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[35]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[36]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[37]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[38]:
        cost=45
    elif demo.get() == st_sk[21] and dema.get() == st_sk[39]:
        cost=45
    elif demo.get() == st_sk[22] and dema.get() == st_sk[0]:#พร้อมพง
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[13]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[14]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == st_sk[15]:
        cost=40
    elif demo.get() == st_sk[22] and dema.get() == st_sk[16]:
        cost=37
    elif demo.get() == st_sk[22] and dema.get() == st_sk[17]:
        cost=33
    elif demo.get() == st_sk[22] and dema.get() == st_sk[18]:
        cost=30
    elif demo.get() == st_sk[22] and dema.get() == st_sk[19]:
        cost=26
    elif demo.get() == st_sk[22] and dema.get() == st_sk[20]:
        cost=23
    elif demo.get() == st_sk[22] and dema.get() == st_sk[21]:
        cost=16
    elif demo.get() == st_sk[22] and dema.get() == st_sk[23]:
        cost=16
    elif demo.get() == st_sk[22] and dema.get() == st_sk[24]:
        cost=23
    elif demo.get() == st_sk[22] and dema.get() == st_sk[25]:
        cost=26
    elif demo.get() == st_sk[22] and dema.get() == st_sk[26]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[27]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[28]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[29]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[30]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[31]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[32]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[33]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[34]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[35]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[36]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[37]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[38]:
        cost=41
    elif demo.get() == st_sk[22] and dema.get() == st_sk[39]:
        cost=41
    elif demo.get() == st_sk[23] and dema.get() == st_sk[0]:#ทองหล่อ
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[13]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[14]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[15]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == st_sk[16]:
        cost=40
    elif demo.get() == st_sk[23] and dema.get() == st_sk[17]:
        cost=37
    elif demo.get() == st_sk[23] and dema.get() == st_sk[18]:
        cost=33
    elif demo.get() == st_sk[23] and dema.get() == st_sk[19]:
        cost=30
    elif demo.get() == st_sk[23] and dema.get() == st_sk[20]:
        cost=26
    elif demo.get() == st_sk[23] and dema.get() == st_sk[21]:
        cost=23
    elif demo.get() == st_sk[23] and dema.get() == st_sk[22]:
        cost=16
    elif demo.get() == st_sk[23] and dema.get() == st_sk[24]:
        cost=16
    elif demo.get() == st_sk[23] and dema.get() == st_sk[25]:
        cost=23
    elif demo.get() == st_sk[23] and dema.get() == st_sk[26]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[27]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[28]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[29]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[30]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[31]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[32]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[33]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[34]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[35]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[36]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[37]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[38]:
        cost=38
    elif demo.get() == st_sk[23] and dema.get() == st_sk[39]:
        cost=38
    elif demo.get() == st_sk[24] and dema.get() == st_sk[0]:#เพระขโนง
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[13]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[14]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[15]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == st_sk[17]:
        cost=40
    elif demo.get() == st_sk[24] and dema.get() == st_sk[18]:
        cost=37
    elif demo.get() == st_sk[24] and dema.get() == st_sk[19]:
        cost=33
    elif demo.get() == st_sk[24] and dema.get() == st_sk[20]:
        cost=30
    elif demo.get() == st_sk[24] and dema.get() == st_sk[21]:
        cost=26
    elif demo.get() == st_sk[24] and dema.get() == st_sk[22]:
        cost=23
    elif demo.get() == st_sk[24] and dema.get() == st_sk[23]:
        cost=16
    elif demo.get() == st_sk[24] and dema.get() == st_sk[25]:
        cost=16
    elif demo.get() == st_sk[24] and dema.get() == st_sk[26]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[27]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[28]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[29]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[30]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[31]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[32]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[33]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[34]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[35]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[36]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[37]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[38]:
        cost=31
    elif demo.get() == st_sk[24] and dema.get() == st_sk[39]:
        cost=31
    elif demo.get() == st_sk[25] and dema.get() == st_sk[0]:#อ่อนนุช
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[13]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[14]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[15]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == st_sk[18]:
        cost=40
    elif demo.get() == st_sk[25] and dema.get() == st_sk[19]:
        cost=37
    elif demo.get() == st_sk[25] and dema.get() == st_sk[20]:
        cost=33
    elif demo.get() == st_sk[25] and dema.get() == st_sk[21]:
        cost=30
    elif demo.get() == st_sk[25] and dema.get() == st_sk[22]:
        cost=26
    elif demo.get() == st_sk[25] and dema.get() == st_sk[23]:
        cost=23
    elif demo.get() == st_sk[25] and dema.get() == st_sk[24]:
        cost=16
    elif demo.get() == st_sk[25] and dema.get() == st_sk[26]:
        cost=16
    elif demo.get() == st_sk[25] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[30]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[31]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[32]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[33]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[34]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[35]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[36]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[37]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[38]:
        cost=15
    elif demo.get() == st_sk[25] and dema.get() == st_sk[39]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[0]:#บางจาก
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[26] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[26] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[26] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[26] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[26] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[26] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[26] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[30]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[31]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[32]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[33]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[34]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[35]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[36]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[37]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[38]:
        cost=15
    elif demo.get() == st_sk[26] and dema.get() == st_sk[39]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[0]:#ปุณณวิธี
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[27] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[27] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[27] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[27] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[27] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[27] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[27] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[30]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[31]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[32]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[33]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[34]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[35]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[36]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[37]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[38]:
        cost=15
    elif demo.get() == st_sk[27] and dema.get() == st_sk[39]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[0]:#อุดม
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[28] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[28] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[28] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[28] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[28] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[28] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[28] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[30]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[31]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[32]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[33]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[34]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[35]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[36]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[37]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[38]:
        cost=15
    elif demo.get() == st_sk[28] and dema.get() == st_sk[39]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[0]:#บางนา
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[29] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[29] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[29] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[29] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[29] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[29] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[29] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[30]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[31]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[32]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[33]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[34]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[35]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[36]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[37]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[38]:
        cost=15
    elif demo.get() == st_sk[29] and dema.get() == st_sk[39]:
        cost=15
    elif demo.get() == st_sk[30] and dema.get() == st_sk[0]:#เเบริ่ง
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[30] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[30] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[30] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[30] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[30] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[30] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[30] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[30] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[30] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[30] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[30] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[30] and dema.get() == st_sk[31]:
        cost=0
    elif demo.get() == st_sk[30] and dema.get() == st_sk[32]:
        cost=0
    elif demo.get() == st_sk[30] and dema.get() == st_sk[33]:
        cost=0
    elif demo.get() == st_sk[30] and dema.get() == st_sk[34]:
        cost=0
    elif demo.get() == st_sk[30] and dema.get() == st_sk[35]:
        cost=0
    elif demo.get() == st_sk[30] and dema.get() == st_sk[36]:
        cost=0
    elif demo.get() == st_sk[30] and dema.get() == st_sk[37]:
        cost=0
    elif demo.get() == st_sk[30] and dema.get() == st_sk[38]:
        cost=0
    elif demo.get() == st_sk[30] and dema.get() == st_sk[39]:
        cost=0
    elif demo.get() == st_sk[31] and dema.get() == st_sk[0]:#สำโรง
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[31] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[31] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[31] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[31] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[31] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[31] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[31] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[31] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[31] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[31] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[31] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[31] and dema.get() == st_sk[30]:
        cost=0
    elif demo.get() == st_sk[31] and dema.get() == st_sk[32]:
        cost=0
    elif demo.get() == st_sk[31] and dema.get() == st_sk[33]:
        cost=0
    elif demo.get() == st_sk[31] and dema.get() == st_sk[34]:
        cost=0
    elif demo.get() == st_sk[31] and dema.get() == st_sk[35]:
        cost=0
    elif demo.get() == st_sk[31] and dema.get() == st_sk[36]:
        cost=0
    elif demo.get() == st_sk[31] and dema.get() == st_sk[37]:
        cost=0
    elif demo.get() == st_sk[31] and dema.get() == st_sk[38]:
        cost=0
    elif demo.get() == st_sk[31] and dema.get() == st_sk[39]:
        cost=0
    elif demo.get() == st_sk[32] and dema.get() == st_sk[0]:#ปู่จ๋า
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[32] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[32] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[32] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[32] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[32] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[32] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[32] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[32] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[32] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[32] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[32] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[32] and dema.get() == st_sk[30]:
        cost=0
    elif demo.get() == st_sk[32] and dema.get() == st_sk[31]:
        cost=0
    elif demo.get() == st_sk[32] and dema.get() == st_sk[33]:
        cost=0
    elif demo.get() == st_sk[32] and dema.get() == st_sk[34]:
        cost=0
    elif demo.get() == st_sk[32] and dema.get() == st_sk[35]:
        cost=0
    elif demo.get() == st_sk[32] and dema.get() == st_sk[36]:
        cost=0
    elif demo.get() == st_sk[32] and dema.get() == st_sk[37]:
        cost=0
    elif demo.get() == st_sk[32] and dema.get() == st_sk[38]:
        cost=0
    elif demo.get() == st_sk[32] and dema.get() == st_sk[39]:
        cost=0
    elif demo.get() == st_sk[33] and dema.get() == st_sk[0]:#ช้างเอราวัณ
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[33] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[33] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[33] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[33] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[33] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[33] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[33] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[33] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[33] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[33] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[33] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[33] and dema.get() == st_sk[30]:
        cost=0
    elif demo.get() == st_sk[33] and dema.get() == st_sk[31]:
        cost=0
    elif demo.get() == st_sk[33] and dema.get() == st_sk[32]:
        cost=0
    elif demo.get() == st_sk[33] and dema.get() == st_sk[34]:
        cost=0
    elif demo.get() == st_sk[33] and dema.get() == st_sk[35]:
        cost=0
    elif demo.get() == st_sk[33] and dema.get() == st_sk[36]:
        cost=0
    elif demo.get() == st_sk[33] and dema.get() == st_sk[37]:
        cost=0
    elif demo.get() == st_sk[33] and dema.get() == st_sk[38]:
        cost=0
    elif demo.get() == st_sk[33] and dema.get() == st_sk[39]:
        cost=0
    elif demo.get() == st_sk[34] and dema.get() == st_sk[0]:#โรงเรียนนายเรือ
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[34] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[34] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[34] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[34] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[34] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[34] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[34] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[34] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[34] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[34] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[34] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[34] and dema.get() == st_sk[30]:
        cost=0
    elif demo.get() == st_sk[34] and dema.get() == st_sk[31]:
        cost=0
    elif demo.get() == st_sk[34] and dema.get() == st_sk[32]:
        cost=0
    elif demo.get() == st_sk[34] and dema.get() == st_sk[33]:
        cost=0
    elif demo.get() == st_sk[34] and dema.get() == st_sk[35]:
        cost=0
    elif demo.get() == st_sk[34] and dema.get() == st_sk[36]:
        cost=0
    elif demo.get() == st_sk[34] and dema.get() == st_sk[37]:
        cost=0
    elif demo.get() == st_sk[34] and dema.get() == st_sk[38]:
        cost=0
    elif demo.get() == st_sk[34] and dema.get() == st_sk[39]:
        cost=0
    elif demo.get() == st_sk[35] and dema.get() == st_sk[0]:#ปากน้ำ
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[35] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[35] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[35] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[35] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[35] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[35] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[35] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[35] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[35] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[35] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[35] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[35] and dema.get() == st_sk[30]:
        cost=0
    elif demo.get() == st_sk[35] and dema.get() == st_sk[31]:
        cost=0
    elif demo.get() == st_sk[35] and dema.get() == st_sk[32]:
        cost=0
    elif demo.get() == st_sk[35] and dema.get() == st_sk[33]:
        cost=0
    elif demo.get() == st_sk[35] and dema.get() == st_sk[34]:
        cost=0
    elif demo.get() == st_sk[35] and dema.get() == st_sk[36]:
        cost=0
    elif demo.get() == st_sk[35] and dema.get() == st_sk[37]:
        cost=0
    elif demo.get() == st_sk[35] and dema.get() == st_sk[38]:
        cost=0
    elif demo.get() == st_sk[35] and dema.get() == st_sk[39]:
        cost=0
    elif demo.get() == st_sk[36] and dema.get() == st_sk[0]:#ศรีนคริน
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[36] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[36] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[36] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[36] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[36] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[36] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[36] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[36] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[36] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[36] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[36] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[36] and dema.get() == st_sk[30]:
        cost=0
    elif demo.get() == st_sk[36] and dema.get() == st_sk[31]:
        cost=0
    elif demo.get() == st_sk[36] and dema.get() == st_sk[32]:
        cost=0
    elif demo.get() == st_sk[36] and dema.get() == st_sk[33]:
        cost=0
    elif demo.get() == st_sk[36] and dema.get() == st_sk[34]:
        cost=0
    elif demo.get() == st_sk[36] and dema.get() == st_sk[35]:
        cost=0
    elif demo.get() == st_sk[36] and dema.get() == st_sk[37]:
        cost=0
    elif demo.get() == st_sk[36] and dema.get() == st_sk[38]:
        cost=0
    elif demo.get() == st_sk[36] and dema.get() == st_sk[39]:
        cost=0
    elif demo.get() == st_sk[37] and dema.get() == st_sk[0]:#เเพรกษา
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[37] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[37] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[37] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[37] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[37] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[37] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[37] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[37] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[37] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[37] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[37] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[37] and dema.get() == st_sk[30]:
        cost=0
    elif demo.get() == st_sk[37] and dema.get() == st_sk[31]:
        cost=0
    elif demo.get() == st_sk[37] and dema.get() == st_sk[32]:
        cost=0
    elif demo.get() == st_sk[37] and dema.get() == st_sk[33]:
        cost=0
    elif demo.get() == st_sk[37] and dema.get() == st_sk[34]:
        cost=0
    elif demo.get() == st_sk[37] and dema.get() == st_sk[35]:
        cost=0
    elif demo.get() == st_sk[37] and dema.get() == st_sk[36]:
        cost=0
    elif demo.get() == st_sk[37] and dema.get() == st_sk[38]:
        cost=0
    elif demo.get() == st_sk[37] and dema.get() == st_sk[39]:
        cost=0
    elif demo.get() == st_sk[38] and dema.get() == st_sk[0]:#สายลวด
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[38] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[38] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[38] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[38] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[38] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[38] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[38] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[38] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[38] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[38] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[38] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[38] and dema.get() == st_sk[30]:
        cost=0
    elif demo.get() == st_sk[38] and dema.get() == st_sk[31]:
        cost=0
    elif demo.get() == st_sk[38] and dema.get() == st_sk[32]:
        cost=0
    elif demo.get() == st_sk[38] and dema.get() == st_sk[33]:
        cost=0
    elif demo.get() == st_sk[38] and dema.get() == st_sk[34]:
        cost=0
    elif demo.get() == st_sk[38] and dema.get() == st_sk[35]:
        cost=0
    elif demo.get() == st_sk[38] and dema.get() == st_sk[36]:
        cost=0
    elif demo.get() == st_sk[38] and dema.get() == st_sk[37]:
        cost=0
    elif demo.get() == st_sk[38] and dema.get() == st_sk[39]:
        cost=0
    elif demo.get() == st_sk[39] and dema.get() == st_sk[0]:#เคหะ
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == st_sk[18]:
        cost=55
    elif demo.get() == st_sk[39] and dema.get() == st_sk[19]:
        cost=52
    elif demo.get() == st_sk[39] and dema.get() == st_sk[20]:
        cost=48
    elif demo.get() == st_sk[39] and dema.get() == st_sk[21]:
        cost=45
    elif demo.get() == st_sk[39] and dema.get() == st_sk[22]:
        cost=41
    elif demo.get() == st_sk[39] and dema.get() == st_sk[23]:
        cost=38
    elif demo.get() == st_sk[39] and dema.get() == st_sk[24]:
        cost=31
    elif demo.get() == st_sk[39] and dema.get() == st_sk[25]:
        cost=15
    elif demo.get() == st_sk[39] and dema.get() == st_sk[26]:
        cost=15
    elif demo.get() == st_sk[39] and dema.get() == st_sk[27]:
        cost=15
    elif demo.get() == st_sk[39] and dema.get() == st_sk[28]:
        cost=15
    elif demo.get() == st_sk[39] and dema.get() == st_sk[29]:
        cost=15
    elif demo.get() == st_sk[39] and dema.get() == st_sk[30]:
        cost=0
    elif demo.get() == st_sk[39] and dema.get() == st_sk[31]:
        cost=0
    elif demo.get() == st_sk[39] and dema.get() == st_sk[32]:
        cost=0
    elif demo.get() == st_sk[39] and dema.get() == st_sk[33]:
        cost=0
    elif demo.get() == st_sk[39] and dema.get() == st_sk[34]:
        cost=0
    elif demo.get() == st_sk[39] and dema.get() == st_sk[35]:
        cost=0
    elif demo.get() == st_sk[39] and dema.get() == st_sk[36]:
        cost=0
    elif demo.get() == st_sk[39] and dema.get() == st_sk[37]:
        cost=0
    elif demo.get() == st_sk[39] and dema.get() == st_sk[38]:
        cost=0
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[1]: #เขียวเข้ม
        cost=23
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[2]:
        cost=26
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[3]:
        cost=30
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[4]:
        cost=33
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[5]:
        cost=37
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[6]:
        cost=40
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[0]: #เขียวเข้ม
        cost=23
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[2]:
        cost=16
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[5]:
        cost=30
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[6]:
        cost=33
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[7]:
        cost=37
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[8]:
        cost=40
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[10]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[3]:
        cost=23
    elif demo.get() == sl_sd[1] and dema.get() == sl_sd[4]:
        cost=26
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[0]: #เขียวเข้ม
        cost=26
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[1]:
        cost=16
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[5]:
        cost=26
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[6]:
        cost=30
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[8]:
        cost=37
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[9]:
        cost=52
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[10]:
        cost=52
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[11]:
        cost=52
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[12]:
        cost=52
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[7]:
        cost=33
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[3]:
        cost=16
    elif demo.get() == sl_sd[2] and dema.get() == sl_sd[4]:
        cost=23
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[1]: #เขียวเข้ม
        cost=23
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[2]:
        cost=16
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[6]:
        cost=26
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[0]:
        cost=30
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[5]:
        cost=23
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[9]:
        cost=48
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[10]:
        cost=48
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[11]:
        cost=48
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[12]:
        cost=48
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[8]:
        cost=33
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[7]:
        cost=30
    elif demo.get() == sl_sd[3] and dema.get() == sl_sd[4]:
        cost=16
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[1]: #เขียวเข้ม
        cost=16
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[2]:
        cost=23
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[6]:
        cost=23
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[0]:
        cost=33
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[5]:
        cost=16
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[9]:
        cost=45
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[10]:
        cost=45
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[11]:
        cost=45
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[12]:
        cost=45
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[8]:
        cost=30
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[7]:
        cost=26
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == sl_sd[3]:
        cost=16
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[1]: #เขียวเข้ม
        cost=23
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[2]:
        cost=16
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[6]:
        cost=16
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[0]:
        cost=30
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[5]:
        cost=23
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[9]:
        cost=48
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[10]:
        cost=48
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[11]:
        cost=48
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[12]:
        cost=48
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[8]:
        cost=33
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[7]:
        cost=30
    elif demo.get() == sl_sd[5] and dema.get() == sl_sd[4]:
        cost=16
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[1]: #เขียวเข้ม
        cost=40
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[2]:
        cost=33
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[3]:
        cost=30
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[0]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[5]:
        cost=23
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[9]:
        cost=31
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[10]:
        cost=31
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[11]:
        cost=31
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[12]:
        cost=31
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[8]:
        cost=16
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[7]:
        cost=16
    elif demo.get() == sl_sd[6] and dema.get() == sl_sd[4]:
        cost=26
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[0]: #เขียวเข้ม
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[1]:
        cost=37
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[2]:
        cost=33
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[3]:
        cost=30
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[4]:
        cost=26
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[5]:
        cost=23
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[6]:
        cost=16
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[8]:
        cost=16
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[9]:
        cost=15
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[10]:
        cost=15
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[11]:
        cost=15
    elif demo.get() == sl_sd[7] and dema.get() == sl_sd[12]:
        cost=15
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[0]: #เขียวเข้ม
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[1]:
        cost=40
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[2]:
        cost=37
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[3]:
        cost=33
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[4]:
        cost=10
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[5]:
        cost=26
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[6]:
        cost=16
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[7]:
        cost=16
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[9]:
        cost=15
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[10]:
        cost=15
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[11]:
        cost=15
    elif demo.get() == sl_sd[8] and dema.get() == sl_sd[12]:
        cost=15
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[0]: #เขียวเข้ม
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[1]:
        cost=55
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[2]:
        cost=52
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[3]:
        cost=48
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[4]:
        cost=45
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[5]:
        cost=41
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[6]:
        cost=31
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[7]:
        cost=31
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[8]:
        cost=15
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[10]:
        cost=15
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[11]:
        cost=15
    elif demo.get() == sl_sd[9] and dema.get() == sl_sd[12]:
        cost=15
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[0]: #เขียวเข้ม
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[1]:
        cost=55
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[2]:
        cost=52
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[3]:
        cost=48
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[4]:
        cost=45
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[5]:
        cost=41
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[6]:
        cost=31
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[7]:
        cost=31
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[8]:
        cost=15
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[9]:
        cost=15
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[11]:
        cost=15
    elif demo.get() == sl_sd[10] and dema.get() == sl_sd[12]:
        cost=15
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[0]: #เขียวเข้ม
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[1]:
        cost=55
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[2]:
        cost=52
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[3]:
        cost=48
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[4]:
        cost=45
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[5]:
        cost=41
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[6]:
        cost=31
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[7]:
        cost=31
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[8]:
        cost=15
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[9]:
        cost=15
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[10]:
        cost=15
    elif demo.get() == sl_sd[11] and dema.get() == sl_sd[12]:
        cost=15
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[0]: #เขียวเข้ม
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[1]:
        cost=55
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[2]:
        cost=52
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[3]:
        cost=48
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[4]:
        cost=45
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[5]:
        cost=41
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[6]:
        cost=31
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[7]:
        cost=31
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[8]:
        cost=15
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[9]:
        cost=15
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[10]:
        cost=15
    elif demo.get() == sl_sd[12] and dema.get() == sl_sd[11]:
        cost=15
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[0] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[1] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[2] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[3] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[4] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[5] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[6] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[7] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[8] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[9] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[10] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้มari
        cost=37
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[1]:
        cost=37
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[2]:
        cost=40
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[9]:
        cost=44
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[11] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้มsnampoi
        cost=33
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[1]:
        cost=33
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[2]:
        cost=37
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[3]:
        cost=40
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[12] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=30
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[1]:
        cost=30
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[2]:
        cost=33
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[3]:
        cost=37
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[4]:
        cost=40
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[13] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=26
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[1]:
        cost=26
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[2]:
        cost=30
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[3]:
        cost=33
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[4]:
        cost=37
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[5]:
        cost=40
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[14] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=23
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[1]:
        cost=23
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[2]:
        cost=26
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[3]:
        cost=30
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[4]:
        cost=33
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[5]:
        cost=37
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[6]:
        cost=40
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[15] and dema.get() == sl_sd[12]:
        cost=59    
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=16
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[1]:
        cost=16
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[2]:
        cost=23
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[3]:
        cost=26
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[4]:
        cost=30
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[5]:
        cost=33
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[6]:
        cost=37
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[7]:
        cost=40
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[16] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=23
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[1]:
        cost=23
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[2]:
        cost=26
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[3]:
        cost=30
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[4]:
        cost=33
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[5]:
        cost=37
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[6]:
        cost=40
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[17] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=26
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[1]:
        cost=26
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[2]:
        cost=30
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[3]:
        cost=33
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[4]:
        cost=37
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[5]:
        cost=40
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[18] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=26
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[1]:
        cost=26
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[2]:
        cost=30
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[3]:
        cost=33
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[4]:
        cost=37
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[5]:
        cost=40
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[19] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=30
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[1]:
        cost=30
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[2]:
        cost=33
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[3]:
        cost=37
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[4]:
        cost=40
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[20] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=33
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[1]:
        cost=33
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[2]:
        cost=37
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[3]:
        cost=40
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[21] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=37
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[1]:
        cost=37
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[2]:
        cost=40
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[22] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=40
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[1]:
        cost=40
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[23] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[24] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[0]:#เขียวไปเขียวเข้ม
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[1]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[2]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[3]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[5]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[6]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[7]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[8]:
        cost=44
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[25] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[26] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[27] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[28] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[29] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[30] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[31] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[32] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[33] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[34] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[35] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[36] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[37] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[38] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[0]:#59
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[1]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[2]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[3]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[4]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[5]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[6]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[7]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[8]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[9]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[10]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[11]:
        cost=59
    elif demo.get() == st_sk[39] and dema.get() == sl_sd[12]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[11]:
        cost=37
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[12]:
        cost=33
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[13]:
        cost=30
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[14]:
        cost=26
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[15]:
        cost=23
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[16]:
        cost=16
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[17]:
        cost=23
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[18]:
        cost=26
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[19]:
        cost=30
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[20]:
        cost=33
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[21]:
        cost=37
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[22]:
        cost=40
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[0] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว2
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[11]:
        cost=37
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[12]:
        cost=33
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[13]:
        cost=30
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[14]:
        cost=26
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[15]:
        cost=23
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[16]:
        cost=16
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[17]:
        cost=23
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[18]:
        cost=26
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[19]:
        cost=30
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[20]:
        cost=33
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[21]:
        cost=37
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[22]:
        cost=40
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[1] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[11]:
        cost=40
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[12]:
        cost=37
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[13]:
        cost=33
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[14]:
        cost=30
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[15]:
        cost=26
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[16]:
        cost=23
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[17]:
        cost=26
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[18]:
        cost=30
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[19]:
        cost=33
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[20]:
        cost=37
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[21]:
        cost=40
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[2] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว3
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[12]:
        cost=40
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[13]:
        cost=37
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[14]:
        cost=33
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[15]:
        cost=30
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[16]:
        cost=26
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[17]:
        cost=30
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[18]:
        cost=33
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[19]:
        cost=37
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[20]:
        cost=40
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[3] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[1]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[2]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[3]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[4]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[5]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[6]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[7]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[8]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[9]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[10]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[11]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[12]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[13]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[14]:
        cost=40
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[15]:
        cost=37
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[16]:
        cost=33
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[17]:
        cost=30
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[18]:
        cost=26
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[19]:
        cost=30
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[20]:
        cost=33
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[21]:
        cost=37
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[22]:
        cost=40
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[23]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[24]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[25]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[26]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[27]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[28]:
        cost=44
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[29]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[30]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[31]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[32]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[33]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[34]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[35]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[36]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[37]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[38]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[4] and dema.get() == st_sk[39]:
        cost=59
        case="หมายเหตุ: สถานนี ศึกษาวิทยา อยู่ระหว่างการก่อสร้าง"
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[13]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[14]:
        cost=40
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[15]:
        cost=37
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[16]:
        cost=33
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[17]:
        cost=37
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[18]:
        cost=40
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[5] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[13]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[14]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[15]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[16]:
        cost=40
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[6] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[13]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[14]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[15]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[16]:
        cost=40
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[7] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[1]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[2]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[3]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[4]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[5]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[6]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[7]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[8]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[9]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[10]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[11]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[12]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[13]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[14]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[15]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[16]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[17]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[18]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[19]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[20]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[21]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[22]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[23]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[24]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[25]:
        cost=44
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[8] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[18]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[19]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[20]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[21]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[22]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[23]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[24]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[25]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[9] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[18]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[19]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[20]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[21]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[22]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[23]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[24]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[25]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[10] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[18]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[19]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[20]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[21]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[22]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[23]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[24]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[25]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[11] and dema.get() == st_sk[39]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[0]:#เขียวเข้มไปเขียว
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[1]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[2]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[3]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[4]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[5]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[6]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[7]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[8]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[9]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[10]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[11]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[12]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[13]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[14]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[15]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[16]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[17]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[18]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[19]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[20]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[21]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[22]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[23]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[24]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[25]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[26]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[27]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[28]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[29]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[30]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[31]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[32]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[33]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[34]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[35]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[36]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[37]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[38]:
        cost=59
    elif demo.get() == sl_sd[12] and dema.get() == st_sk[39]:
        cost=59
    else:
        cost=00
        

    if case != "":
        messagebox.showwarning("หมายเหตุ",case)
    po=Label(w2,text="จากสถานี:",font=("Angsana New",50,"bold"),bg=fak2,fg="White").grid(row=0,column=0)
    fisa=Label(w2,text=demo.get(),font=("Angsana New",50),bg=fak2,fg="White").grid(row=0,column=1)
    pou=Label(w2,text="  ถึงสถานี:",font=("Angsana New",50,"bold"),bg=fak2,fg="White").grid(row=1,column=0)
    fisb=Label(w2,text=dema.get(),font=("Angsana New",50),bg=fak2,fg="White").grid(row=1,column=1)
    po1=Label(w2,text="เป็นเงิน "+str(cost)+" บาท",font=("Angsana New",40),bg=fak2,fg="White").grid(row=2,column=0,columnspan=2,padx=10)
    if rb.get() == 3:
        dis=cost*50//100
        tot=cost-dis
        if cost == 59:
            tot-=1
        dec="Senior card "
    elif rb.get() == 4:
        if cost > 44:
            dis=cost*8//100
            tot=cost-dis-1
        else:
            tot=cost
        dec="Student Card "
    elif rb.get() == 2:
        tot=cost
        dec="Adult Card "
    else:
        tot=cost
        dec="Single Journey Card "
    po3=Label(w2,text="หากจ่ายด้วยบัตร "+dec+" จะเป็นเงิน "+str(tot)+" บาท",font=("Angsana New",20),bg=fak2,fg="White").grid(row=3,column=0,columnspan=2)
    with open("log.txt","a",encoding="utf-8")as tth:
            tth.write("ต้นทาง "+demo.get())
            tth.write(" ปลายทาง "+dema.get())
            tth.write(" จ่ายด้วยบัตร "+dec)
            tth.write(str(tot)+" บาท")
            tth.write(time+"\n")
            
            
sta=LabelFrame(w1,text="สถานีต้นทาง", padx=kkph,pady=kkpp,font=("Angsana New",12),bg=fak1,fg="White")
sta.grid(row=0,column=0,padx=strok+1)

line_list = ["สายสีเขียว",  "สายสีเขียวเข้ม"]
line2_list= ["สายสีเขียว",  "สายสีเขียวเข้ม"]

lb1 =ttk.Combobox(sta, values=line_list,state="readonly",font=("Angsana New",15))
lb1.grid()
lb1.set("เลือกสายของต้นทาง")
lb1.bind("<<ComboboxSelected>>",Stan)



stb=LabelFrame(w1, text="สถานีปลายทาง", padx=kkph,pady=kkpp,font=("Angsana New",12),bg=fak1,fg="White")
stb.grid(row=0,column=1,padx=strok)

tee=ttk.Combobox(sta ,width=19,state="disable",font=("Angsana New",12)).grid(column=0,row=1,pady=strok)
"""con1=Button(sta,text="เลือก",font=("Angsana New",13),state="disable",command=MicroA)
con1.grid()"""

lb2 =ttk.Combobox(stb,values=line_list,state="disable",font=("Angsana New",15))
lb2.grid()
lb2.set("เลือกสายของปลายทาง")
lb2.bind("<<ComboboxSelected>>",Stbn)

too=ttk.Combobox(stb ,width=19,state="disable",font=("Angsana New",12)).grid(column=0,row=1,pady=strok)
"""con2=Button(stb,text="เลือก",font=("Angsana New",13),state="disable",command=MicroB)
con2.grid()"""

final=Frame(w1,pady=20,bg=fak1)

fnala=Label(final,text="    สถานีต้นทาง:",font=("Angsana New",20),bg=fak1,fg="White").grid(pady=2,row=0,column=0)
fnalb=Label(final,text="สถานีปลายทาง:",font=("Angsana New",20),bg=fak1,fg="White").grid(pady=2,row=1,column=0)


ffa=Label(final,font=("Angsana New",20),bg=fak1,fg="White")
ffa.grid(pady=2,row=0,column=1)
ffb=Label(final,font=("Angsana New",20),bg=fak1,fg="White")
ffb.grid(pady=2,row=1,column=1)


card=LabelFrame(w1, text="ชนิดของบัตร",font=("Angsana New",18),bg=fak1,fg="White")

rb=IntVar()
rb.set(1)

h1=Radiobutton(card,value=1,variable=rb,image=im1,bg=fak1)
h1.grid(row=0,column=0)

h2=Radiobutton(card,value=2,variable=rb,image=im2,bg=fak1)
h2.grid(row=0,column=1)

h3=Radiobutton(card,value=3,variable=rb,image=im4,bg=fak1)
h3.grid(row=0,column=2)

h4=Radiobutton(card,value=4,variable=rb,image=im3,bg=fak1)
h4.grid(row=0,column=3)

final.grid(row=1,column=0,columnspan=2)
card.grid(row=2,column=0,columnspan=2)

hh=Button(w1, text="Accept",command=Ennn,state="disable",padx=19,pady=10,font=("Angsana New",18),bg=fak2,fg="White")
hh.grid(row=7,column=0,columnspan=2,pady=15)

w1.config(menu=gg)
w1.mainloop()

