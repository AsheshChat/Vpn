import tkinter as tk
import subprocess

class WireGuardVPNClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('WireGuard VPN Client')
        
        self.status_label = tk.Label(root, text='Status: Disconnected', font=('Arial', 14))
        self.status_label.pack(pady=10)
        
        self.connect_button = tk.Button(root, text='Connect', command=self.connect_vpn, font=('Arial', 14))
        self.connect_button.pack(pady=10)
        
        self.disconnect_button = tk.Button(root, text='Disconnect', command=self.disconnect_vpn, font=('Arial', 14), state=tk.DISABLED)
        self.disconnect_button.pack(pady=10)
        
    def connect_vpn(self):
        # Execute the WireGuard 'wg-quick up' command to start the VPN connection
        try:
            subprocess.run(['wg-quick', 'up', 'path_to_wireguard_config_file'], check=True)
            self.status_label.config(text='Status: Connected')
            self.connect_button.config(state=tk.DISABLED)
            self.disconnect_button.config(state=tk.NORMAL)
        except subprocess.CalledProcessError as e:
            # Handle error if the WireGuard command fails
            print(f'Error: {e}')
        
    def disconnect_vpn(self):
        # Execute the WireGuard 'wg-quick down' command to stop the VPN connection
        try:
            subprocess.run(['wg-quick', 'down', 'C:\Program Files\WireGuard\Data\Configurations'], check=True)
            self.status_label.config(text='Status: Disconnected')
            self.connect_button.config(state=tk.NORMAL)
            self.disconnect_button.config(state=tk.DISABLED)
        except subprocess.CalledProcessError as e:
            # Handle error if the WireGuard command fails
            print(f'Error: {e}')

def main():
    root = tk.Tk()
    vpn_client_gui = WireGuardVPNClientGUI(root)
    root.mainloop()

if __name__ == '__main__':
    # Run the WireGuard VPN program with GUI
    main()
