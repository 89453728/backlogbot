import models.database as db

def message_handler (message_text):
        assert(type(message_text)==str)
        messg_format = message_text.split(':')
        if(len(messg_format)!=4):
                return False
        return [''.join(messg_format[1].split(' ')),messg_format[3]]

