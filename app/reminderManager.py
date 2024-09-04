import time
import json

from app.path import CUR_DIR


async def getDataFromJson():
    filePath = f'{CUR_DIR}\\json\\reminder.json'

    with open(filePath, 'r') as file:
        data = json.load(file)
    
    return data

async def setDataToJson(data):
    filePath = f'{CUR_DIR}\\json\\reminder.json'

    with open(filePath, 'w') as file:
        json.dump(data, file, indent=4)

async def getIdListrByTime(time):
    data = getDataFromJson()

    id_list = []

    for key in data[time]:
        id_list.append(key)

    return id_list

async def getDescriptionListById(id, time):
    data = getDataFromJson()
    
    return data[time][id]

async def getDataListById(id):
    data = getDataFromJson()

    result = {}

    for time in data:
        if id in data[time]:
            result.update({
                time: data[time][id]
            })

    return result

async def setDataByTime(time, obj):
    data = getDataFromJson()

    data[time].update(obj)

    setDataToJson(data)

async def updateDataByTime(time, id, description):
    data = getDataFromJson()

    data[time][id] = description

    setDataToJson(data)