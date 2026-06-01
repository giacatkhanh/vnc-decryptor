# vnc-decryptor
Python script to decrypt VNC passwords extracted from Windows Registry using fixed DES key
🔍 VNC Hex String Storage Locations
1. RealVNC
-Usually stored at the system level in the Registry.
```cmd
reg query HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\vncserver /v Password
```
