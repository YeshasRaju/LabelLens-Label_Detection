import requests
from customtkinter import *
import PIL
from PIL import Image, ImageTk
import cv2
import torch
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/last.pt', force_reload=True)

def process_frame(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(rgb_frame)
    rendered_frame = np.squeeze(results.render())
    bgr_frame = cv2.cvtColor(rendered_frame, cv2.COLOR_RGB2BGR)
    for result in results.xyxy[0]:
        class_id = int(result[5])
        label_name = results.names[class_id]
        present_labels.append(label_name)
    for i in labels:
        if i in present_labels:
            act_labels[labels.index(i)].configure(image=check)
        else:
            act_labels[labels.index(i)].configure(image=cross)
    checking = all(e in present_labels for e in labels)
    if checking == True:
        p_or_f.configure(text="PASS",fg_color="green")
    else:
        p_or_f.configure(text="FAIL",fg_color="red")
    present_labels.clear()
    return bgr_frame

def update_frame():
    if not paused:
        ret, frame = cap.read()
        if not ret:
            print("Error ")
            return
        frame = cv2.resize(frame, (800,800))
        processed_frame = process_frame(frame)
        image = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(image=image)
        top_label.imgtk = imgtk
        top_label.configure(image=imgtk)
    window.after(10, update_frame)

def toggle_pause(event):
    global paused
    paused = not paused

def choices(choice):
    global labels, act_labels, sam_act_labels, onep_act_labels, all_act_labels
    for lab in act_labels:
        lab.destroy()

    labels.clear()
    act_labels.clear()
    sam_act_labels.clear()
    onep_act_labels.clear()
    all_act_labels.clear()
    if choice == "Samsung":
        create_labels(samsung_labels, sam_act_labels)
    elif choice == "OnePlus":
        create_labels(oneplus_labels, onep_act_labels)
    elif choice == "All":
        create_labels(all_labels, all_act_labels)


def create_labels(label_list, act_label_list):
    for i in range(len(label_list)):
        col = i % 2
        row = (2 * (i // 2))
        test_label = CTkLabel(image=cross, text=label_list[i] + "\n\n\n", master=canvas, text_color="white")
        test_label.grid(column=col, row=row, padx=50, pady=5)
        act_label_list.append(test_label)
    act_labels.extend(act_label_list)
    labels.extend(label_list)

samsung_labels = ["Galaxy F54_Samsung", "Knox_Samsung", "Do Not Dispose_Samsung", "Recycle_Samsung", "SoyOil_Samsung", "Box_Samsung", "BIS_Samsung", "Made for India_Samsung", "Samsung", "Snapdragon_Samsung"]
oneplus_labels = ["OnePlus", "BIS_OnePlus", "SoyOil_OnePlus", "Dolby_OnePlus", "Snapdragon_OnePlus", "Recycle_OnePlus", "Do Not Dispose_OnePlus", "Box_OnePlus"]
all_labels = samsung_labels + oneplus_labels
labels, present_labels, act_labels, sam_act_labels, onep_act_labels, all_act_labels = [], [], [], [], [], []

window = CTk()

window.title("LABEL INSPECTION APP")
window.iconbitmap("images/icon.png")
set_appearance_mode("dark")
image = PIL.Image.open('images/background_img.jpg')
background_image = CTkImage(image, size=(500, 500))
def bg_resizer(e):
    if e.widget is window:
        i = CTkImage(image, size=(e.width, e.height))
        bg_lbl.configure(text="", image=i)
bg_lbl = CTkLabel(window, text="", image=background_image)
bg_lbl.place(x=0, y=0)
window.bind("<Configure>", bg_resizer)

window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}+0+0")

main_label = CTkLabel(master=window, text="LABEL DETECTION", font=("Helvetica", 24), text_color="white", bg_color="#000000")
main_label.place(relx=0.5, rely=0.05, anchor=CENTER)

top_label = CTkLabel(master=window, bg_color="#000000",text="",text_color="white")
top_label.place(relx=0.25, rely=0.45, anchor=CENTER)

real_time = CTkLabel(master=window,height=50,width=200,text_color="white",bg_color="#000000",text="Real Time Camera",font=("Helvetica", 18))
real_time.place(relx=0.25,rely=0.1,anchor=CENTER)


canvas = CTkCanvas(master=window, width=600, height=500, bg="#353535", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.8, rely=0.5, anchor=CENTER)

test_params = CTkLabel(master=window,height=50,width=200,text="Test Parameters",font=("Helvetica", 18),bg_color="#000000",text_color="white")
test_params.place(relx=0.8,rely=0.1,anchor=CENTER)

p_or_f = CTkLabel(master=window,text="",fg_color="red",font=("Helvetica", 30),corner_radius=13,width=100,height=50,text_color="white", bg_color="#000000")
p_or_f.place(relx=0.25, rely=0.8, anchor=CENTER)

check = CTkImage(light_image=Image.open("images/check.jpg"), size=(20, 20))
cross = CTkImage(light_image=Image.open("images/cross.jpg"), size=(20, 20))

create_labels(all_labels, act_labels)

img1 = Image.open("images/exit.png")
button2 = CTkButton(master=window, text="EXIT", command=window.destroy, image=CTkImage(dark_image=img1, light_image=img1), width=150, height=60,font=("Helvetica", 25))
button2.place(relx=0.5, rely=0.9, anchor=CENTER)

combo_box = CTkComboBox(values=["All", "Samsung", "OnePlus"], master=window, height=50, width=200, font=("Helvetica", 18), dropdown_font=("Helvetica", 18), corner_radius=15, border_width=2, border_color="#000000", button_color="#000000", button_hover_color="#000000", dropdown_hover_color="#000000", dropdown_fg_color="#353535",fg_color="#000000", dropdown_text_color="white",bg_color="#000000", text_color="white", hover=True, command=choices, justify="center")
combo_box.place(relx=0.5, rely=0.8, anchor=CENTER)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error!! Could not open camera, check camera and try again")
    exit()

paused = False
window.bind("<p>", toggle_pause)

update_frame()

window.mainloop()
cap.release()