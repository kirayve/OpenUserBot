
from telethon import events
from datetime import datetime
import importlib.util
import asyncio
import random
import importlib.util
from datetime import datetime
from random import randint
from asyncio import sleep
from os import execl
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which, rmtree
from telethon import version
from os import remove, execle, path, makedirs, getenv, environ
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
import distutils
from userbot import CMD_HELP, LOGS, HEROKU_APP_NAME, HEROKU_API_KEY, bot, UPSTREAM_REPO_URL
from collections import deque
import sys
import os
import io
import git
import heroku3
import json
import subprocess
from datetime import datetime
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import heroku3
import asyncio
import sys
import json
from speedtest import Speedtest
from telethon import functions
from os import remove, execle, path, makedirs, getenv, environ
from shutil import rmtree
import asyncio
import json
from asyncio import sleep
from telethon.errors import rpcbaseerrors
import os
import subprocess
import time
import math
from pySmartDL import SmartDL
import asyncio
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
import sys
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def asyncrunapp_run(cmd, heroku):
    subproc = await asyncrunapp(cmd, stdout=asyncPIPE, stderr=asyncPIPE)
    stdout, stderr = await subproc.communicate()
    exitCode = subproc.returncode
    if exitCode != 0:
        await heroku.edit(
            '**An error was detected while running subprocess**\n'
            f'```exitCode: {exitCode}\n'
            f'stdout: {stdout.decode().strip()}\n'
            f'stderr: {stderr.decode().strip()}```')
        return exitCode
    return stdout.decode().strip(), stderr.decode().strip(), exitCode

  

#@borg.on(admin_cmd(pattern="heroku ?(.*)"))
#async def _event(heroku):
#@register(outgoing=True, pattern=r"^!heroku(?: |$)(.*)")
@register(outgoing=True, pattern="^.heroku$")
async def heroku_manager(manager):
    await manager.edit("`Processing...`")
    await asyncio.sleep(3)
    conf = manager.pattern_match.group(1)
    result = await asyncrunapp_run(f'heroku ps -a {HEROKU_APP_NAME}', manager)
    if result[2] != 0:
        return
    hours_remaining = result[0]
    await manager.edit('`' + hours_remaining + '`')
    return


@register(outgoing=True, pattern="^.sysd$")
async def sysdetails(sysd):
    """ For .sysd command, get system info using neofetch. """
    try:
        neo = "neofetch --stdout"
        fetch = await asyncrunapp(
            neo,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        await sysd.edit("`" + result + "`")
    except FileNotFoundError:
        await sysd.edit("`Install neofetch first !!`")

        

@register(outgoing=True, pattern="^.pip(?: |$)(.*)")
async def pipcheck(pip):
    """ For .pip command, do a pip search. """
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.edit("`Searching . . .`")
        invokepip = f"pip3 search {pipmodule}"
        pipc = await asyncrunapp(
            invokepip,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.edit("`Output too large, sending as file`")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
                remove("output.txt")
                return
            await pip.edit("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`"
                           f"{pipout}"
                           "`")
        else:
            await pip.edit("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`No Result Returned/False`")
    else:
        await pip.edit("`Use .help pip to see an example`")
