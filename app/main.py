from fastapi import FastAPI
from services import Services
from models.key_value_model import KeyValueModel

app = FastAPI()
services = Services()

@app.get("/")
def index():
    return {
        "success": True,
        "message": "Server active"
    }

@app.get("/get/{key}")
async def get_value(key: str):
    response = services.get_value(key)
    print(dir(response))
    if response == "Key not found":
        return {"Key not found"}
    else:
        print("cme else")
        value = response.get(True)
        print(dir(value))
        print(value)
        return {value}

@app.post("/set")
async def set_value(data: KeyValueModel):
    key, value = data.key, data.value
    print(key, value)
    response = services.set_value(key, value)
    if response == None:
        return {"Could not set the key and value"}
    value = response.get(True)
    if value == True:
        return {"Key and value set successfully"}
    return {"Could not set the key and value"}

@app.delete("/delete/{key}")
async def delete_key(key):
    response = services.delete_key(key)
    if response == None:
        return {"Could not delete the key"}
    value = response.get(True)
    return {"Key deleted successfully"}