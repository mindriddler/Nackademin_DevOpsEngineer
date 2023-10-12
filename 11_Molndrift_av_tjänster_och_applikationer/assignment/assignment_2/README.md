## Introduktion

I uppgift #2 var mitt mål att sätta upp och ansluta till en Azure File Share, ett molnbaserat filsystem. 
Nedan följer en redogörelse av de steg jag tog för att uppnå detta, utmaningar jag stötte på, samt reflektioner och lärdomar jag fick under processen.

## Table-of-Contents

- [Introduktion](#introduktion)
- [Table-of-Contents](#table-of-contents)
- [Steg som tagits](#steg-som-tagits)
  - [Navigering i Azure Portal och skapande av lagringskonto](#navigering-i-azure-portal-och-skapande-av-lagringskonto)
  - [Skapande av File Share och filuppladdning](#skapande-av-file-share-och-filuppladdning)
  - [Hämtning av anslutningsskript](#hämtning-av-anslutningsskript)
    - [Windows](#windows)
    - [Linux](#linux)
    - [MacOS:](#macos)
    - [Nycklar](#nycklar)
    - [Key 1](#key-1)
    - [Key 2](#key-2)
      - [OSB!](#osb)
- [Utmaningar jag stötte på](#utmaningar-jag-stötte-på)
    - [Lösningar och workarounds](#lösningar-och-workarounds)
- [Lärdomar och reflektioner](#lärdomar-och-reflektioner)
  - [Är Azure File Share PaaS, SaaS eller IaaS?](#är-azure-file-share-paas-saas-eller-iaas)
  - [Säkerhetsreflektion](#säkerhetsreflektion)
  - [Andra anslutningsalternativ](#andra-anslutningsalternativ)
    - [Disclaimer](#disclaimer)
- [Slutsats](#slutsats)

## Steg som tagits

### Navigering i Azure Portal och skapande av lagringskonto
Jag inledde processen genom att navigera till [Azure-portalen](portal.azure.com) och sökte efter "Storage account". 

Efter att ha konfigurerat lagringskontot med mina önskade inställningar såg jag till att "Network access" var inställd på "Allow access from all networks", vilket tillät global tillgänglighet.

### Skapande av File Share och filuppladdning
Jag fortsatte genom att välja "File shares" från menyn och etablerade en ny file share. För teständamål laddade jag upp några slumpmässiga filer till denna file share.

### Hämtning av anslutningsskript
För att upprätta en anslutning använde jag det tillhandahållna "connect"-alternativet, kopierade följande codesnippet för körning på min lokala dator.
Skickar även med för Linux och MacOS.

#### Windows
```powershell
$connectTestResult = Test-NetConnection -ComputerName fredrikcloudstorage.file.core.windows.net -Port 445
if ($connectTestResult.TcpTestSucceeded) {
    # Save the password so the drive will persist on reboot
    cmd.exe /C "cmdkey /add:`"fredrikcloudstorage.file.core.windows.net`" /user:`"localhost\fredrikcloudstorage`" /pass:`"[REDACTED]`""
    # Mount the drive
    New-PSDrive -Name Z -PSProvider FileSystem -Root "\\fredrikcloudstorage.file.core.windows.net\cloudcourse" -Persist
} else {
    Write-Error -Message "Unable to reach the Azure storage account via port 445. Check to make sure your organization or ISP is not blocking port 445, or use Azure P2S VPN, Azure S2S VPN, or Express Route to tunnel SMB traffic over a different port."
}
```

#### Linux
```bash
sudo mkdir /mnt/cloudcourse
if [ ! -d "/etc/smbcredentials" ]; then
sudo mkdir /etc/smbcredentials
fi
if [ ! -f "/etc/smbcredentials/fredrikcloudstorage.cred" ]; then
    sudo bash -c 'echo "username=fredrikcloudstorage" >> /etc/smbcredentials/fredrikcloudstorage.cred'
    sudo bash -c 'echo "password=[REDACTED]" >> /etc/smbcredentials/fredrikcloudstorage.cred'
fi
sudo chmod 600 /etc/smbcredentials/fredrikcloudstorage.cred

sudo bash -c 'echo "//fredrikcloudstorage.file.core.windows.net/cloudcourse /mnt/cloudcourse cifs nofail,credentials=/etc/smbcredentials/fredrikcloudstorage.cred,dir_mode=0777,file_mode=0777,serverino,nosharesock,actimeo=30" >> /etc/fstab'
sudo mount -t cifs //fredrikcloudstorage.file.core.windows.net/cloudcourse /mnt/cloudcourse -o credentials=/etc/smbcredentials/fredrikcloudstorage.cred,dir_mode=0777,file_mode=0777,serverino,nosharesock,actimeo=30
```

#### MacOS:
```bash
open smb://fredrikcloudstorage:[REDACTED]@fredrikcloudstorage.file.core.windows.net/cloudcourse
```

#### Nycklar

Om du behöver access nycklarna så har du dom här:
#### Key 1
- [REDACTED]
- **Connection String**
  - DefaultEndpointsProtocol=https;AccountName=fredrikcloudstorage;AccountKey=[REDACTED];EndpointSuffix=core.windows.net

#### Key 2
- [REDACTED]
- **Connection String**
  - DefaultEndpointsProtocol=https;AccountName=fredrikcloudstorage;AccountKey=[REDACTED];EndpointSuffix=core.windows.net

##### OSB!
Detta är extremt dålig practice, dessa nycklar ska aldrig få finnas på detta sätt men jag
skriver med dom här OM du behöver dom.

## Utmaningar jag stötte på

Även om uppsättningen på Azure var enkel, stötte jag på en betydande utmaning när jag försökte ansluta
till file share från min lokala maskin. När jag körde det tillhandahållna PowerShell-skriptet möttes jag av ett felmeddelande som indikerade att port 445 var blockerad.

```powershell
╭╴ Administrator ...\11_Molndrift_av_tjänster_och_applikationer\assignments\assignment_2 main [+/-] 16 1 ✓
╰╴❯ powershell.exe ./connect.ps1
WARNING: TCP connect to (20.47.32.114 : 445) failed
WARNING: Ping to 20.47.32.114 failed with status: DestinationHostUnreachable 
C:\Users\Fredrik\Repos\Nackademin\11_Molndrift_av_tjänster_och_applikationer\assignments\assignment_2\connect.ps1 : Unable to reach the Azure storage account via port 445. Check to make sure your organization or ISP is not blocking port 445, or use Azure P2S VPN, Azure S2S VPN, or Express Route to tunnel SMB traffic over a different port.
At line:1 char:1
+ ./connect.ps1
+ ~~~~~~~~~~~~~
    + CategoryInfo         : NotSpecified: (:) [Write-Error], WriteErrorException 
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,connect.ps1
```

Efter lite felsökning upptäckte jag att min Internetleverantör (ISP), Telenor, blockerade denna specifika
port. Tyvärr nekades min begäran om att avblockera porten av ISP.

#### Lösningar och workarounds
Istället för att fokusera på det lokala anslutningsproblemet beslutade jag mig för att testa anslutningen på
ett annat nätverk. Jag valde skolans nätverk, där jag lyckades ansluta utan några problem.

Jag hade kunnat gå förbi problemet på mitt hemnätverk genom att sätta upp en VPN, men för denna
uppgift ansåg jag att det var en onödig komplikation när det fungerade felfritt på ett nätverk som inte
blockerade porten.
Jag hittade även en annan lösning vid namn Azure Storage Explorer, som jag kommer att diskutera senare.

Se [Andra anslutningsalternativ](#andra-anslutningsalternativ) för mer information.

## Lärdomar och reflektioner
### Är Azure File Share PaaS, SaaS eller IaaS?
- Azure File Share kategoriseras som en Platform as a Service (PaaS). 
  I vanliga termer erbjuder detta användare en plattform för filförvaring och hantering utan komplexiteten att hantera den underliggande infrastrukturen.

### Säkerhetsreflektion
- Att dela Azure lagringskontonycklar innebär betydande risker. Dessa nycklar ger full åtkomst, vilket gör det möjligt för individer att ändra eller till och med radera all lagrad data. Det är viktigt att vara försiktig när man bestämmer vem som får tillgång till denna information.

- **Azure Role-Based Access Control (RBAC)** 
  - Istället för att distribuera nycklar kan Azures Role-Based Access Control (RBAC) användas för att ge specifika åtkomstbehörigheter. För de som är oinsatta är RBAC en mekanism genom vilken specifika roller kan tilldelas användare, vilket ger dem behörighet att utföra vissa operationer.

- **Shared Access Signatures (SAS)**
  - Ett annat alternativ till att dela nycklar är att använda Shared Access Signatures. SAS ger tillfällig, begränsad åtkomst till Azure-resurser, vilket säkerställer ettkontrollerat och säkert sätt att få åtkomst. Om en nyckel hanmar i fel händer är det viktigt att snabbt ersätta den för att förhindra obehörig åtkomst.

### Andra anslutningsalternativ
- **Azure Storage Explorer**
  - Azure Storage Explorer är ett verktyg som kan användas för att ansluta till Azure Storage Accounts. Det är ett användbart verktyg för att utforska och hantera Azure Storage Accounts, och det är också ett bra alternativ för att ansluta till Azure File Shares.
  Denna SAS nyckel slutar att fungera per automatik den 20e Oktober. Använd nedan connection strings för att ansluta till Azure File Share:

  **Connection string**
    - BlobEndpoint=https://fredrikcloudstorage.blob.core.windows.net/;QueueEndpoint=https://fredrikcloudstorage.queue.core.windows.net/;FileEndpoint=https://fredrikcloudstorage.file.core.windows.net/;TableEndpoint=https://fredrikcloudstorage.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-10-20T00:04:52Z&st=2023-10-11T16:04:52Z&spr=https&sig=[REDACTED]

  **SASToken**
    - ?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-10-20T00:04:52Z&st=2023-10-11T16:04:52Z&spr=https&sig=[REDACTED]

  **Blob Service SAS URL**
    - https://fredrikcloudstorage.blob.core.windows.net/?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-10-20T00:04:52Z&st=2023-10-11T16:04:52Z&spr=https&sig=[REDACTED]

  **File Service SAS URL**
    - https://fredrikcloudstorage.file.core.windows.net/?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-10-20T00:04:52Z&st=2023-10-11T16:04:52Z&spr=https&sig=[REDACTED]

  **Queue Service SAS URL**
    - https://fredrikcloudstorage.queue.core.windows.net/?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-10-20T00:04:52Z&st=2023-10-11T16:04:52Z&spr=https&sig=[REDACTED]

  **Table Service SAS URL**
    - https://fredrikcloudstorage.table.core.windows.net/?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-10-20T00:04:52Z&st=2023-10-11T16:04:52Z&spr=https&sig=[REDACTED]


#### Disclaimer
Dessa SAS nycklar är giltiga till den 20e Oktober 2023. Om du läser detta efter den 20e Oktober 2023 vänligen kontakta mig för att få en ny SAS nyckel. 

De är också skapade med full access till alla tjänster,vilket inte är rekommenderat i en produktionsmiljö. 

Det är viktigt att begränsa åtkomsten till de tjänstersom behövs. Men för teständamål är det enklaste sättet att få åtkomst till alla tjänster.

## Slutsats
Även om min upplevelse med Azure File Share var övervägande positiv, underströk den vikten av att beakta externa faktorer, som ISP-restriktioner, när man arbetar med moln. Som tur är så finns det tjänser på de olika cloud platformarna som kan hjälpa en att lösa externa problem som man inte har kontroll över.

Jag har lärt mig att det finns många olika sätt att ansluta till Azure File Share, och att det är viktigt att välja rätt metod för varje situation.
Denna uppgift har gett mig lärdom men jag känner ändå att Microsofts way of doing things är ganska klumpigt. 

Tillexempel:
  - **SMB**
    - Varför använder SMB fortfarande port 445? Microsoft vet att denna port blockeras av mångaISP:er, så varför inte använda en annan port som standard?
      - Jag är inte speciellt insatt i SMB protokollet så det kan vara något jag missar helt ochhållet och det finns en bra anledning till att det är som det är.

  - **Skapa ett Storage Account för att skapa File Share**
    - Varför? För mig är det mer logiskt att man enbart skapar sin File Share (Liknande GCP CloudStorage) och sätter permissions, nycklar och annat till den istället för till ett Storage Account