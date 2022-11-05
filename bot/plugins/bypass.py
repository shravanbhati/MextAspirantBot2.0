import re
from bot.helper.http import http
from bot import app
from info import COMMAND_HANDLER
from bot.helper.tools import rentry
from urllib.parse import unquote
from bot.helper.human_read import get_readable_file_size

def pling(url):
    try:
        id_url = re.search(r"https?://(store.kde.org|www.pling.com)\/p\/(\d+)", url)[2]
        link = f"https://www.pling.com/p/{id_url}/loadFiles"
        res = await http.get(link)
        json_dic_files = res.json().pop("files")
        if len(json_dic_files) < 8:
            return "\n".join(f'→ <a href="{unquote(i["url"])}">{i["name"]} ({get_readable_file_size(int(i["size"]))})</a>' for i in json_dic_files)
        else:
            msg = f"\n**Source Link** :\n`{url}`\n**Direct Link :**\n"
            msg += "\n".join(f'**→ [{i["name"]}]({unquote(i["url"])}) ({get_readable_file_size(int(i["size"]))})**' for i in json_dic_files)
            return msg
    except Exception as e:
        return e
      
__MODULE__ = "Bypass"
__HELP__ = """
/directurl [Link] - Bypass URL.

Supported Link:
- Pling and all aliases.
- Soon..
"""

@app.on_message(filters.command(["directurl"], COMMAND_HANDLER))
async def bypass(_, message):
  if len(message.command) == 1:
    return await message.reply(f"Gunakan perintah /{message.command[0]} untuk bypass url")
  url = message.command[1]
  mention = f"{message.from_user.mention} ({message.from_user.id})"
  if re.match(r"https?://(store.kde.org|www.pling.com)\/p\/(\d+)", url):
     pling = pling(url)
     if len(pling) > 3800:
        result = rentry(data)
        await message.reply(result)
     else:
        await message.reply(pling)
  else:
     await message.reply("Unsupported link..")
    
