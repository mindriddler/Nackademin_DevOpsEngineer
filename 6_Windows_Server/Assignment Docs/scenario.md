# Scenario

- [Scenario](#scenario)
  - [Summary](#summary)
  - [Case](#case)
  - [Guidelines for the Domain](#guidelines-for-the-domain)
  - [Document list](#document-list)

## Summary

You are tasked with setting up an AD domain with at least four different OUs on the highest level in addition to the domain controllers. You need to install at least one Windows 7 or 10 machine that will join the domain. You will be given a list of settings to be managed through GPOs, and you are also expected to suggest additional GPOs that would be useful in a production environment. Finally, the installation and configuration must be documented in a professional manner.

Note: Do not start any DHCP in the lab environment.

The work must be done in groups of two.

---

## Case

You have been given the assignment to create a computer environment for company X. You do not need to offer any services. Besides setting up the computer environment (only one client machine), you are expected to write an invoice and a technical description of the server environment.

The company has emphasized the **importance of document security**, both in terms of central storage and backup, and that they cannot be read by unauthorized individuals.

**Only administrators should be able to log in locally on the file servers** (this is default on the domain controllers).

- The company has **100 users** in at least **two locations** (see the list, but you can change locations).
- Both locations should have **separate administrators** for **both computer and user accounts**.
- These local administrators should also have **local administrative rights on the user client machines**.
- You should **create groups for these OU administrators** and then **add a user to the groups**.
- You should **not** give the administrative rights directly to the accounts.

You should have **at least two printers (one per location)** that will be automatically installed on the client machines in the respective OUs.

The company should have name resolution to at least one other group in the class. You should automate the installation of a program that is linked to computer accounts, which will then automatically install the program at boot of the client machines. The user accounts should be bulk imported using any technology (I recommend PowerShell) and the import file should be attached to the invoice and server documentation. You are free to change the information in the user table, for example, they do not need to work in Stockholm and Sundsvall, and you can also change names, etc.

The employees are divided into the following groups:

- Management with a CEO
- Sales
- Consultants
- Accounting and finance
- IT support (1 person per office)

**The users should have a desktop background with the name, number, and email address of their administrator.**

Note: IMPORTANT: Rename the servers BEFORE you make them domain controllers (you can rename the other computers when they join the domain). This is also in the checklist that is in a separate file.

The domain can be named anything, but make sure you have a unique domain name.

You should come up with relevant (sensible) GPO settings. There should be a noticeable difference between the user environment at the two locations/departments. One location should have an advantage over the other in several respects...

---

## Guidelines for the Domain

You must think of relevant (reasonable) GPO settings.

There should be a noticeable difference between the user environment on both locations/departments.

One location should have a more locked down computer environment in several respects.

Neither of the administrators, either domain administrators or those with local administrative rights,
should have a restricted computer environment.

All administrators should have stricter password requirements than other user accounts.

At the first level, three OUs should be created with the following sub-OUs:

```powershell
Location
∟ Users
∟ Computers
∟ Groups

Location
∟ Users
∟ Computers
∟ Groups

Resource groups (Optional)

Servers
∟ File servers
∟ Any other servers
```

In the two group OUs, groups should be created that gather the different users. In the OU for Resource groups, there should only be groups as members and not users. Groups at different levels should be combined to share a folder on the server so that users from the folder's own group get Read and Write while another group only gets Read. All folders should
be shared with Full Control share permissions to the Authenticated users group (or possibly to Everyone).

Remember to include both Share and NTFS permissions when documenting file servers.

Presentation is done through a short demo for Erik, which is carried out after you have sent the document to me via email.

---

## Document list

- Server documentation
- Invoice including specifications (work time, hardware, software)
- List of any assumptions you have made (this is not a requirement, but you can write, for example, that you are only setting up one domain controller)
- Import file for users

---

[Back to mainpage](../../README.md)
