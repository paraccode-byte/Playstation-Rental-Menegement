from . import func
from datetime import datetime, timedelta
import os
import sys

def handler_CRUD():
    try:
        input_user = int(input(func.crud_list()))
        if input_user == 1:
            table_number = input("INPUT NOMOR MEJA: ")
            name = input('INPUT NAMA: ')
            duration = int(input('INPUT DURASI (JAM): '))
            finish = datetime.now() + timedelta(hours=duration)
            edit = func.create(
                    table_number,
                    name,    
                    duration,
                    int(datetime.now().timestamp()),
                    int(finish.timestamp())
                    )
            if edit:
                print("--------- SELESAI ----------")
                print("----- Data berhasil di -----")
                print("-------- TAMBAHKAN ---------") 
                
        elif input_user == 2:
            table_number = input("INPUT NOMOR MEJA: ")
            properti = int(input(func.update_prop_list()))

            if properti == 1:
                name = input('INPUT NAMA: ')
                edit = func.update(table_number, {"name": name})
            elif properti == 2:
                duration = int(input('INPUT DURASI (JAM): '))
                edit = func.update(table_number, {"duration": duration})
            else:
                return print("Please enter the correct number")

            if edit:
                print("--------- SELESAI ----------")
                print("----- Data berhasil di -----")
                print("-------- PERBAHARUI --------") 

        elif input_user == 3:
            table_number = input("INPUT NOMOR MEJA: ")
            edit = func.delete(table_number)
            if edit:
                print("--------- SELESAI ----------")
                print("----- Data berhasil di -----")
                print("---------- HAPUS -----------") 

        elif input_user == 4:
            print("Return to the main menu...")
            os.execv(sys.executable, ['python'] + sys.argv)

        else:
            print("Invalid Input!")
            handler_CRUD()

    except Exception as err:
        print(err)