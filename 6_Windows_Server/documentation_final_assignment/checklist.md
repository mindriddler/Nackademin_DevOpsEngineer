# Checklist

The lab will go smoothly and the work will be efficient if you more or less work in this order, extra smooth if you work continuously with documentation.

- [Checklist](#checklist)
  - [1. Design and Plan](#1-design-and-plan)
  - [2. Mail the domain](#2-mail-the-domain)
  - [3. Shut down old virtual machines](#3-shut-down-old-virtual-machines)
  - [4. Set up your servers](#4-set-up-your-servers)
  - [5. Fix the IP addresses](#5-fix-the-ip-addresses)
  - [6. Rename Domain Controller](#6-rename-domain-controller)
  - [7. Promote Domain Controller](#7-promote-domain-controller)
  - [8. Join the other servers](#8-join-the-other-servers)
  - [9. Promote additional DC](#9-promote-additional-dc)
  - [10. Create the OU structure](#10-create-the-ou-structure)
  - [11. Import User Accounts](#11-import-user-accounts)
  - [12. Create Groups](#12-create-groups)
  - [13. Distributions and rights](#13-distributions-and-rights)
  - [14. GPO](#14-gpo)
  - [15. Join clients to the domain](#15-join-clients-to-the-domain)
  - [16. Test settings and rights](#16-test-settings-and-rights)
  - [17. Check requirements](#17-check-requirements)
  - [18. Complete the documentation](#18-complete-the-documentation)
  - [19. Where's ma money?](#19-wheres-ma-money)

---

## 1. Design and Plan

    Design and plan your environment on paper, preferably use A3 paper. Make sure you get a unique domain name

---

## 2. Mail the domain

    Mail the domain name to Erik.
    NOTE Do not skip this

---

## 3. Shut down old virtual machines

    Go into Hyper-V on the machine(s) you are going to set up the environment start by making sure all old virtual machines are shut down and then add the letter z to the beginning of the name of any existing virtual machines so you don't mix them up with your WC for the scenario lab.

---

## 4. Set up your servers

    Set up your servers, easiest by working with differentiation disks that point to one of the mother disks on the course computers, but it is also fine to copy one of the mother disks. Start by creating a folder for each VM, do not put any files directly in the VM folder. Clients with Windows 10 or 11 can be installed from an installation file.

---

## 5. Fix the IP addresses

    Configure them with the fixed IP addresses assigned to your group, enter 10.6.68.1 as gateway and 255.255.255.0 as Subnet mask.

---

## 6. Rename Domain Controller

    Rename your first DC and restart

---

## 7. Promote Domain Controller

    Promote your first DC

---

## 8. Join the other servers

    Join your other servers to the domain and rename it at the same time.

---

## 9. Promote additional DC

    Promote any additional DC (Optional)

---

## 10. Create the OU structure

    Create the OU structure

---

## 11. Import User Accounts

    Import user accounts

---

## 12. Create Groups

    Create and popularize groups

---

## 13. Distributions and rights

    Create distributions and set correct rights.

---

## 14. GPO

    Create and configure desired GPOs

---

## 15. Join clients to the domain

    Set up one or two client computers and join them to the domain

---

## 16. Test settings and rights

    Test settings and rights

---

## 17. Check requirements

    Check that you have met the requirements/desires in the scenario

---

## 18. Complete the documentation

    Complete the documentation, don't forget the GPO report in HTML format which is easiest to fix with PowerShell. NOTE Do not generate separate reports for each GPO but one report for all GPOs

---

## 19. Where's ma money?

    Invoice

---

[Back to mainpage](../../README.md)
