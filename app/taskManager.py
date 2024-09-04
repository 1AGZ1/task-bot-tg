import json
from app.path import CUR_DIR, check_file_exists


async def getDataFromJson(id):
    filePath = f'{CUR_DIR}/json/{id}.json'

    if check_file_exists(filePath):
        with open(filePath, 'r') as file:
            data = json.load(file)
    else:
        with open(filePath, 'w') as file:
            data = {}
            
            json.dump(data, file, indent=4)

    return data

async def setDataToJson(id, data):
    filePath = f'{CUR_DIR}/json/{id}.json'

    with open(filePath, 'w') as file:
        json.dump(data, file, indent=4)

async def getNameByPath(id, path):
    data = await getDataFromJson(id)

    return data[path]['name']

async def getDescriptionByPath(id, path):
    data = await getDataFromJson(id)

    return data[path]['description']

async def addObjByPath(id, obj, path):
    data = await getDataFromJson(id)

    data.update({path: obj})

    await setDataToJson(id, data)

async def delObjByPath(id, path):
    data = await getDataFromJson(id)

    data.pop(path)

    await setDataToJson(id, data)

async def getPathListByPath(id, path):
    data = await getDataFromJson(id)

    return list(filter(lambda key: key.startswith(path) and (path.count('/') == key.count('/') - 1), data.keys()))

async def getNamesListByPathList(id, pathList):
    data = await getDataFromJson(id)

    nameList = []
    for path in pathList:
        nameList.append(data[path]['name'])

    return nameList




'''
class Task:
    name: str
    description: str
    content: list

    def __init__(self, name: str, description: str, content: list):
        self.name = name
        self.description = description
        self.content = content

    def getName(self):
        return self.name
    def getDescription(self):
        return self.description
    def getContent(self):
        return self.content
    
    def setName(self, name : str):
        self.name = name
    def setDescription(self, description: str):
        self.description = description
    def setContent(self, content: list):
        self.content = content
    
class TaskManager:
    data : list

    def __init__(self):
        self.data = []

    def __init__(self, data: list):
        self.data = data

    def getNamesArrByPath(self, path: list):
        names_arr : list = []
        ptr : list = self.data
        for name in path:
            for content_iter, content in enumerate(ptr):
                if name == content["name"]:
                    ptr = content["content"]
                    break
                if content_iter == len(ptr) - 1:
                    return []
                
        for content in ptr:
            names_arr.append(content['name'])

        return names_arr
'''