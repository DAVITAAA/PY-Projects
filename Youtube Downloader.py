import customtkinter
from tkinter import *
from tkinter import messagebox
from pytube import YouTube

def popup(event):
    try:
        menu.tk_popup(event.x_root,event.y_root) # Pop the menu up in the given coordinates
    finally:
        menu.grab_release() # Release it once an option is selected
    
def paste():
    clipboard = root.clipboard_get() # Get the copied item from system clipboard
    entry1.insert('end',clipboard) # Insert the item into the entry widge

def copy():
    inp = entry1.get() # Get the text inside entry widget
    root.clipboard_show() # show the tkinter clipboard
    root.clipboard_append(inp) # Append to system clipboard


def downloader():
    try:
        if entry1.get() == "":
            messagebox.showerror(message="Something went wrong")
        else:
            url = YouTube(str(link.get()),on_progress_callback=on_progress)
        if res_menu.get() == "1080P":
            video = url.streams.get_highest_resolution()
            #video.download('C:\\Users\\Administrator\\Desktop\\tuxa')
            finish_label.configure(Text="Downloaded")
        elif res_menu.get() == "720P":
            video = url.streams.filter(res="720p").first()
            #video.download('C:\\Users\\Administrator\\Desktop\\tuxa')
            finish_label.configure(Text="Downloaded")
        elif res_menu.get() == "MP3":
            video = url.streams.get_audio_only()
            #video.download('C:\\Users\\Administrator\\Desktop\\tuxa')
            finish_label.configure(Text="Downloaded")
        elif res_menu.get() == "480P":
            video = url.streams.get_by_resolution("480P")
            #video.download('C:\\Users\\Administrator\\Desktop\\tuxa')
            finish_label.configure(Text="Downloaded")
        else:
            print("Invalid resolution selected")
    except Exception as e:
        messagebox.showinfo(message="Downloaded")

def on_progress(stream, chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text = per + '%')
    pPercentage.update()

    progressbar.set(float(percentage_of_compeletion)/100)


customtkinter.set_appearance_mode("dark")
customtkinter.set_appearance_mode("dark")


root = customtkinter.CTk()
root.geometry("600x440+570+200")

frame = Frame(master=root,bg="Black")
frame.pack(fill="both",expand=True)

top_label = customtkinter.CTkLabel(master=frame,text="Youtube Downloader",font=("Roboto",30))
top_label.pack(pady=10,padx=10)

menu_label = customtkinter.CTkLabel(master=frame,text="აირჩიეთ ხარისხი: ")
menu_label.place(x=15,y=100)

resolutions = ["1080P",
                "720P",
                "480P",
                "MP3"]

resolution1=StringVar()

link = StringVar()


res_menu = customtkinter.CTkComboBox(master=frame,values=resolutions)
res_menu.place(x=10,y=130)

download_button = customtkinter.CTkButton(master=frame,text="Download",command=downloader)
download_button.place(x=400,y=130)


entry1 = customtkinter.CTkEntry(master=frame,textvariable=link,width=600,font=("arial",20),placeholder_text="Enter URL: ",corner_radius=65)
entry1.pack(pady =2,padx=2)
entry1.bind('<Button-3>',popup)

pPercentage = customtkinter.CTkLabel(root, text="%",fg_color="black")
pPercentage.place(x=500,y=200)

progressbar = customtkinter.CTkProgressBar(root,width=400,height=10)
progressbar.set(0)
progressbar.place(x=80,y=208)

menu = Menu(root,tearoff=0)
menu.add_command(label='Copy',command=copy) # Create labels and commands
menu.add_command(label='Paste',command=paste)

finish_label = customtkinter.CTkLabel(frame,text="")
finish_label.pack()


root.mainloop()