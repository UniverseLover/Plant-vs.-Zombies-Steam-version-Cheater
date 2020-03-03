from win32 import win32process,win32api,win32gui
import ctypes

kernel32=ctypes.windll.LoadLibrary(r"C:/Windows/System32/kernel32.dll")
def GetAddress(handle,BaseAddress=0x00197f1c,offset=[0x5578]):
    value=ctypes.c_long()
    kernel32.ReadProcessMemory(int(handle),BaseAddress,ctypes.byref(value),4,None)
    for i in range(len(offset)-1):
        kernel32.ReadProcessMemory(int(handle), value.value+offset[i], ctypes.byref(value), 4, None)
    return value.value+offset[len(offset)-1]


hwnd=win32gui.FindWindow("MainWindow","Plants vs. Zombies")
pid=win32process.GetWindowThreadProcessId(hwnd)[1]
handle=win32api.OpenProcess(0x1F0FFF,False,pid)


currentSun=ctypes.c_long()
changeSun=ctypes.c_long()

while True:
    address = GetAddress(handle) 
    kernel32.ReadProcessMemory(int(handle),address,ctypes.byref(currentSun),4,None)
    print("{}:{}".format("当前阳光",currentSun.value))
    changeSun.value = int(input("要修改成多少："))
    kernel32.WriteProcessMemory(int(handle), address, ctypes.byref(changeSun), 4, None)

