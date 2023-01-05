import asyncio
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

def extract_d(d):
    res = []
    for a, b in enumerate(d["usernames"]):
        if b[0].lower() == "d":
            res.append({
                "username": b,
                "git_hw_link": d["git_hw_links"][a],
                "file_naming": d["file_namings"][a],
                "contents_of_file": d["contents_of_files"][a]
            })
    return res

@routes.post("/WT")
async def work_tok(request):
    try:
        rq = await request.json()
        tasks = []
        async with aiohttp.ClientSession() as session:
            tasks.append(asyncio.create_task(
                session.post("http://0.0.0.0:8084/gatherData",
                json = extract_d(rq["data"]
            ))))

            await asyncio.gather(*tasks)
            await session.close()

        return web.json_response({ "service_id": 3, "status": "it works"}, status = 200)

    except Exception as ex:
        return web.json_response({ "Error": str(ex) }, status = 500)

app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port = 8083)

"""
3. WT microservis uzima dictionary. Uzima samo redove gdje username
pocinje na d. Prosljeduje kod 4. microservisu.

"""