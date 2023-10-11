Denna är till en övning under dagen. Den ska installeras lokalt på din SQL-server, och sedan ska vi se hur vi gör för att flytta den till Azure. 

Gör så här för att installera lokalt: 

- Hämta filen, normalt hamnar den i din privata Download (som SQL inte har rättigheter att läsa)
- Kopiera den till en annan mapp som SQL får läsa, exempelvis C:\Temp
- Packa upp zip-filen
- Gå in i SQL Management Studio
- Högerklicka på Databases
- Välj Restore Database...
- Ange Device > klicka på knappen med de tre prickarna > klicka på Add > leta upp .bak-filen > klicka på OK ett par gånger.