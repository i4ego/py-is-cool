from fastapi import FastAPI #imports. please, install all packages: "pip install fastapi uvicorn pydantic"
from uvicorn import run
from pydantic import BaseModel
from random import randint as create_id
app = FastAPI() #api init
users = dict() #users
class response(BaseModel): #type "response"
  name: str
  password: str
@app.post('/reg') #registration (send POST request to http://127.0.0.1:8000/reg )
async def reg(res: response):
  id = create_id(0, 100000)
  while id in users:
    id = create_id(0, 100000)
  users[id] = res
  return id
@app.get('/') #userlist (send POST request to http://127.0.0.1:8000/ )
async def getusers():
    return users
if __name__ == '__main__': #running API
  run(app)
