import tkinter as tk
import keyboard

pressed_keys = set()

def on_key_event(event):
    if event.event_type == 'down':
        pressed_keys.add(event.name)
        
        if event.name == 'a' and 'd' in pressed_keys:
            keyboard.release('d')
        
        elif event.name == 'd' and 'a' in pressed_keys:
            keyboard.release('a')
        
    elif event.event_type == 'up':
        pressed_keys.discard(event.name)
        
        if event.name == 'd' and 'a' in pressed_keys:
            keyboard.press('a')
        
        elif event.name == 'a' and 'd' in pressed_keys:
            keyboard.press('d')

def exit_application():
    keyboard.unhook_all()
    root.destroy()

root = tk.Tk()
root.title("PyTap")

exit_button = tk.Button(root, text="Exit (Ctrl+Shift+H)", command=exit_application)
exit_button.pack(pady=20)

keyboard.hook(on_key_event)

keyboard.add_hotkey('ctrl+shift+h', exit_application)

root.mainloop()
