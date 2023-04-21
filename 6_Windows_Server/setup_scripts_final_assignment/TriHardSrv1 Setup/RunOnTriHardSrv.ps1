$TaskName = "ShitForTriHardSrv"
$TaskDescription = "Do shit for TriHard Server"
$TaskScriptPath = "C:\script\ShitForTriHardSrv.ps1"
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


New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 10.6.68.177 -PrefixLength 24 -DefaultGateway 10.6.68.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 10.6.68.175
$secPassword = ConvertTo-SecureString "Linux4Ever" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ("Administrator", $secPassword)
Add-Computer -DomainName "ItsCrap.io" -Credential $cred

Write-Host "Installing some Windows features, please wait. Computer will automatically restart when finished."
Start-Job -Name addFeature -ScriptBlock {
    Install-WindowsFeature "Print-Services" -IncludeAllSubFeature -IncludeManagementTools
    Install-WindowsFeature "RSAT-DFS-Mgmt-Con" -IncludeAllSubFeature -IncludeManagementTools
} | Wait-Job | Receive-Job
Restart-Computer
