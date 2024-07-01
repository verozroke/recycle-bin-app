from cx_Freeze import setup, Executable
import os

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter", "ctypes"],
    "include_files": ["core/", "functions/", "generator/", "assets/logo.png"]
}

base = None
if os.name == 'nt':
    base = 'Win32GUI'  # Use this to suppress the console window on Windows

setup(
    name="RecycleBinManager",
    version="0.1",
    description="A simple app to manage the Windows Recycle Bin",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, target_name="RecycleBinManager.exe", icon="logo.ico")]
)
