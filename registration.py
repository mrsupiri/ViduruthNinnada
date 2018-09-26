import tkinter as tk
from tkinter import ttk
from play_animation import play
LARGE_FONT = ("Verdana", 12)


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
        submit_button = ttk.Button(frame, text="Submit", command=lambda: self.save_data())
        submit_button.pack(side="right", pady=10, padx=30)
        frame.pack(pady=10, fill=tk.X)

        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def get_school(self, event=None):
        print('Yes')
        self.school_name.insert(0, self.schools[self.school_id.get()])

    def save_data(self):
        data = "{},{},{},{},{}".format(self.school_id.get(), self.school_name.get(), self.school_st_count.get(),
                                       self.mic_name_input.get(), self.mic_tp_input.get())
        for student in self.students_widgets:
            data += ','+student['Name Input'].get()
            data += ','+student['TP Input'].get()
        play('videos/{}.mov'.format(self.school_id.get()))
        print(data)


app = ViduruthNinnada()
app.bind("<Return>", app.get_school)
app.geometry("1024x576")
app.mainloop()
