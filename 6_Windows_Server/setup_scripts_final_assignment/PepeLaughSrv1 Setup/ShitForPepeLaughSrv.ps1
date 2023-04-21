$TaskName = "ShitForPepeLaughSrv"
$TaskExists = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
# If it does exist, unregister it and confirm success
if ($TaskExists) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Host "Task $TaskName removed"
}
# If it doesn't exist, inform that it was not found
else {
    Write-Host "Task $TaskName does not exist"
}

$raid5 = "RAID5"
$driveLetter = "R"
# Change the disk numbers to match the disks you want to initialize and add to the RAID
$disks = Get-Disk | Where-Object -FilterScript { $_.OperationalStatus -eq "Offline" }
foreach ($disk in $disks) {
    Set-Disk -InputObject $disk -IsOffline $false
    Initialize-Disk -InputObject $disk -PartitionStyle GPT
}
New-StoragePool `
    -FriendlyName $raid5 `
    -StorageSubSystemFriendlyName "Windows Storage*" `
    -PhysicalDisks (Get-PhysicalDisk | Where-Object CanPool -eq "True")

New-VirtualDisk `
    -StoragePoolFriendlyName $raid5 `
    -FriendlyName $raid5 `
    -UseMaximumSize `
    -ResiliencySettingName "Parity" `
    -ProvisioningType Fixed
Get-Disk `
| Where-Object OperationalStatus -eq "Offline" `
| Initialize-Disk -PartitionStyle GPT -PassThru `
| New-Partition -DriveLetter $driveLetter -UseMaximumSize `
| Format-Volume -FileSystem NTFS -NewFileSystemLabel $raid5 -Confirm:$false

$folderNames = @("PepeLaughPrivate", "PepeLaughShared", "PepeLaughIT", "PepeLaughConsultant", "PepeLaughSales", "PepeLaughManagement", "PepeLaughAccounting")
# Create the folders
foreach ($folderName in $folderNames) {
    $sharePath = "R:\$folderName"
    New-Item -ItemType Directory -Path $sharePath
    New-SmbShare -Path $sharePath -Name $folderName
    Revoke-SmbShareAccess -Name $folderName -AccountName "Everyone" -Force
    Grant-SmbShareAccess -Name $folderName -AccountName "Authenticated Users" -AccessRight Full -Force
    
}
foreach ($folderName in $folderNames) {
    $sharePath = "R:\$folderName"
    $acl = Get-Acl $sharePath

    # Remove existing access rules for PepeLaughIT
    $acl.Access | Where-Object { $_.IdentityReference -match "PepeLaughIT" } | ForEach-Object { $acl.RemoveAccessRule($_) }
    $acl.Access | Where-Object { $_.IdentityReference -match "Domain Admins" } | ForEach-Object { $acl.RemoveAccessRule($_) }

    # Grant FullControl to PepeLaughIT explicitly
    $accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("PepeLaughIT", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
    $acl.SetAccessRule($accessRule)
    $accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("Domain Admins", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
    $acl.SetAccessRule($accessRule)

    # Set the AccessRules for other users
    $names = @("PepeLaughManagement")
    $permissions = "Modify"
    switch ($folderName) {
        "PepeLaughConsultant" {
            $names += "PepeLaughConsultant"
        }
        "PepeLaughSales" {
            $names += "PepeLaughSales"
        }
        "PepeLaughManagement" {
            $names += "PepeLaughManagement"
        }
        "PepeLaughAccounting" {
            $names += "PepeLaughAccounting"
        }
        "PepeLaughPrivate" {
            $names += "PepeLaughConsultant", "PepeLaughSales", "PepeLaughAccounting"
        }
        "PepeLaughShared" {
            $names += "PepeLaughConsultant", "PepeLaughSales", "PepeLaughAccounting"
        }
    }
    foreach ($name in $names) {
        foreach ($perm in $permissions) {
            $accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule($name, $perm, "ContainerInherit,ObjectInherit", "None", "Allow")
            $acl.SetAccessRule($accessRule)
        }
    }
    $acl.SetAccessRuleProtection($true, $true)
    Set-Acl $sharePath $acl
}

write-host "Installing printer drivers"
Add-PrinterDriver -Name "Microsoft OpenXPS Class Driver 2"
write-host "Adding printer"
Add-Printer -Name "PepeLaughPrinter" -DriverName "Microsoft OpenXPS Class Driver 2" -PortName "10.6.68.178"
write-host "Printer installed"
