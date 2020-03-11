# coding:utf-8
import win32api
import win32con
import win32gui
from win32.lib import win32con
import os
import socket
import winreg

sub_key = [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
           r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall']

software_name = []

# 根节点
reg_root = win32con.HKEY_LOCAL_MACHINE
# 键的路径（具体路径自行修改）
reg_path = r"计算机\HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store"
# 权限和参数设置
reg_flags = win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
for item in win32api.RegEnumKeyEx(key):
    print(item)
win32api.RegCloseKey(key)

def handle_window(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):
        if '软件名或其包含的字词' in win32gui.GetWindowText(hwnd):
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        else:
            print("Not found")


hostname = socket.gethostname()



for i in sub_key:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, i, 0, winreg.KEY_ALL_ACCESS)
    for j in range(0, winreg.QueryInfoKey(key)[0] - 1):
        try:
            key_name = winreg.EnumKey(key, j)
            key_path = i + '\\' + key_name
            each_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
            DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayName')
            DisplayName = DisplayName.encode('utf-8')
            software_name.append(DisplayName)
        except WindowsError:
            pass

software_name = list(set(software_name))
software_name = sorted(software_name)

for result in software_name:
    print(bytes.decode(result) + '\n')


if __name__ == '__main__':
    win32gui.EnumWindows(handle_window, None)