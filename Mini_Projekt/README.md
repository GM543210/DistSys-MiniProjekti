# DistSys - Prvi mini projekt

### 1. Prvi mikroservis
Fake E-ucenje API microservis (M0). Sastoji se od DB i jedne rute koja vraca github linkove na zadace. Prilikom pokretanja servisa, provjerava se postoje li podaci u DB. Ukoliko ne postoje, pokrece se funkcija koja popunjava DB s testnim podacima (10000). Kad microservis zaprimi zahtjev za dohvacanje linkova, uzima maksimalno 100 redataka podataka iz DB-a.

### 2. Drugi mikroservis
Microservis asinkrono poziva e-ucenje API (M1), te prosljeđuje podatke kao dictionary Worker tokenizer (WT) microservisu.

### 3. Treći mikroservis
WT microservis uzima dictionary. Uzima samo redove gdje username pocinje na w. Prosljeđuje kod 4. microservisu.

### 4. Četvrti mikroservis
WT microservis uzima dictionary. Uzima samo redove gdje username pocinje na d. Prosljeđuje kod 4. microservisu.

### 5. Peti mikroservis
Microservis sastoji od rute (/gatherData) sprema se Python kod u listu. Ako ima više od 10 elemenata unutar liste asinkrono se kreiraju svi file-ovi iz liste.