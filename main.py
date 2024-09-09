import asyncio
import json
from pprint import pprint
from typing import List, Dict
from fastapi import FastAPI, UploadFile, File

from util.types import Part, PartsList

import camelot

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/wake_up")
async def wake_up():
    return {"message": "Waking up"}, 200


@app.post('/process')
async def process(post_file: UploadFile = File(...)):
    c = camelot.read_pdf(post_file.file, pages='1-end', flavor="stream")
    headers: List[str] = []
    objects: List[Part] = []
    present_parent = ""

    for table in c:
        # Convert the table to a list of dictionaries
        parsed_data: List[Dict[str, str]] = table.df.to_dict(orient='records')

        for obj in parsed_data:
            # If first item is not empty and others are empty, check if header item
            if obj["0"] != "" and all(obj[str(index)] == "" for index in range(1, 5)):
                headers.append(obj["0"])
                present_parent = obj["0"]
            if present_parent != "" and all(obj[str(index)] != "" for index in range(len(obj))):
                # If the ref has a '.', it's valid
                if "." in obj["1"].__str__():
                    parsed_part = Part(
                        parent=present_parent,
                        code=obj["0"],
                        ref=obj["1"],
                        quantity=obj["4"],
                        size=obj["3"]
                    )
                    objects.append(parsed_part)
                    pprint(parsed_part.to_json())

        with open('output.json', 'w') as outfile:
            json.dump(PartsList(name=present_parent, parts=objects).to_json(), outfile)

        return PartsList(name="test", parts=objects).to_json()
#     asyncio.run(process())
