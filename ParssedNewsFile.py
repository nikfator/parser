import customtkinter
from main import ParsedNews

app = customtkinter.CTk()
app_title = 'KrasnodarMedia'
app.geometry('500x500')

def button_click(el):
    # Содержимое текстового поля.
    textbox.configure(state='normal', wrap='word')
    textbox.delete(1.0, 'end')
    textbox.insert('1.0', el.script)
    textbox.configure(state='disabled')

# Получение данных новостей
news = ParsedNews(1).data

# Левая часть интерфейса с кнопками
left_frame = customtkinter.CTkScrollableFrame(app)
for n in news:
    buttons = customtkinter.CTkButton(left_frame, text=f'{n.title[:20]}...')
    buttons.configure(command=lambda b=n: button_click(b))
    buttons.pack(fill='x')
left_frame.pack(side='left', fill='both', expand=True)

# Правую часть интерфейса с текстбоксом (только один)
right_frame = customtkinter.CTkFrame(app)
textbox = customtkinter.CTkTextbox(right_frame)
textbox.pack(fill='both', expand=True)
right_frame.pack(side='right', fill='both', expand=True)

app.mainloop()
