# Run as Administrator on the host mmachine
Set-VMhost -EnableEnhancedSessionMode $False
# Create the VM directory if it does not exist
$vmDirectory = "C:\VM";
if (-not (Test-Path $vmDirectory)) {
    New-Item -ItemType Directory -Path $vmDirectory; 
}

# Create the subdirectories if they do not exist
# Running them separate 
$subDirectories = @("DC1", "ISO", "ClientW10", "TriHardSrv1", "PepeLaughSrv1"); 
foreach ($directory in $subDirectories) {
    New-Item -ItemType Directory -Path "$vmDirectory\$directory"
    Write-Host "Created $directory"
}

# Download the files
$fileVariables = @{
    DCSetup        = "C:\VM\ISO\DCSetup.vhd"
    Win10          = "C:\VM\ISO\Windows10Enterprise.iso"
    PepeLaughSetup = "C:\VM\ISO\PepeLaughSetup.vhd"
    TrihardSetup   = "C:\VM\ISO\TriHardSetup.vhd"
}

$urlVariables = @{
    DCSetupUrl     = "https://onedrive.live.com/download?cid=8A5671F4D3C47F8E&resid=8A5671F4D3C47F8E%2147690&authkey=AMAbRv7AOzlW03w"
    Win10Url       = "https://onedrive.live.com/download?cid=8A5671F4D3C47F8E&resid=8A5671F4D3C47F8E%2147687&authkey=AJZSx2EJOcvE7bI"
    PepeLaughSetup = "https://onedrive.live.com/download?cid=8A5671F4D3C47F8E&resid=8A5671F4D3C47F8E%2147689&authkey=AER-tBVeV4ydr18"
    TriHardSetup   = "https://onedrive.live.com/download?cid=8A5671F4D3C47F8E&resid=8A5671F4D3C47F8E%2147688&authkey=AMG2AeEUJQPb9tY"
}

foreach ($fileVariable in $fileVariables.Keys) {
    if ([IO.File]::Exists($fileVariables[$fileVariable])) {
        Write-Host "File $($fileVariables[$fileVariable]) already exists"
    }
    else {
        Write-Host "File $($fileVariables[$fileVariable]) does not exist"
        Write-Host "Downloading to $($fileVariables[$fileVariable])"
        Invoke-WebRequest -Uri $urlVariables["$($fileVariable)Url"] -OutFile $fileVariables[$fileVariable]
        Write-Host "Downloaded to $($fileVariables[$fileVariable])"
    }
}


Set-ItemProperty -Path "C:\VM\ISO\DCSetup.vhd" -Name IsReadOnly -Value $true 
Set-ItemProperty -Path "C:\VM\ISO\PepeLaughSetup.vhd" -Name IsReadOnly -Value $true 
Set-ItemProperty -Path "C:\VM\ISO\TriHardSetup.vhd" -Name IsReadOnly -Value $true 
Write-Host "Creating disks for VMs"
New-VHD -Path C:\VM\DC1\DC1.vhd -ParentPath "C:\VM\ISO\DCSetup.vhd" -Differencing
New-VHD -Path C:\VM\PepeLaughSrv1\PepeLaughSrv1.vhd -ParentPath "C:\VM\ISO\PepeLaughSetup.vhd" -Differencing
New-VHD -Path C:\VM\TriHardSrv1\TriHardSrv1.vhd -ParentPath "C:\VM\ISO\TriHardSetup.vhd" -Differencing


# For creating a external switch, replace "Ethernet 2" with your own
# Use Get-NetAdapter to find the name of the NIC you want to use
$SwitchName = 'VM1'
$Item = (Get-VMSwitch | Where-Object { $_.Name -eq $SwitchName } ).count

if ($Item -eq 1) {
    Write-Host "Switch '$SwitchName' already exists"
}
else {
    Write-Host "Creating Switch '$SwitchName'"
    #New-VMSwitch -Name $SwitchName -NetAdapterName "Ethernet 2"
    New-VMSwitch -Name $SwitchName -SwitchType Internal
    Write-Host "Switch '$SwitchName' Created"
}

# Uncomment the other machines if you want them
# Im only working on the DC atm
$VMVariable = @{
    DC1           = "DC1" 
    TriHardSrv1   = "TriHardSrv1"
    PepeLaughSrv1 = "PepeLaughSrv1"
    ClientW10     = "ClientW10" 
}

