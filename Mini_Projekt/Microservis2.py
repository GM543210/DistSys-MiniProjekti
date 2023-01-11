import asyncio
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

def extract_w(d):
    res = []
    for a, b in enumerate(d["usernames"]):
        if b[0].lower() == "w":
            res.append({
                "username": b,
                "git_hw_link": d["git_hw_links"][a],
                "file_naming": d["file_namings"][a],
                "contents_of_file": d["contents_of_files"][a]
            })
    return res

@routes.post("/WTW")
async def work_tok(request):
    try:
        rq = await request.json()

        async with aiohttp.ClientSession() as session:
                result = await session.post("http://localhost:8084/gatherData",
                json = extract_w(rq["data"]))
                result.close()

        return web.json_response({ "service_id": 2, "status": "it works"}, status = 200)

    except Exception as ex:
        return web.json_response({ "service_id": 2, "Error": str(ex) }, status = 500)

app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port = 8082)




"""
2. WT microservis uzima dictionary. Uzima samo redove gdje username
pocinje na w. Prosljeduje kod 4. microservisu.

"""