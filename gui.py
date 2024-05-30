# UNIVERSAL WINDOWS95 ACTIVATOR: This is a simple GUI written in Python using the TkInter
# library. It's recommended to run uwact.py instead of this, as I'm planning to turn this into
# an executable bundle of all three scripts.

import tkinter as tk
import keygen


def keygen_out() -> str:
    return f"{keygen.generate_cd_key()}\n{keygen.generate_oem_key()}\n"


def window():
    root = tk.Tk()
    root.minsize(250, 150)
    root.maxsize(250, 150)
    root.title("UWAct\n(@pescodaldeck)")

    label = tk.Label(root, text=root.title(), font=("Helvetica", 18))
    label.pack(pady=(10, 0))

    text = tk.Text(root, height=2)
    text.pack(side="bottom", fill="both", expand=True)

    def button_clicked():
        text.delete("1.0", "end")
        output = keygen_out()
        text.insert("end", output)


    button = tk.Button(root, text="GENERATE", command=button_clicked)
    button.pack(pady=(20, 0))

    root.mainloop()


window()
