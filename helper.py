import json

name_db = "DbUser.json"

def read_all():
    with open(name_db, "r", encoding='utf-8') as file:
        return json.load(file)


def read(id):
    all_data = read_all()
    for i in all_data:
        if i["id"] == id:
            return i
        else:
            return False

def create(id, name, duration, time_start, time_finish):
    data = read_all()
    data.append({"id" : id, "name" : name, "duration": duration, "time_start": time_start, "time_finish": time_finish})
    with open(name_db, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        return "succses"

def update(id, propertys, velue):
    data = read_all()
    for i in data:
        if i["id"] == id:
            for p in propertys:
                data[p] = velue
                with open(name_db, "w", encoding="utf-8") as file:
                     json.dump(data, file, indent=4, ensure_ascii=False)
                     return "succses"
        else:
            return False

def delete(id):
    data = read_all()
    for i in data:
        if i["id"] == id:
            data.remove(i)
            with open(name_db, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                return "succses"
        else:
            return False