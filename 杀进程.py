import win32gui

from win32.lib import win32con



def handle_window(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):

        if '软件名或其包含的字词' in win32gui.GetWindowText(hwnd):
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        else:
            print("Not found")


if __name__ == '__main__':
    win32gui.EnumWindows(handle_window, None)
