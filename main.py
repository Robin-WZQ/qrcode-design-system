#=============================
# Create by Robin-WZQ
# Time: 2021/8/2 (version_2.0)
# JUST FOR FUN!
#============================

import tkinter
import tkinter.filedialog
from PIL import Image,ImageTk
from torchvision import transforms as transforms
import os
from MyQR import myqr


#create an UI 
win = tkinter.Tk()
win.title("picture process")
win.geometry("1280x1080")

#declare the global variable
original = Image.new('RGB', (300, 400))
save_img = Image.new('RGB', (300, 400))
count = 0
e2 = None
e2 = str(e2)
file_name = None
img2 = tkinter.Label(win)

#choose a picture 
def choose_file():
	select_file = tkinter.filedialog.askopenfilename(title='选择图片')
	global file_name
	file_name=select_file
	e.set(select_file)
	load = Image.open(select_file)
	load = transforms.Resize((300,400))(load)
	#declare the global variable
	global original
	original = load
	render = ImageTk.PhotoImage(load)
	img  = tkinter.Label(win,image=render)
	img.image = render
	img.place(x=100,y=100)

#get the input information from client and then generate the Qrcode
def qrcode_generate():
    root = tkinter.Tk()
    tkinter.Label(root,text='Please input the content or link').grid(row=0,column=0)
    v1=tkinter.StringVar()    # declare variable . 
    e1 = tkinter.Entry(root,textvariable=v1)            # store the information   
    e1.grid(row=0,column=1,padx=10,pady=5)      # design .
    def show():
        e2 = e1.get()
        myqr.run(
            words= e2,
            picture=file_name,
            version=5,
            contrast=1.0,
            brightness=1.0,
            save_name="picture_qrcode.png",
            colorized=True,
        )

        new_img = Image.open('picture_qrcode.png')
        render = ImageTk.PhotoImage(new_img)
        global img2
        img2.destroy()
        img2  = tkinter.Label(win,image=render)
        img2.image = render
        img2.place(x=800,y=100)
    tkinter.Button(root,text='确认',width=10,command = show).grid(row=3,column=0,padx=10,pady=5)  #design function 

#show the path
e = tkinter.StringVar()
e_entry = tkinter.Entry(win, width=68, textvariable=e)
e_entry.pack()

#set up the botton of showing the pictures
button1 = tkinter.Button(win, text ="Select", command = choose_file)
button1.pack()

button2 = tkinter.Button(win, text="QRcode" , command = qrcode_generate,width=20,height =1)
button2.place(x=570,y=300)


#set up label to original image and the modified image respectively
label1 = tkinter.Label(win,text="Original Picture")
label1.place(x=200,y=50)

label2 = tkinter.Label(win,text="Your QRcode!")
label2.place(x=900,y=50)


#set the exit botton
button0 = tkinter.Button(win,text="Exit",command=win.quit,width=20,height =1)
button0.place(x=570,y=650)
win.mainloop()
