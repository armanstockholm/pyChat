import tkinter as tk
import pymongo

#connect to mongoDB

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PythonChat"]
messages_col = db["messages"]


# Gui
root = tk.Tk()
root.title("PythonChat")
root.geometry("300x300")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

def send_message():
    if entry.get():
        messages_col.insert_one({"text": entry.get()})
        entry.delete(0, tk.END)

def fetch_messages():
    global message_label
    messages = messages_col.find().sort("_id")
    message_label.config(text="Messages: \n " + "\n".join(f"- {m["text"]}" for m in messages))
    root.after(2000, fetch_messages)
    
    
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

message_label = tk.Label(root, text="Messages:" , justify="left")
message_label.pack()

fetch_messages()
root.mainloop()