import tkinter as tk
import socket
from wakeonlan import send_magic_packet

def wake_on_lan():
    hostname = hostname_entry.get().upper()  # Convert to uppercase
    mac_address = mac_address_entry.get()

    try:
        ip_address = socket.gethostbyname(hostname)
        send_magic_packet(mac_address, ip_address=ip_address)
        status_label.config(text="Magic packet sent successfully.")
    except socket.gaierror:
        status_label.config(text="Error: Hostname resolution failed.")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("WoL Client")

# Create and place labels and entry fields
hostname_label = tk.Label(root, text="PC Hostname (or IP address):")
hostname_label.pack()
hostname_entry = tk.Entry(root)
hostname_entry.pack()

mac_address_label = tk.Label(root, text="MAC Address:")
mac_address_label.pack()
mac_address_entry = tk.Entry(root)
mac_address_entry.pack()

# Create the WoL button
wol_button = tk.Button(root, text="Wake-on-LAN", command=wake_on_lan)
wol_button.pack()

# Display status messages
status_label = tk.Label(root, text="")
status_label.pack()

# Start the GUI main loop
root.mainloop()
