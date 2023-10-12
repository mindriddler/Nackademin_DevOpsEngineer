# Introduktion
I uppgift #1 var mitt mål att installera AD Connect och synkronisera den med Azure AD. Nedan följer en detaljerad redogörelse av de steg jag tog, utmaningarna jag stötte på och de lärdomar jag drog av processen.

# Steg som tagits

## Nedladdning av AD Connect:
Jag laddade ner AD Connect installationsfilen från Microsofts officiella sida för AD Connect till min lokala AD server.

## Skapande av Azure AD:
Jag gick till Azure portalen och skapade en Azure Active Directory resurs (numera kallad Microsoft Entra ID), och döpte den till "fredrikio.onmicrosoft.com". Jag ändrade sedan mitt användarnamn i den nya AD till "fredrik@fredrikio.onmicrosoft.com" för att förenkla inloggningen då adressen är lättare att komma ihåg än den ursprungliga.

## Installation av AD Connect:
Jag påbörjade installationen av AD Connect på min lokala server genom att klicka på installationsfilen och följde installationsguiden. 
Direkt här stötte jag på problem då jag fick ett felmeddelande som indikerade att mitt lokala AD inte var kompatibelt med Azure AD. Jag insåg att detta berodde på att jag hade använt domännamnet "fredrik.local" för mitt lokala AD, vilket inte är kompatibelt med Azure AD. Jag löste detta genom att skapa om mitt lokala AD och använda domännamnet "fredrik.io" istället.
Därefter fortsatte jag med installationen och valde "Express Settings" för att förenkla processen.
Under installationsprocessen blev jag ombedd att ange mina Azure AD-inloggningsuppgifter. 
Jag stötte på problem här eftersom jag initialt försökte logga in med min skolmail, men insåg senare att jag behövde använda "fredrik@fredrikio.onmicrosoft.com" för inloggningen. 
Efter detta fortsatte jag med installationen utan problem.

## Verifikation:
När installationen var klar, gick jag tillbaka till Azure portalen och navigerade till min Azure AD resurs. Där kunde jag se att mina lokala användare nu var synkroniserade till Azure AD. Jag observerade också att synkroniseringen hade skett i samband med att installationen blev klar.

## Ytterligare Test:
För att testa synkroniseringsprocessen ytterligare, skapade jag en ny grupp och en ny användare i mitt lokala AD. Jag kunde bekräfta att dessa nya objekt synkroniserades till Azure AD som väntat, vilket indikerade att allt fungerade som det skulle.

## Utmaningar och Lösningar
### Domänproblem:
Det första stora problemet var domännamnet "fredrik.local" som inte var kompatibelt med Azure AD. Lösningen var att skapa om mitt lokala AD och använda domännamnet "fredrik.io" istället.

### Autentiseringsproblem:
Det andra problemet var relaterat till autentisering under installationsprocessen av AD Connect. Eftersom mitt Azure konto är skapat med min skolmail så trodde jag att jag behövde använda den för AD Connecet men så var inte fallet och satt fast där ett litet tag men efter lite googlande så provade jag att logga in med "fredrik@fredrikio.onmicrosoft.com" som jag skapat tidigare i Azure AD och då gick det.

## Lärdomar och Reflektioner
Denna uppgift gav mig en djupare förståelse för vikten av korrekt domän- och autentiseringskonfiguration när man arbetar med Azure AD och AD Connect. Jag lärde mig också hur viktigt det är att noggrant följa installationsguiden och använda korrekt inloggningsinformation.

## Slutsats
Trots de utmaningar jag stötte på, lyckades jag med uppgiften och fick en värdefull erfarenhet av arbete med Azure AD och AD Connect. Jag har nu en bättre förståelse för hur dessa system interagerar och hur man hanterar möjliga hinder under installations- och konfigurationsprocessen.