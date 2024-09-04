data = {
   "/path1/": {
        "name":"string1",
        "description": "string1"
    },
    "/path1/path2/": {
        "name":"string2",
        "description": "string1"
    },
    "/path1/path2/path3/":{
        "name":"string3",
        "description": "string1"
    }
}

a = {
    'time1': {
        '1235':'гавно',
        '1234':'гавно',
        '1232':'гавно',
        '1236':'гавно',
        '1238':'гавно'
    },
    'time2': {
        '1235':'гавно',
        '1234':'гавно',
        '1232':'гавно',
        '1236':'гавно',
        '1238':'гавно'
    },
    'time3': {
        '1235':'гавно',
        '1234':'гавно',
        '1232':'гавно',
        '1236':'гавно',
        '1238':'гавно'
    }
}

id = '1236'

result = {}

for time in a:
    if id in a[time]:
        result.update({
            time: a[time][id]
        })

print(result)
