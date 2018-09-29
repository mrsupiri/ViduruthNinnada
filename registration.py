import tkinter as tk
from tkinter import ttk
from play_animation import play, file
import _thread
import serial
import time

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)


# ser = serial.Serial('/dev/ttyACM0', 9600)
_thread.start_new_thread(play, ())


def open_door():
    # ser.write(1)
    time.sleep(2)
    # ser.write(0)


def close_door():
    # ser.write(2)
    time.sleep(2)
    # ser.write(0)


class ViduruthNinnada(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Viduruth Ninnada Registration")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.schools = {}

        with open('schools.csv', 'r') as f:
            for line in f:
                data = line.strip().split(',')
                self.schools[data[1].strip()] = data[0].strip()
        # print(self.schools)

        main_frame = tk.Frame(container)
        frame = tk.Frame(main_frame)

        self.school_id = tk.Entry(frame)
        self.school_id.pack(side="right", pady=10, padx=10)

        school_id_label = tk.Label(frame, text="School ID", font=LARGE_FONT)
        school_id_label.pack(side="right", pady=10, padx=10)

        school_name_label = ttk.Label(frame, text="School Name", font=LARGE_FONT)
        school_name_label.pack(side="left", pady=10, padx=10)

        self.school_name = ttk.Entry(frame)
        self.school_name.pack(side="left", pady=10, padx=10, fill="x", expand=True)

        school_st_count_label = ttk.Label(frame, text="Total Number of Students", font=LARGE_FONT)
        school_st_count_label.pack(side="left", pady=10, padx=10)

        self.school_st_count = ttk.Entry(frame)
        self.school_st_count.pack(side="left", pady=10, padx=10, fill="x", expand=True)

        frame.pack(pady=30)

        frame = ttk.Frame(main_frame)
        mic_name_label = ttk.Label(frame, text="Name of MIC", font=LARGE_FONT)
        mic_name_label.pack(side="left", pady=10, padx=10)

        self.mic_name_input = ttk.Entry(frame)
        self.mic_name_input.pack(side="left", pady=10, padx=10, fill="x", expand=True)

        mic_tp_label = ttk.Label(frame, text="MIC Telephone", font=LARGE_FONT)
        mic_tp_label.pack(side="left", pady=10, padx=10)

        self.mic_tp_input = ttk.Entry(frame)
        self.mic_tp_input.pack(side="left", pady=10, padx=10, fill="x", expand=True)
        frame.pack(pady=10)

        self.students_widgets = []

        for i in range(1, 5):
            frame = tk.Frame(main_frame)

            student = {'Name Label': ttk.Label(frame, text="Student-{} Name".format(i), font=LARGE_FONT)}
            student['Name Label'].pack(side="left", pady=10, padx=10)

            student['Name Input'] = ttk.Entry(frame)
            student['Name Input'].pack(side="left", pady=10, padx=10, fill="x", expand=True)

            student['TP Label'] = ttk.Label(frame, text="Student-{} Telephone".format(i), font=LARGE_FONT)
            student['TP Label'].pack(side="left", pady=10, padx=10)

            student['TP Input'] = ttk.Entry(frame)
            student['TP Input'].pack(side="left", pady=15, padx=10, fill="x", expand=True)

            self.students_widgets.append(student)
            frame.pack()

        frame = ttk.Frame(main_frame)
        self.submit_button = ttk.Button(frame, text="Submit", command=lambda: self.save_data())
        self.submit_button.pack(side="right", pady=10, padx=30)

        self.open_door_button = ttk.Button(frame, text="Open Door", command=lambda: open_door())
        self.open_door_button.pack(side="left", pady=10, padx=30)
        self.open_close_button = ttk.Button(frame, text="Close Door", command=lambda: close_door())
        self.open_close_button.pack(side="left", pady=10, padx=30)

        frame.pack(pady=10, fill=tk.X)

        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.school_id.focus_set()
        # self.submit_button.config(state="disabled")

    def get_school(self, event=None):
        # print(self.school_id.get())
        if self.school_id.get() not in self.schools.keys():
            popupmsg('School was Not Found on the Database\nPlease Contact a Organizer')
            # self.school_name.insert(0, 'School was not found')
            # self.submit_button.config(state="disabled")
        else:
            self.school_name.insert(0, self.schools[self.school_id.get()])

            # self.submit_button.config(state="normal")

    def save_data(self):
        data = "{},{},{},{},{}".format(self.school_id.get(), self.school_name.get(), self.school_st_count.get(),
                                       self.mic_name_input.get(), self.mic_tp_input.get())
        for student in self.students_widgets:
            data += ',' + student['Name Input'].get()
            data += ',' + student['TP Input'].get()
        # play('videos/{}.mov'.format(self.school_id.get()))
        # ser.write(1)
        print(data, file=open('registration.csv', 'a'))

        # open_door()

        file.append('videos/{}.mov'.format(self.school_id.get()))

        self.school_id.delete(0, 'end')
        self.school_name.delete(0, 'end')
        self.school_st_count.delete(0, 'end')
        self.mic_name_input.delete(0, 'end')
        self.mic_tp_input.delete(0, 'end')
        for student in self.students_widgets:
            student['Name Input'].delete(0, 'end')
            student['TP Input'].delete(0, 'end')
        self.school_id.focus_set()


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Error !")
    label = ttk.Label(popup, text=msg, font=LARGE_FONT)
    label.pack(side="top", fill="x", pady=10, padx=20)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


app = ViduruthNinnada()
app.bind("<Return>", app.get_school)
app.geometry("1024x576")
app.mainloop()
