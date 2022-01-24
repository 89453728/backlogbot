# Telegram Bots template
from telegram.ext import (Updater,CommandHandler,MessageHandler,Filters)
from models.msg_handler import (message_handler)
from models.database import (put_in_table, rem_from_table, get_cols_by_col)
import urllib

DB = "backlog.db"
TABLE_NAME = "backlog"


# logs command
def logs(update,ctx):
        chat_id = update.message.chat_id
        logs = get_cols_by_col(DB,TABLE_NAME,["title"],"chat_id = "+str(chat_id),"order by title asc")
        if logs==False: 
                ctx.bot.send_message(chat_id,"<b> Todavia no hay logs</b>",parse_mode="HTML")
        else:   
                r = "<b>Logs existentes: </b>\n\n"
                for i in logs:
                        r += "* " + i[0] + "\n"
                ctx.bot.send_message(chat_id,r,parse_mode="HTML")

# read command
def read(update,ctx):
        chat_id = update.message.chat_id
        title = update.message.text.split(' ')
        if len(title)!=2:
                ctx.bot.send_message(chat_id,"El titulo no es valido, no debe tener espacios")
        else :
                title = title[1]
                r = get_cols_by_col(DB,TABLE_NAME,['description'],"title = '" + title + "' AND chat_id = "  + str(chat_id))
                if r == False:
                        ctx.bot.send_message(chat_id,"<b>No se ha encontrado ningun log</b>",parse_mode="HTML")
                elif len(r) == 1:
                        ctx.bot.send_message(chat_id,"<b>" + title + "</b>\n\n"+r[0][0],parse_mode="HTML")
                else:
                        for i in range(0,len(r)):
                                ctx.bot.send_message(chat_id,"<b>" + title + "(" + str(i) + ")</b>\n\n"+ r[i][0],parse_mode="HTML")
                                

# rm command
def rm(update,ctx):
        chat_id = update.message.chat_id
        title = update.message.text.split(' ')
        if len(title)!=2:
                ctx.bot.send_message(chat_id,"El titulo no es valido, no debe tener espacios")
        else :
                title = title[1]
                rem_from_table(DB,TABLE_NAME,"title = '"+title+"' AND chat_id = " + str(chat_id))

# help command
def help(update,ctx):
        ctx.bot.send_message( update.message.chat_id,("""<b>Comandos de backlog</b>\n<b>* help: </b>muestra este mensage\n<b>* hello: </b>te manda un saludo\n<b>* logs: </b>puedes ver todos los logs guardados\n<b>* rm 'log_name':</b> sirve para eliminar un log existente\n<b>* read 'titulo': </b>leer la descripcion de los logs con ese titulo\n\n<b>nota:</b> para añadir un log basta con enviar un mensaje con dos lineas, la primera con la palabra titulo seguido de : y luego el titulo que quieres darle, en la siguiente linea pones la descripcion (ojo! todo en una sola linea o el bot no lo detectara, no escribas saltos de linea (maximo 4096 caracteres el mensaje entero)"""),
                parse_mode="HTML")

# hello command
def hello(update,ctx):
        ctx.bot.send_message(update.message.chat_id,"Hi")
# message handler
def msg(update, ctx):
        r = message_handler(update.message.text)
        print(r)
        if r:
                put_in_table(DB,TABLE_NAME,['chat_id', 'title','description'],[update.message.chat_id,r[0],r[1]])
                ctx.bot.send_message(update.message.chat_id,"<b> Log registrado con el nombre: " + r[0] + " </b>",parse_mode="HTML")
def main():
        # get token
        try:
                f = open("tok",'r')
        except Exception as ex:
                print("error opening tok file: ",ex)
                exit(-1)
        token = f.readline()
        token = token[0:len(token)-1]
        f.close()
        
        # make the bot run
        updater = Updater(token,use_context = True)
        bot = updater.dispatcher
        bot.add_handler(CommandHandler('hello',hello))
        bot.add_handler(CommandHandler('logs',logs))
        bot.add_handler(CommandHandler('help',help))
        bot.add_handler(CommandHandler('read',read))
        bot.add_handler(CommandHandler('rm',rm))
        bot.add_handler(MessageHandler(Filters.text,callback=msg))
        updater.start_polling()
        updater.idle()

if __name__ == "__main__":
        main()
