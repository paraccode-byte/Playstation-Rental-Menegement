import json

name_db = "./data/DbUser.json"

def read_all():
    with open(name_db, "r", encoding="utf-8") as file:
        return json.load(file)


def read(id):
    data = read_all()

    for i in data:
        if i["id"] == id:
            return i
    return False


def create(id, name, duration, time_start, time_finish):
    data = read_all()

    data.append(
        {
            "id": id,
            "name": name,
            "duration": duration,
            "time_start": time_start,
            "time_finish": time_finish,
        }
    )

    with open(name_db, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return "success"


def update(id, properties):
    data = read_all()

    for i in data:
        if i["id"] == id:
            i.update(properties)

            with open(name_db, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            return "success"

    return False


def delete(id):
    data = read_all()

    for i in data:
        if i["id"] == id:
            data.remove(i)

            with open(name_db, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            return "success"

    return False

def crud_list():
    with open('./data/CRUD_list.txt', 'r', encoding='utf-8') as file:
        return file.read()

def update_prop_list():
    with open('./data/prop.update.txt', 'r', encoding='utf-8') as file:
        return file.read()


