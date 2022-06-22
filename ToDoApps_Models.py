from pydantic import BaseModel
from fastapi import Form
class ToDoAppsModels(BaseModel):
    Task: str
    finish: bool
    @classmethod
    def as_form(cls,Task: str= Form(...)):
        return cls(Task=Task,finish=False)