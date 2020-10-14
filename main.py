#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""
心之憂矣於我歸處 Python ♡ Nasy.

    |             *         *
    |                  .                .
    |           .                          舒而脫脫兮
    |     *                      ,
    |                   .                  無感我帨兮
    |
    |                               *      無使尨也吠
    |          |\___/|
    |          )    -(             .              ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Oct 12, 2020
email    : Nasy <nasyxx+python@gmail.com>
filename : main.py
project  : nasy_tg_bot
license  : GPL-3.0+

Nasy Telegram User Bots.

"""
# Standard Library
import asyncio
import sys

# Others
from aiocron import crontab
from bots import bots
from loguru import logger

logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time}</green> <level>{message}</level>",
)


@crontab("*/1 * * * *")
async def run_async() -> None:
    """Run all async bots."""
    for bot in bots.a_bots:
        bot.run()


if __name__ == "__main__":
    asyncio.get_event_loop().run_forever()
