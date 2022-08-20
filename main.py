import os
from config import api_id, api_hash, bot_token
import converter
import pyrogram
from pyrogram import Client, filters

app = Client("hand bot",
	bot_token = bot_token,  
	api_id = api_id,
	api_hash = api_hash)
@app.on_message(filters.command(["start", "help"]))
def start_command(bot, message):
	text  = f"""
	Hi, {message.from_user.first_name}
	Just send me a text and get the handwritten 
	version of the text in image format
	"""
	message.reply_text(text)
	message.reply_video("./Telegram")
@app.on_message(filters.text)
def image_converter(bot, message):
	process = message.reply_text("please wait ...")
	filename = f"{message.chat.id}.jpg"	
	text = str(message.text)
	chat_id = message.chat.id
	try :
		process.edit("converting...")
		photo = converter.text_to_handwriting(text, filename)
		process.edit("uploading...")
		bot.send_photo(
			chat_id = chat_id,
			photo = photo)
	except:
		message.reply_text("sorry, unable to convert the text")
	process.edit("uploaded")
if __name__ == "__main__":
	app.run()