foreach ($VMname in $VMVariable.Keys) {
    $Item = (Get-VM | Where-Object -Property Name -EQ -Value $VMname).count
    If ($Item -eq '1') {
        Write-Host "$VMname already exists"
    }
    else {
        Write-Host "Creating $VMname"
        if ($VMname -eq "DC1") {
            New-VM -Name "DC1" -VHDPath "C:\VM\DC1\DC1.vhd" -BootDevice IDE -Generation 1 -SwitchName VM1
            Set-VMMemory DC1 -DynamicMemoryEnabled $true -MinimumBytes 4GB -StartupBytes 4GB -MaximumBytes 8GB -Priority 80 -Buffer 25
            Set-VMProcessor DC1 -Count 2
            Write-Host "$VMname created"
            Write-Host "Starting $VMname"
            Start-vm $VMname 
        }
        if ($VMname -eq "TriHardSrv1") {
            # We will set up a Fail over cluster between TriHardSrv1 and PepeLaughSrv1
            New-VM -Name "TriHardSrv1" -VHDPath "C:\VM\TriHardSrv1\TriHardSrv1.vhd" -BootDevice IDE -Generation 1 -SwitchName VM1
            Set-VMMemory TriHardSrv1 -DynamicMemoryEnabled $true -MinimumBytes 2GB -StartupBytes 4GB -MaximumBytes 8GB -Priority 80 -Buffer 25
            Set-VMProcessor TriHardSrv1 -Count 2
            Write-Host "$VMname created"
            Write-Host "Creating drives for RAID5"
            for ($i = 1; $i -le 6; $i++) {
                $VHDPath = "C:\VM\TriHardSrv1\RAID5\RAID5_" + $i + ".vhdx"
                New-VHD -Path $vHDPath -SizeBytes 20GB -Dynamic
                Add-VMHardDiskDrive -VMName TriHardSrv1 -ControllerType SCSI -ControllerNumber 0 -Path $vHDPath
            }
        } 
        if ($VMname -eq "PepeLaughSrv1") {
            # We will set up a Fail over cluster between TriHardSrv1 and PepeLaughSrv1
            New-VM -Name "PepeLaughSrv1" -VHDPath "C:\VM\PepeLaughSrv1\PepeLaughSrv1.vhd" -BootDevice IDE -Generation 1 -SwitchName VM1
            Set-VMMemory PepeLaughSrv1 -DynamicMemoryEnabled $true -MinimumBytes 2GB -StartupBytes 4GB -MaximumBytes 8GB -Priority 80 -Buffer 25
            Set-VMProcessor PepeLaughSrv1 -Count 2
            Write-Host "$VMname created"
            Write-Host "Creating drives for RAID5"
            for ($i = 1; $i -le 6; $i++) {
                $VHDPath = "C:\VM\PepeLaughSrv1\RAID5\RAID5_" + $i + ".vhdx"
                New-VHD -Path $vHDPath -SizeBytes 20GB -Dynamic
                Add-VMHardDiskDrive -VMName PepeLaughSrv1 -ControllerType SCSI -ControllerNumber 0 -Path $vHDPath
            }
        } 
        if ($VMname -eq "ClientW10") {   
            New-VM -Name "ClientW10" -NewVHDPath "C:\VM\ClientW10\ClientW10.vhdx" -NewVHDSizeBytes 40GB -Generation 1 -SwitchName VM1
            Set-VMMemory ClientW10 -DynamicMemoryEnabled $true -MinimumBytes 2GB -StartupBytes 4GB -MaximumBytes 16GB -Priority 80 -Buffer 25
            Set-VMProcessor ClientW10 -Count 2
            Set-VMDvdDrive -VMName ClientW10 -Path C:\VM\ISO\Windows10Enterprise.iso
            Write-Host "$VMname created" 
        }              
    }
}

Write-Host "System will now be sleeping for 10 minutes"
Write-Host "This is the time it will take for the DC to do its thing"
Write-Host "After this, the other VMs will be started"
Write-Host "This is to ensure the DC is up and running before the other VMs are started"
$TotalSeconds = 600
$Increment = 1
$Progress = 0

for ($i = $TotalSeconds; $i -ge 0; $i -= $Increment) {
    $Progress = [math]::Round((1 - ($i / $TotalSeconds)) * 100, 2)
    $TimeLeft = New-TimeSpan -Seconds $i
    Write-Progress -Activity "Progress" -Status "Time Left: $($TimeLeft.ToString('hh\:mm\:ss'))" -PercentComplete $Progress
    Start-Sleep -Seconds $Increment
}

Write-Progress -Activity "Progress" -Completed


$notrunning = @{
    TriHardSrv1   = "TriHardSrv1"
    PepeLaughSrv1 = "PepeLaughSrv1"
    ClientW10     = "ClientW10" 
}
foreach ($VMname in $notrunning.Keys) {
    Write-Host "Starting $VMname"
    Start-vm $VMname
}




