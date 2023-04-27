# -*- coding: utf-8 -*-
# uvicorn main:app --reload --host 0.0.0.0 --port 8000

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import json
from .dependencies import (
    data_work,
)


router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/", response_class = HTMLResponse)
def root( request: Request ):

    with open('src/data/ping_info.json', 'r') as file:
        data = json.load(file)
        data = data_work(data)

    return templates.TemplateResponse("monitoring.html", {"request": request, "data": data})


@router.get("/get_ping_info")
def get_ping_info():
    with open('src/data/ping_info.json', 'r') as file:
        data = json.load(file)
        data = data_work(data)        

    return data



## -------------------------------------------------------------------------- ##
## Comentado hasta entender el menejo de multiples clientes
## -------------------------------------------------------------------------- ##

# from typing import List
# from fastapi import WebSocket, WebSocketDisconnect
# from time import sleep

# SEND_INTERVAL = 5

# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: List[WebSocket] = []

#     async def connect(self, websocket: WebSocket):
#         await websocket.accept()
#         self.active_connections.append(websocket)

#     def disconnect(self, websocket: WebSocket):
#         self.active_connections.remove(websocket)

#     async def send_personal_message(self, message: str, websocket: WebSocket):
#         await websocket.send_text(message)

#     async def broadcast(self, message: str):
#         for connection in self.active_connections:
#             await connection.send_text(message)



# manager = ConnectionManager()

# @router.websocket("/ws/{client_id}")
# async def websocket_endpoint(websocket: WebSocket, client_id: int):
#     # await websocket.accept()
#     await manager.connect(websocket)
#     try:
#         while True:
#             print("live response...")
#             sleep( SEND_INTERVAL )

#             with open('src/data/ping_info.json', 'r') as file:
#                 data = json.load(file)
#                 data = data_work(data)
            
#             # await websocket.send_text(json.dumps(data))
#             await manager.send_personal_message(json.dumps(data), websocket)

#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         # await manager.broadcast(f"")


