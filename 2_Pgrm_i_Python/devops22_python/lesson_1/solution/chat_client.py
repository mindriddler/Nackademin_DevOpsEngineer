import tkinter as tk


def create_widgets(parent):

    chat_label = tk.Label(
                parent,
                text="Hello Chat",
                font=('helvetica', 22),
                pady=10
            )
            
    chat_label.grid(
                row=0,
                columnspan=5
            )

    chat_entry = tk.Entry(
        parent,
        font=("helvetica", 14)
    )
    chat_entry.grid(
        row=2,
        column=0,
        sticky=tk.EW,
        columnspan=4,
        pady=20
    )

    chat_button = tk.Button(
        parent,
        text="Send message"
    )
    chat_button.grid(
        row=2,
        column=4,
        sticky=tk.EW,
        padx=(20, 0)
    )
    
    chat_text = tk.Text(parent,
        font=("helvetica", 14),
        state=tk.DISABLED
    )

    chat_text.grid(
        row=1,
        sticky=tk.EW,
        columnspan=5,
        column=0
    )

    setup_chat_handler(chat_entry, chat_button, chat_text)

    
def setup_chat_handler(from_entry_widget ,from_button_widget, to_text_widget):    
    def submit_chat_message(event=None):
        text = from_entry_widget.get()
        to_text_widget.configure(state=tk.NORMAL)
        to_text_widget.insert(tk.END, f'> {text}\n')
        to_text_widget.configure(state=tk.DISABLED)
        from_entry_widget.delete(0, tk.END)

    from_entry_widget.bind("<Return>", submit_chat_message,)
    from_button_widget.bind("<Return>", submit_chat_message,)
    from_button_widget.bind("<Button-1>", submit_chat_message, "+")

def init_tk():
    root = tk.Tk()
    create_widgets(root)
    return root

def main():
    mw = init_tk()
    mw.mainloop()

if __name__ == "__main__":
    main()
