import asyncio
import mysql
import logging
logging.basicConfig(level=logging.INFO)
from aiohttp import web
routes = web.RouteTableDef()
async def get_text():
    with open('1.txt','r',encoding='utf8') as f:
        return f.read()
@routes.get('/')
async def index(request):
    # s = mysql.Database('47.101.53.77', 'root', 'ppaa1122', 'test')
    # a=s.select_Mysql('select * from t_student',0)
    aa=await get_text()
    return web.Response(body=aa,content_type='text/html',charset='utf8')
@routes.get('/{name}')
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>Hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')
app = web.Application()
app.add_routes(routes)
web.run_app(app, host='0.0.0.0', port=8000)
logging.info('开始记录')