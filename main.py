from fastapi import FastAPI

app = FastAPI()


@app.get("/<password>")
async def root(password):
    # 1. Read passwordList.txt file as list of strings
    # 2. search for the coming password in the password list from step 1
    # 3. return the found password's number
    return {"message": "Hi LOLO"}
