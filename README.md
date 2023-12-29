# CursorMover
This program allows you to move the cursor with the arrows, alternatively
you can press 'A' to toggle the automatic movement of the cursor. The movement speed can be changed by pressing the letter 'X'.


## Build Executable
PyInstaller is needed to package an executable

Build package by running the following command:
```console
PyInstaller MoveCursor.spec
```


## Python Good To Know stuff
Enable script execution temporarily to enable environment
```console
Set-ExecutionPolicy RemoteSigned -Scope Process
```

Enable Environment
```console
.\venv\Scripts\Activate.ps1
```
