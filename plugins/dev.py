"""Evaluate Python Code inside Telegram
Syntax: .eval PythonCode"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import io
import sys
import traceback
from pyrogram import filters
from info import COMMAND_HANDLER
from bot import app

@app.on_message(filters.command(["run","run@MissKatyRoBot"], COMMAND_HANDLER) & filters.user(617426792))
async def eval(client, message):
    if len(message.command) < 2 :
        return await message.reply("Masukkan kode yang ingin dijalankan..")
    status_message = await message.reply_text("Sedang Memproses ...")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "<b>EVAL</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>OUTPUT</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n"

    if len(final_output) > 3000:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd,
                disable_notification=True
            )
    else:
        await reply_to_.reply_text(final_output)
        await status_message.delete()

async def aexec(code, client, message):
    exec(
        'async def __aexec(client, message): ' +
        ''.join(f'\n {l_}' for l_ in code.split('\n'))
    )
    return await locals()['__aexec'](client, message)
