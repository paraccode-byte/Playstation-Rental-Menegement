import data.var
import helper.helper
import helper.CRUD.handler
import helper.user_monitoring.handler
import helper.financial_report.handler
def main():
    try:
        helper.helper.clear_screen()
        print(data.var.header)
    
        main_choice = helper.helper.to_int(input(data.var.main_list()))
        if main_choice == 1:
            helper.CRUD.handler.handler_CRUD()
        elif main_choice == 2:
            helper.user_monitoring.handler.user_monitoring()
        elif main_choice == 3:
            helper.financial_report.handler.financial_report()
        elif not main_choice:
            return print('Please enter a number')
        else:
            return print('Invalid input')
        
        
    except Exception as err:
        print(err)
    
main()