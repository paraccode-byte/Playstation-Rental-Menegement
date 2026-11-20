header = "==================== PLAYSTASTION RENTAL MENEGEMENT ======================="

def main_list():
    with open('./data/main_list.txt', 'r', encoding='utf-8') as file:
        return file.read()

