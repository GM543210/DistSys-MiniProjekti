import aiohttp
import aiosqlite
import asyncio
import aiofiles
from aiohttp import web
import json

routes = web.RouteTableDef()

global DATABASE
DATABASE = "Mini_Projekt/DB/Database.db"

def dissolve_data(objct):
    elem = (
        objct["repo_name"].split("/")[0],
        "https://github.com/" + objct["repo_name"],
        objct["path"].split("/")[-1],
        objct["content"]
    )
    return elem
        
async def inspect_DB():
    async with aiosqlite.connect(DATABASE) as database:
        cursor = await database.cursor()
        await cursor.execute("SELECT COUNT(*) FROM e_ucenje")

        count = await cursor.fetchall()
        
        if count[0][0] == 0:
            await shove_in_DB()


async def shove_in_DB():
    async with aiofiles.open("Mini_Projekt/DB/ProjectFiles/FakeData.json", mode = "r") as file:
        a = 0        
        async for line in file:
            async with aiosqlite.connect(DATABASE) as database:
                await database.execute(
                    "INSERT INTO e_ucenje (username, git_hw_link, file_naming, contents_of_file) VALUES (?, ?, ?, ?)",
                    dissolve_data(json.loads(line))
                )
                await database.commit()
            a += 1
            if a == 10000:
             return

@routes.get("/getDataDB")
async def get_data_db(request):
    try:   
        response = {
            "service_id": 0, "data": {
                                 "usernames": [],
                                 "git_hw_link": [],
                                 "file_naming": [],
                                 "contents_of_file": []
                                }
        }

        limit = 100
        
        offset = request.query["offset"]
        async with aiosqlite.connect(DATABASE) as database:
                async with database.execute(f"Select * FROM e_ucenje LIMIT {limit} OFFSET {offset}") as cursor:
                    async for seq in cursor:
                        response["data"]["usernames"].append(seq[1])
                        response["data"]["git_hw_link"].append(seq[2])
                        response["data"]["file_naming"].append(seq[3])
                        response["data"]["contents_of_file"].append(seq[4])
                        await database.commit()

        return web.json_response(response , status = 200)
    
    except Exception as ex:
        return web.json_response({"Error":str(ex)})
asyncio.run(inspect_DB())


app = web.Application()
app.router.add_routes(routes)
#web.run_app(app, port = 8080)
web.run_app(app)

"""
0. Fake E-ucenje API microservis (M0). 
Sastoji se od DB i jedne rute koja vraca github linkove na zadace. (parse_data)

Prilikom pokretanja servisa, provjerava se postoje li podaci u DB. ( inspect_DB())
Ukoliko ne postoje, pokrece se funkcija koja popunjava DB s testnim podacima (10 000). 
(shove_in_DB())

Kad microservis zaprimi zahtjev za dohvacanje linkova, 
uzima maksimalno 100 redataka podataka iz DB-a. (Get stotku)
"""