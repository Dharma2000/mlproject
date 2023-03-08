import sys

def error_message_etail(error,error_detailes:sys):
    _,_,exc_tb=error_detail.exc_ingo()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_messages="error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
       file_name,exc_tb.tb_lineno,str(error)) 
    return error_message

class customException(Exception):
    def__init__(self,error_message,error_detail:sys)
       super().__init__(error_message)
       self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def__str__(self):
        return self.error_message             