#coding:utf-8
import win32api
import win32con
#根节点
reg_root = win32con.HKEY_LOCAL_MACHINE
#键的路径（具体路径自行修改）
reg_path = r"计算机\HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store"
#权限和参数设置
reg_flags = win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS
     

key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)

    
for item in win32api.RegEnumKeyEx(key):
    print(item)
win32api.RegCloseKey(key)
