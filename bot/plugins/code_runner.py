from pyrogram import Client, filters, enums
import aiohttp
from info import COMMAND_HANDLER


async def listcode():
    async with aiohttp.ClientSession() as session:
        r = await session.get("https://glot.io/api/run")
        return await r.json()


async def glot(lang, langcode, code):
    async with aiohttp.ClientSession() as session:
        data = {"files": [{"name": f"Yasir.{langcode}", "content": code}]}
        headers = {"content-type": "application/json", "Authorization": "Token b8a2b75a-a078-4089-869c-e53d448b1ebb"}
        r = await session.post(f"https://glot.io/api/run/{lang}/latest", headers=headers, json=data)
        return await r.json()


@Client.on_message(filters.command(["codelist", "codelist@MissKatyRoBot"], COMMAND_HANDLER))
async def list_lang(client, message):
    daftarlang = await listcode()
    list_ = "".join(f"~> {i['name']}\n" for i in daftarlang)
    return await message.reply(f"<b>Daftar Bahasa Pemrograman Yang Didukung:</b>\n{list_}")


@Client.on_message(filters.command(["assembly"], "!"))
@Client.on_edited_message(filters.command(["assembly"], "!"))
async def assembly(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "asm", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["ats"], "!"))
@Client.on_edited_message(filters.command(["ats"], "!"))
async def ats(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "dats", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["bash"], "!"))
@Client.on_edited_message(filters.command(["bash"], "!"))
async def bash(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "sh", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["c"], "!"))
@Client.on_edited_message(filters.command(["c"], "!"))
async def c(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "c", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["clojure"], "!"))
@Client.on_edited_message(filters.command(["clojure"], "!"))
async def clojure(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "clj", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["cobol"], "!"))
@Client.on_edited_message(filters.command(["cobol"], "!"))
async def cobol(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "cob", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["coffeescript"], "!"))
@Client.on_edited_message(filters.command(["coffeescript"], "!"))
async def coffeescript(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "coffee", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["cpp"], "!"))
@Client.on_edited_message(filters.command(["cpp"], "!"))
async def cpp(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "cpp", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["crystal"], "!"))
@Client.on_edited_message(filters.command(["crystal"], "!"))
async def crystal(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "cr", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["csharp"], "!"))
@Client.on_edited_message(filters.command(["csharp"], "!"))
async def csharp(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "cs", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["d"], "!"))
@Client.on_edited_message(filters.command(["d"], "!"))
async def d(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "d", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["elixir"], "!"))
@Client.on_edited_message(filters.command(["elixir"], "!"))
async def elixir(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "ex", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["elm"], "!"))
@Client.on_edited_message(filters.command(["elm"], "!"))
async def elm(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "elm", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["erlang"], "!"))
@Client.on_edited_message(filters.command(["erlang"], "!"))
async def erlang(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "erl", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["fsharp"], "!"))
@Client.on_edited_message(filters.command(["fsharp"], "!"))
async def fsharp(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "fs", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["go"], "!"))
@Client.on_edited_message(filters.command(["go"], "!"))
async def go(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "go", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["groovy"], "!"))
@Client.on_edited_message(filters.command(["groovy"], "!"))
async def groovy(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "groovy", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["haskell"], "!"))
@Client.on_edited_message(filters.command(["haskell"], "!"))
async def haskell(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "hs", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["idris"], "!"))
@Client.on_edited_message(filters.command(["idris"], "!"))
async def idris(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "idr", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["java"], "!"))
@Client.on_edited_message(filters.command(["java"], "!"))
async def java(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "java", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["javascript"], "!"))
@Client.on_edited_message(filters.command(["javascript"], "!"))
async def javascript(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "js", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["julia"], "!"))
@Client.on_edited_message(filters.command(["julia"], "!"))
async def julia(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "jl", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["kotlin"], "!"))
@Client.on_edited_message(filters.command(["kotlin"], "!"))
async def kotlin(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "kt", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["lua"], "!"))
@Client.on_edited_message(filters.command(["lua"], "!"))
async def lua(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "lua", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["mercury"], "!"))
@Client.on_edited_message(filters.command(["mercury"], "!"))
async def mercury(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "m", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["nim"], "!"))
@Client.on_edited_message(filters.command(["nim"], "!"))
async def nim(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "nim", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["nix"], "!"))
@Client.on_edited_message(filters.command(["nix"], "!"))
async def nix(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "nix", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["ocaml"], "!"))
@Client.on_edited_message(filters.command(["ocaml"], "!"))
async def ocaml(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "ml", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["perl"], "!"))
@Client.on_edited_message(filters.command(["perl"], "!"))
async def perl(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "pl", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["php"], "!"))
@Client.on_edited_message(filters.command(["php"], "!"))
async def php(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "php", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["python"], "!"))
@Client.on_edited_message(filters.command(["python"], "!"))
async def python(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "py", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["raku"], "!"))
@Client.on_edited_message(filters.command(["raku"], "!"))
async def raku(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "raku", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["ruby"], "!"))
@Client.on_edited_message(filters.command(["ruby"], "!"))
async def ruby(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "rb", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["rust"], "!"))
@Client.on_edited_message(filters.command(["rust"], "!"))
async def rust(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "rs", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["scala"], "!"))
@Client.on_edited_message(filters.command(["scala"], "!"))
async def scala(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "scala", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["swift"], "!"))
@Client.on_edited_message(filters.command(["swift"], "!"))
async def swift(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "swift", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)


@Client.on_message(filters.command(["typescript"], "!"))
@Client.on_edited_message(filters.command(["typescript"], "!"))
async def typescript(client, message):
    if len(message.command) < 2:
        return await message.reply("Silahkan masukkan kode yang ingin dijalankan.")
    try:
        res = await glot(message.command[0], "ts", message.text.split(None, 1)[1])
        hasil = res["stdout"] if res["stdout"] else res["stderr"]
        hasil = f"Hasil :\n{hasil}"
        return await message.reply(hasil, parse_mode=enums.ParseMode.DISABLED)
    except Exception as e:
        return await message.reply(e, parse_mode=enums.ParseMode.DISABLED)
