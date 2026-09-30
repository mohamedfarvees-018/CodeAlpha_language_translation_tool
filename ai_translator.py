import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Translate Function
def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter text.")
        return

    source = source_lang.get()
    target = target_lang.get()

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)

        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
        output_text.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x500")
root.config(bg="#f0f8ff")

title = tk.Label(root, text="🌍 Language Translation Tool",
                 font=("Arial", 18, "bold"), bg="#f0f8ff")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack()

tk.Label(frame, text="Source Language").grid(row=0, column=0, padx=10)
tk.Label(frame, text="Target Language").grid(row=0, column=1, padx=10)

languages = [
    "english",
    "tamil",
    "hindi",
    "french",
    "german",
    "spanish",
    "japanese",
    "korean"
]

source_lang = ttk.Combobox(frame, values=languages, state="readonly")
source_lang.current(0)
source_lang.grid(row=1, column=0, padx=10)

target_lang = ttk.Combobox(frame, values=languages, state="readonly")
target_lang.current(1)
target_lang.grid(row=1, column=1, padx=10)

tk.Label(root, text="Enter Text:", bg="#f0f8ff").pack(anchor="w", padx=20)

input_text = tk.Text(root, height=6, width=70)
input_text.pack(padx=20)

translate_btn = tk.Button(root, text="Translate", bg="blue",
                          fg="white", command=translate_text)
translate_btn.pack(pady=10)

tk.Label(root, text="Translated Text:", bg="#f0f8ff").pack(anchor="w", padx=20)

output_text = tk.Text(root, height=6, width=70, state="disabled")
output_text.pack(padx=20)

root.mainloop()