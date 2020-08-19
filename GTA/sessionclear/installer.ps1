<# 
My First Mod INSTALL to desktop
#>

# Variables
$userProfile = $env:USERPROFILE
$installPath = "$userProfile\Desktop\"
$appPath = "$userProfile\Desktop\GTATool\"
$downloadurl = "https://download.sysinternals.com/files/PSTools.zip"
$toolsFile = "$userProfile\Desktop\GTATool\PSTools.zip"
$toolsFolder = "$userProfile\Desktop\GTATool\PSTools\"
$SuspendEXE = "$userProfile\Desktop\PSTools\pssuspend.exe"

#make folders
New-Item -Path $installPath -Name GTATool -ItemType directory
New-Item -Path $appPath -Name PsTools -ItemType directory

# download the windows pack and extract to place
$WebClient = New-Object System.Net.WebClient
$WebClient.DownloadFile($downloadurl,$toolsFile)
Expand-Archive -Path $toolsFile -DestinationPath $toolsFolder

# clean up zip
Remove-Item -Path $toolsFile

# create the executable file for mod
New-Item -Path $appPath -Name mod.ps1 -ItemType File

$filecontent = @" 

function Clear_Lobby { 
& $userProfile\Desktop\PSTools\pssuspend.exe GTA5
Start-Sleep -Seconds 10
& $userProfile\Desktop\PSTools\pssuspend.exe -r GTA5
}

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Application]::EnableVisualStyles()

#Main dimentions
`$Ryans_GTAMOD                    = New-Object system.Windows.Forms.Form
`$Ryans_GTAMOD.ClientSize         = '276,125'
`$Ryans_GTAMOD.text               = "Ryan`'s GTA Mod menu"
`$Ryans_GTAMOD.BackColor          = "#4a90e2"
`$Ryans_GTAMOD.TopMost            = `$false
`$Button1                         = New-Object system.Windows.Forms.Button
`$Button1.text                    = "Clear Lobby"
`$Button1.width                   = 245
`$Button1.height                  = 80
`$Button1.location                = New-Object System.Drawing.Point(10,20)
`$Button1.Font                    = 'Microsoft Sans Serif,10'
`$Ryans_GTAMOD.controls.AddRange(@(`$Button1))
`$Button1.Add_Click({ Clear_Lobby  })
`$Ryans_GTAMOD.ShowDialog()

"@
$filecontent | Out-File -FilePath $appPath\mod.ps1