header = "==================== PLAYSTASTION RENTAL MENEGEMENT ======================="

def main_list():
    with open('./main_list.txt', 'r', encoding='utf-8') as file:
        return file.read()
