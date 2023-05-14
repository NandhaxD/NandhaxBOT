from Katsuki import bot, MODULE, INFO as GET_INFO


@bot.on_callback_queey(filters.regex('^help'))
async def help_commnds(_, query):
   user_id = (await GET_INFO.app()).id
   if not query.from_user.id == int(user_id):
       return await query.answer("😤 You aren't my master")
   CB_NAME = query.data.split(':')[1].casefold()
   data = [x for x in MODULE if x['module'].casefold() == CB_NAME]
   if len(data) == 0:
       return await query.answer("🤔 somthing wrong.")
   module = data[0]['module']
   help = data[0]['help']
   return await query.message.edit(strings.HELP_CMD.format(module=module, help=help))
       
            
            

   
