; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId=A7F27B2C-242C-47BC-B3BA-5E5EA564DDAF
AppName=Recycle Bin Manager
AppVersion=1.0
DefaultDirName={pf}\Recycle Bin Manager
DefaultGroupName=Recycle Bin Manager
AllowNoIcons=yes
OutputDir=.
OutputBaseFilename=RecycleBinManagerSetup
SetupIconFile=logo.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "build\exe.win-amd64-3.11\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Recycle Bin Manager"; Filename: "{app}\main.exe"
Name: "{group}\Uninstall Recycle Bin Manager"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,Recycle Bin Manager}"; Flags: nowait postinstall skipifsilent
