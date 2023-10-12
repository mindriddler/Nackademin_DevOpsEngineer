## Introduktion

I uppgift #3 var mitt mål att sätta upp en nginx webbserver i en containerinstans i Azure.
Nedan följer en redogörelse av de steg jag tog för att uppnå detta, utmaningar jag stötte på, samt reflektioner och lärdomar jag fick under processen.

## Table-of-Contents

- [Introduktion](#introduktion)
- [Table-of-Contents](#table-of-contents)
- [Navigering i Azure Portalen](#navigering-i-azure-portalen)
- [Konfiguration av Containern](#konfiguration-av-containern)
- [Nätverksinställningar](#nätverksinställningar)
- [Distribution](#distribution)
- [Åtkomst till Nginx](#åtkomst-till-nginx)
- [Reflektion](#reflektion)

## Navigering i Azure Portalen
Från Azure portalen klickade jag på "Create Resource" och sökte efter "Container Instances". Jag valde
"Container Instances" från listan över tillgängliga resurser och klickade på "Create" för att skapa en ny
containerinstans.

## Konfiguration av Containern
Under fliken "Basics" angav jag nödvändiga uppgifter som prenumeration, resursgrupp, container-namn
och region. För imagesource valde jag "Quickstart images" och valde "Nginx" som image.

## Nätverksinställningar
Nästa steg var att gå till fliken "Networking". Jag följde min namnstandard (fredrik-student-X) och jag såg
till att port 80 var öppen för TCP för att tillåta HTTP-åtkomst.

## Distribution
Efter att ha granskat alla konfigurationer klickade jag på "Skapa" för att distribuera containerinstansen.

## Åtkomst till Nginx
När distributionen var klar gick jag in på containerinstansen för att få min FQDN. Med hjälp av denna FQDN kom jag år nginx-webbsidan via min webbläsare och möttes av meddelandet "Welcome to nginx!".

**FQDN:** 
- `fredrik-nginx.frbpe6fxapgkaze5.northeurope.azurecontainer.io`

**Public IP:** 
- `20.54.5.190`

## Reflektion
Detta var den enklaste uppgiften och tog högst 5 minuter att göra klart. Men det är värdefull kunskap att veta att man kan slänga upp en webserver på kort tid genom att använda Container Instances resursen.