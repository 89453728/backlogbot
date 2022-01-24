def message_handler (message_text):
        assert(type(message_text)==str)
        r = message_text.split('\n')
        k = []
        if(len(r) != 2):
                return False
        
        k.append(''.join((r[0].split(':')[1]).split(' ')))
        k.append(r[1].split(':')[1])
        return k

