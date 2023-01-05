import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

async def get_stotku(session, offset):
    result = await session.get(f"http://0.0.0.0:8080/getDataDB?offset={offset}")
    return await result.json()

@routes.get("/getData")
async def get_data(request):
    try:
        tasks = []
        async with aiohttp.ClientSession() as session:
            for a in range(0, 10001, 100):
                dz = await get_stotku(session, a)

                tasks.append(asyncio.create_task(session.post("http://0.0.0.0:8082/WT", json = dz)))
                tasks.append(asyncio.create_task(session.post("http://0.0.0.0:8083/WT", json = dz)))

                resp = await asyncio.gather(*tasks)
                data = [await data.json() for data in resp]
                
        return web.json_response({ "service_id": 1, "data": data }, status = 200)

    except Exception as ex:
        return web.json_response({ "Error": str(ex) })

app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port = 8081)

"""
1. Microservis asinkrono poziva e-ucenje API (Microservis 1), 

te prosljeduje podatke kao dictionary Worker tokenizer (WT) microservisu. 
"""