import uvicorn
from fastapi import FastAPI,Request,HTTPException,Form,Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
from ToDoApps_Models import *
from starlette.responses import RedirectResponse

ToDoList = []
app = FastAPI()
templates = Jinja2Templates(directory='template')

@app.get("/list/", response_model= List[ToDoAppsModels])
async def tampilkan():
    return ToDoList


@app.get("/index",response_class=HTMLResponse)
async def tes(request:Request):
    return templates.TemplateResponse("ToDoApps.html", {"request":request, "data":ToDoList})

@app.post("/add_data/")
async def tampilans(form_data: ToDoAppsModels = Depends(ToDoAppsModels.as_form)):
    ToDoList.append(form_data)
    return RedirectResponse("/index", status_code=303)

@app.get("/hapus/{id}")
def awd(id:int):
    ToDoList.pop(id-1)
    return RedirectResponse("/index", status_code=303)

@app.get("/finish/{id}")
def update(id:int):
    ToDoList[id-1].finish = True
    return RedirectResponse("/index", status_code=303)



if __name__ == '__main__':
    uvicorn.run(app)
