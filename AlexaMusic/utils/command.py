# A Powerful Music Bot Property Of Alone Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Alone © @ALONE_WAS_BOT © Alone
# Owner Alone
# Alone


from typing import Union, List
from pyrogram import filters

other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)


def commandpro(commands: Union[str, List[str]]):
    return filters.command(commands, "")
