# Setup

Instalirajte Python na vaš računalo. Možete preuzeti Python s ovog linka: https://www.python.org/downloads/

Instalirajte Anaconda Distribution. Možete preuzeti Anaconda Distribution s ovog linka: https://www.anaconda.com/products/individual#download-section

Unutar projektnog foldera, instalirajte potrebne biblioteke pomoću naredbe conda install -c anaconda aiohttp aiosqlite. Ova naredba će instalirati aiohttp i aiosqlite biblioteke u globalni Python environment.

U .py file-u, importirajte aiohttp i aiosqlite biblioteke. Početak vašeg .py file bi trebao izgledati ovako:

import aiohttp
import aiosqlite
.
.
.

# kod mikroservisa

Pri instaliranju radilo je:

python -m pip install aiohttp
python -m pip install aiosqlite
