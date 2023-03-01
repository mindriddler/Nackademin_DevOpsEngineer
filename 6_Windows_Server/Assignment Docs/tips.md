# Tips & Comments

- [Tips \& Comments](#tips--comments)
  - [Step 1](#step-1)
  - [Step 2](#step-2)
  - [Step 3](#step-3)
  - [Step 4](#step-4)
  - [Step 5](#step-5)
  - [Step 6](#step-6)
  - [Step 7](#step-7)
  - [Tip](#tip)
  - [Prohibited](#prohibited)
  - [More tips](#more-tips)

Tips and comments for the scenario lab
A few short tips to facilitate and speed up the installation of the virtual lab environment

Take one of the existing host computers from the Windows Server course

## Step 1

    Open the Hyper-V manager first shut down all virtual machines

## Step 2

    Discard the virtual machines you no longer want to save, such as "Surf computer" and other test machines

## Step 3

    Go into the C:\VM folder and discard the folders of the virtual machines you have discarded in step 2

## Step 4

    Rename any virtual machines you want to save so that they have a z or _ before their name
    Example: Server1 => z_server1, DC => z_DC

## Step 5

    Always create a new folder in the C:\VM directory for each new virtual machine you are going to create. Don't be careless with this

## Step 6

    Create clients and servers by creating differential disks pointing to mother disks for Windows2022 and possibly Windows 7
    NOTE Windows 7 is only 32-bit and will not be able to take 64-bit software installations or 64-bit drivers for printers you install with GPOs,
    so I recommend that you install some Virtual Windows 10 or 11 instead

## Step 7

    Install your Windows 10 or 11 using ISO binding to new virtual machines
    See instructions for setting up your own lab environment for info on how to set up a virtual Windows 11

## Tip

    Use the classroom network as a network
    All extra disks for your VM (e.g. for file servers) should be SCSI

## Prohibited

    Setting up your own DHCP server on the classroom network

## More tips

    If you are going to have two identical domain controllers in your environment,
    it is enough to set up one of them,
    then you write the documentation as if you have both (just copy the text and then change the name and IP address in the documentation of DC1)
    However, if you have two DCs that are also file servers and are to be used for different things,
    it is best to throw both up in the lab environment
    Use static IP addresses for your servers, let the classroom's DHCP server lend IP addresses to your hosts and clients
    but don't forget to redirect the clients' Preferred DNS to point to your own domain controller

    The next tip is not to disturb the environment too much.
    This is a small company, you don't need to resort to all the cool techniques that exist,
    just stick with the ones we've gone through (e.g. we haven't learned how to administer sites so I don't expect you to configure that)

    See Erik's work schedule/checklist

    If you have problems with the name resolution against the internet,
    just add a Forwarder to your DNS (not a conditional forwarder) that points to 8.8.8.8 or 1.1.1.1

    One last thing for this time. Roaming Profiles (network pointing of user profile) is the 90s, we have learned to manage Folder Redirection

---

[Back to mainpage](../../README.md)
