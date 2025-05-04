import winreg
import os
import sys

def register_context_menu():
    script_path = os.path.abspath("psd_to_png.py")
    python_exe = sys.executable
    command = f'"{python_exe}" "{script_path}" "%1"'

    try:
        key_path = r"Photoshop.Image\shell\PSDtoPNG"
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "PSDtoPNG")
        command_key = winreg.CreateKey(key, "command")
        winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, command)
        print("右键菜单注册成功！")
    except Exception as e:
        print(f"注册失败: {str(e)}")

if __name__ == "__main__":
    register_context_menu()
