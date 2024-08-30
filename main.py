import asyncio
import json
from pprint import pprint
from typing import List, Dict
from fastapi import FastAPI

from util.types import Part, PartsList

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/wake_up")
async def wake_up():
    return {"message": "Waking up"}, 200


@app.get('/process')
async def process():
    with open('foo-page-1-table-1.json') as f:
        #how many tables are there in the doc
        headers: List[str] = []
        objects: List[Part] = []
        present_parent = ""
        data = f.read()

        parsed_data:List[Dict[str, str]] = json.loads(data)

        # for index in range(len(parsed_data)):
            # print(f"parsed_data: {parsed_data[index]}")

        for obj in parsed_data:
            #if first item is not empty and other are
            #check if header item
            if obj["0"] != "" and all(obj[str(index)] == "" for index in range(1, 5)):
                headers.append(obj["0"])
                present_parent = obj["0"]
                # print(f"present_parent -> {present_parent}")


            if present_parent != "" and all(obj[str(index)] != "" for index in range(len(obj))):
                # if obj["1"] != "C\u00f3d":
                #if the ref has a '.' it's valid
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

# if __name__ == "__main__":
#     asyncio.run(process())
