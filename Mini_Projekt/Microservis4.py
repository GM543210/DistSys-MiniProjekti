import aiohttp
from aiohttp import web
import aiofiles
import asyncio

routes = web.RouteTableDef()
global GATHERED_DATA
GATHERED_DATA = []

async def create_files():
    for elem in GATHERED_DATA:
        async with aiofiles.open(f"Mini_Projekt/ProjectFiles/{elem['file_naming']}", mode = "w", encoding = "utf-8") as file:
            await file.write(elem["content"])


@routes.post("/gatherData")
async def gather_data(request):
    req = await request.json()

    GATHERED_DATA.extend(req)
    if (len(GATHERED_DATA) > 10):
        await create_files()
    return web.json_response({ "status": "it works" }, status = 200)

app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port = 8084)


"""
4. microservis sastoji od rute (/gatherData) sprema se Python kod u listu.

Ako ima više od 10 elemenata unutar liste asinkrono se kreiraju svi file-ovi iz liste.
"""