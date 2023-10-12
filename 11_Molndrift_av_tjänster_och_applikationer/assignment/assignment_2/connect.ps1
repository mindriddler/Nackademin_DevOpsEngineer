$connectTestResult = Test-NetConnection -ComputerName fredrikcloudstorage.file.core.windows.net -Port 445
if ($connectTestResult.TcpTestSucceeded) {
    # Save the password so the drive will persist on reboot
    cmd.exe /C "cmdkey /add:`"fredrikcloudstorage.file.core.windows.net`" /user:`"localhost\fredrikcloudstorage`" /pass:`"[REDACTED]`""
    # Mount the drive
    New-PSDrive -Name Z -PSProvider FileSystem -Root "\\fredrikcloudstorage.file.core.windows.net\cloudcourse" -Persist
}
else {
    Write-Error -Message "Unable to reach the Azure storage account via port 445. Check to make sure your organization or ISP is not blocking port 445, or use Azure P2S VPN, Azure S2S VPN, or Express Route to tunnel SMB traffic over a different port."
}
