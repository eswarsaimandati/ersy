
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# === Global State ===
root = tk.Tk()
root.withdraw()  # Hide main window initially

# === Utility Functions ===
def exit_app():
    root.quit()

def show_main_menu():
    menu = tk.Toplevel()
    menu.title("Ersy - Main Menu")
    menu.geometry("300x250")
    tk.Button(menu, text="🔐 Generate Keys", width=25,
              command=lambda: [menu.destroy(), open_keygen_window()]).pack(pady=10)
    tk.Button(menu, text="🛡️ Encrypt File", width=25,
              command=lambda: [menu.destroy(), open_encrypt_window()]).pack(pady=10)
    tk.Button(menu, text="🔓 Decrypt File", width=25,
              command=lambda: [menu.destroy(), open_decrypt_window()]).pack(pady=10)
    tk.Button(menu, text="❌ Exit", width=25, command=exit_app).pack(pady=10)

def open_keygen_window():
    win = tk.Toplevel()
    win.title("Generate RSA Keys")
    win.geometry("300x200")

    tk.Label(win, text="Keys will be saved in the application folder.").pack(pady=10)

    def generate_keys():
        try:
            subprocess.run(["python", "generate_keys.py"], check=True)
            messagebox.showinfo("Success", "Keys generated successfully.")
            win.destroy()
            show_main_menu()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate keys: {e}")

    tk.Button(win, text="Generate Keys", width=20, command=generate_keys).pack(pady=10)
    tk.Button(win, text="⬅ Back", width=20,
              command=lambda: [win.destroy(), show_main_menu()]).pack(pady=5)
    tk.Button(win, text="❌ Exit", width=20, command=exit_app).pack(pady=5)

def open_encrypt_window():
    win = tk.Toplevel()
    win.title("Encrypt File")
    win.geometry("400x300")

    image = tk.StringVar()
    secret = tk.StringVar()
    pubkey = tk.StringVar()
    output = tk.StringVar()

    def choose(var, label, filetypes):
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            var.set(filename)
            label.config(text=os.path.basename(filename))

    def choose_output():
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            output.set(path)
            output_label.config(text=os.path.basename(path))

    tk.Button(win, text="Select Image",
              command=lambda: choose(image, img_label, [("Image Files","*.png;*.bmp;*.tga;*.tiff")])).pack()
    img_label = tk.Label(win, text="No image selected")
    img_label.pack()

    tk.Button(win, text="Select Secret File",
              command=lambda: choose(secret, secret_label, [("All Files","*.*")])).pack()
    secret_label = tk.Label(win, text="No file selected")
    secret_label.pack()

    tk.Button(win, text="Select Public Key",
              command=lambda: choose(pubkey, pubkey_label, [("PEM Files","*.pem")])).pack()
    pubkey_label = tk.Label(win, text="No public key selected")
    pubkey_label.pack()

    tk.Button(win, text="Select Output File", command=choose_output).pack()
    output_label = tk.Label(win, text="No output selected")
    output_label.pack()

    def encrypt():
        if not image.get() or not secret.get() or not pubkey.get() or not output.get():
            messagebox.showerror("Error", "Select all required files.")
            return
        try:
            result = subprocess.run(
                ['python', 'ersy.py', 'hide', image.get(), secret.get(), pubkey.get(), output.get()],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                messagebox.showinfo("Success", "Encryption completed successfully.")
                win.destroy()
                show_main_menu()
            else:
                messagebox.showerror("Error", result.stderr)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {e}")

    tk.Button(win, text="Start Encryption", width=20, command=encrypt).pack(pady=10)
    tk.Button(win, text="⬅ Back", width=20,
              command=lambda: [win.destroy(), show_main_menu()]).pack(pady=5)
    tk.Button(win, text="❌ Exit", width=20, command=exit_app).pack(pady=5)

def open_decrypt_window():
    win = tk.Toplevel()
    win.title("Decrypt File")
    win.geometry("400x300")

    image = tk.StringVar()
    privkey = tk.StringVar()
    output = tk.StringVar()

    def choose(var, label, filetypes):
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            var.set(filename)
            label.config(text=os.path.basename(filename))

    def choose_output():
        path = filedialog.asksaveasfilename()
        if path:
            output.set(path)
            output_label.config(text=os.path.basename(path))

    tk.Button(win, text="Select Image",
              command=lambda: choose(image, img_label, [("Image Files","*.png;*.bmp;*.tga;*.tiff")])).pack()
    img_label = tk.Label(win, text="No image selected")
    img_label.pack()

    tk.Button(win, text="Select Private Key",
              command=lambda: choose(privkey, key_label, [("PEM Files","*.pem")])).pack()
    key_label = tk.Label(win, text="No private key selected")
    key_label.pack()

    tk.Button(win, text="Select Output File", command=choose_output).pack()
    output_label = tk.Label(win, text="No output selected")
    output_label.pack()

    def decrypt():
        if not image.get() or not privkey.get() or not output.get():
            messagebox.showerror("Error", "Select all required files.")
            return
        try:
            result = subprocess.run(
                ['python', 'ersy.py', 'extract', image.get(), privkey.get(), output.get()],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                messagebox.showinfo("Success", "Decryption completed successfully.")
                win.destroy()
                show_main_menu()
            else:
                messagebox.showerror("Error", result.stderr)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {e}")

    tk.Button(win, text="Start Decryption", width=20, command=decrypt).pack(pady=10)
    tk.Button(win, text="⬅ Back", width=20,
              command=lambda: [win.destroy(), show_main_menu()]).pack(pady=5)
    tk.Button(win, text="❌ Exit", width=20, command=exit_app).pack(pady=5)

# === Start GUI ===
show_main_menu()
root.mainloop()
