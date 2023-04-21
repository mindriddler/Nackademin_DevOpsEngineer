# Will turn off all vms with Server as begining of the name

$VMVariable = @{
    DC1           = "DC1" 
    TriHardSrv1   = "TriHardSrv1"
    PepeLaughSrv1 = "PepeLaughSrv1"
    ClientW10     = "ClientW10" 
}

foreach ($VMname in $VMVariable.Keys) {
    $FolderPath = "C:\VM\$VMname"
    If (Test-Path $FolderPath -PathType Container) {
        Write-Host "Stopping $VMname"
        Stop-VM -Name $VMname -Force
        Start-Sleep 5
        Write-Host "Deleting $VMname"
        Remove-VM -Name $VMname -Force
        Write-Host "Deleting $VMname folder"
        Remove-Item -Path $FolderPath -Recurse -Force
        Write-Host "------------------------------"
        Write-Host "$VMname deleted"
        Write-Host "------------------------------"
    }
    else {
        Write-Host "$VMname folder does not exist"
    }   
}


$Item = (Get-VMSwitch | Where-Object -Property Name -EQ -Value "VM1").count
If ($Item -eq '1') {
    Write-Host "Removing VM1 switch"
    Remove-VMSwitch -Name VM1 -Force
    Write-Host "Switch removed"
}
else {
    Write-Host "VM1 switch does not exist"
}




