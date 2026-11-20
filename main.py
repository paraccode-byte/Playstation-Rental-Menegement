import data.var
import helper.helper
import helper.CRUD.handler
def main():
    try:
        # helper.helper.clear_screen()
        print(data.var.header)
    
        main_choice = helper.helper.to_int(input(data.var.main_list()))
        if main_choice == 1:
            helper.CRUD.handler.handler_CRUD()
        elif main_choice == 2:
            ""
        elif main_choice == 3:
            ""
        elif not main_choice:
            return print('Please enter a number')
        else:
            return print('Invalid input')
        
        
    except Exception as err:
        print(err)
    
main()