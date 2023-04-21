# Check if the $TaskName exists
$TaskName = "ADStuff"
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

# Create array of OUs and their nested attributes
$ouVariables = @{
    "PepeLaugh" = @{
        "Users"     = @{
            "IT"         = $true
            "Consultant" = $true
            "Sales"      = $true
            "Management" = $true
            "Accounting" = $true
        }
        "Groups"    = $true
        "Computers" = $true
    }
    "TriHard"   = @{
        "Users"     = @{
            "IT"         = $true
            "Consultant" = $true
            "Sales"      = $true
            "Management" = $true
            "Accounting" = $true
        }
        "Groups"    = $true
        "Computers" = $true
    }
    "Servers"   = $true
}



# Create top level OUs based on the keys of the $ouVariables Hashtable
foreach ($ou in $ouVariables.Keys) {
    $ouPath = "DC=ItsCrap,DC=io"
    New-ADOrganizationalUnit -Name $ou -Path $ouPath -ProtectedFromAccidentalDeletion $true
    Write-Host "OU $ou created"

    # Check if there are any nested OUs and create them if necessary
    $nestedOUs = $ouVariables[$ou] | Where-Object { $_.GetType().Name -eq "Hashtable" }
    foreach ($subOU in $nestedOUs.Keys) {
        $subOUPath = "OU=$ou,$ouPath"
        New-ADOrganizationalUnit -Name $subOU -Path $subOUPath -ProtectedFromAccidentalDeletion $true
        Write-Host "Nested OU '$subOU' created under '$ou'"
        
        # Check if there are any furthur nested OUs and create them if necessary
        $nestedNestedOUs = $nestedOUs[$subOU] | Where-Object { $_.GetType().Name -eq "Hashtable" } 
        foreach ($subSubOU in $nestedNestedOUs.Keys) {
            $subSubOUPath = "OU=$subOU,$subOUPath"
            New-ADOrganizationalUnit -Name $subSubOU -Path $subSubOUPath -ProtectedFromAccidentalDeletion $true
            Write-Host "Nested OU '$subSubOU' created under '$subOU'"
        }
    }
}

$OUPaths = @{
    "PepeLaugh" = "OU=Groups,OU=PepeLaugh,DC=ItsCrap,DC=io"
    "TriHard"   = "OU=Groups,OU=TriHard,DC=ItsCrap,DC=io"
}
$Prefixes = @{
    "PepeLaugh" = "PepeLaugh"
    "TriHard"   = "TriHard"
}

$GroupNames = @("IT", "Consultant", "Sales", "Management", "Accounting")
# Iterate through a list of OUs from the $OUPaths dictionary
foreach ($OUPath in $OUPaths.Values) {
    # Get the OU name from the path string 
    $OU = $OUPath.Split(',')[1].Substring(3)
    # Get the prefix for the group name based on the OU
    $Prefix = $Prefixes[$OU]
    # Loop for every group name in the list
    foreach ($GroupName in $GroupNames) {
        # Create a new Active Directory group with a name that contains the prefix
        $GroupNameWithPrefix = "$Prefix$GroupName"
        New-ADGroup -Name $GroupNameWithPrefix -GroupCategory Security -GroupScope Global -Path $OUPath
        Write-Host "Group $GroupNameWithPrefix created in $OUPath"
    }
}

# Create user accounts  
$Users = Import-Csv -Path "C:\script\employees.csv"
# Iterate through users in CSV
foreach ($User in $Users) {
    $Displayname = $User.'Firstname' + " " + $User.'Lastname'
    $UserFirstname = $User.'Firstname'
    $UserLastname = $User.'Lastname'
    $Location = $User.'Location'
    $Description = $User.'Position'
    # Check if the username is already created and append an int to it 
    $OU = "OU=$Description,OU=Users,OU=$Location,DC=ItsCrap,DC=io"
    $SAM = $User.'Lastname'
    $i = 0
    $OriginalSAM = $SAM
    # Check if the SAM account name already exists in AD
    while (Get-ADUser -Filter "SamAccountName -eq '$SAM'" -ErrorAction SilentlyContinue) {
        $i++
        $SAM = $OriginalSAM + $i
    }
    # Create UPN using the username and add other details 
    $UPN = $SAM + "@ItsCrap.io"
    
    $Password = 'Linux4Ever'
    $Group = $Location + $Description
    # Create Windows Active Directory User
    New-ADUser `
        -Name "$Displayname" `
        -SamAccountName $SAM `
        -UserPrincipalName $UPN `
        -GivenName "$UserFirstname" `
        -Surname "$UserLastname" `
        -Description "$Description" `
        -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) `
        -Enabled $true -Path "$OU" `
        -ChangePasswordAtLogon $true `
        -PasswordNeverExpires $false 
    Write-Host "Created account for user $Displayname"
    # Add user to Group membership
    Add-ADGroupMember -Identity $Group -Members $SAM
    Write-Host "Added $SAM to $Group"
}

