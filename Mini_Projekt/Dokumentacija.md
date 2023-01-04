# The Plan

### 1

Da biste započeli s ovim projektnim zadatkom bez korištenja virtualnih okruženja i bez korištenja Flask biblioteke, slijedite sljedeće korake:

Instalirajte Python na vaš računalo. Možete preuzeti Python s ovog linka: https://www.python.org/downloads/

Instalirajte Anaconda Distribution. Možete preuzeti Anaconda Distribution s ovog linka: https://www.anaconda.com/products/individual#download-section

Otvorite Visual Studio Code i kreirajte novi projektni folder.

Otvorite konzolu u Visual Studio Codeu tako da pritisnete tipku "Ctrl + '" ili odaberete "Terminal > New Terminal" iz izbornika.

Unutar projektnog foldera, instalirajte potrebne biblioteke pomoću naredbe conda install -c anaconda aiohttp aiosqlite. Ova naredba će instalirati aiohttp i aiosqlite biblioteke u globalni Python environment.

Unutar projektnog foldera, kreirajte novi Python file s imenom "main.py". Ovo će biti glavni file vašeg mikroservisa.

U main.py file-u, importirajte aiohttp i aiosqlite biblioteke. Vaš main.py file bi trebao izgledati ovako:

Copy code
import aiohttp
import aiosqlite

# kod vašeg mikroservisa
Pokrenite vaš mikroservis pomoću naredbe python main.py. Vaš mikroservis će se pokrenuti.