
# Create a schedule task that will run on user logon
# This task will load the script "ADStuff.ps1"
$TaskName = "ADStuff"
$TaskDescription = "Do AD stuff"
$TaskScriptPath = "C:\script\ADStuff.ps1"
$TaskAction = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File $TaskScriptPath"
$TaskTrigger = New-ScheduledTaskTrigger -AtLogOn
$taskTrigger.Delay = "PT30S"
Register-ScheduledTask -TaskName $TaskName -Description $TaskDescription -Action $TaskAction -Trigger $TaskTrigger -Force
$TaskExists = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($TaskExists) {
    Write-Host "The task $TaskName exists."
}
else {
    Write-Host "The task $TaskName does not exist."
}

New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 10.6.68.175 -PrefixLength 24 -DefaultGateway 10.6.68.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 127.0.0.1

# This part will install all the needed stuff for turn the VM
# into a DC
$DatabasePath = "c:\windows\NTDS"
$DomainMode = "WinThreshold"
$DomainName = "ItsCrap.io"
$DomainNetBIOSName = "ItsCrap"
$ForestMode = "WinThreshold"
$LogPath = "c:\windows\NTDS"
$SysVolPath = "c:\windows\SYSVOL" 
$Password = (ConvertTo-SecureString -String "Linux4Ever" -AsPlainText -Force)


#Install AD DS, DNS and GPMC 
start-job -Name addFeature -ScriptBlock { 
    Add-WindowsFeature -Name "ad-domain-services" -IncludeAllSubFeature -IncludeManagementTools 
    Add-WindowsFeature -Name "dns" -IncludeAllSubFeature -IncludeManagementTools 
    Add-WindowsFeature -Name "gpmc" -IncludeAllSubFeature -IncludeManagementTools } 
Wait-Job -Name addFeature 

#Create New AD Forest
Install-ADDSForest `
    -CreateDnsDelegation:$false `
    -DatabasePath $DatabasePath `
    -DomainMode $DomainMode `
    -DomainName $DomainName `
    -SafeModeAdministratorPassword $Password `
    -DomainNetbiosName $DomainNetBIOSName `
    -ForestMode $ForestMode `
    -InstallDns:$true `
    -LogPath $LogPath `
    -NoRebootOnCompletion:$false `
    -SysvolPath $SysVolPath `
    -Force:$true


