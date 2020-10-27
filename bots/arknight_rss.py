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
date     : Oct 14, 2020
email    : Nasy <nasyxx+python@gmail.com>
filename : arknigth_rss.py
project  : bots
license  : GPL-3.0+

Arknigth weibo to Telegram bot.
"""
# Standard Library
import re
from asyncio import gather

# DataBase
import shelve

# Telegram
from pyrogram import Client

# Others
from defusedxml.ElementTree import fromstring
from httpx import get
from loguru import logger

# Config
from config import TLG, rss, user

# Types
from typ import Bot

TO = -1001385481497
V_RE = re.compile(r'<video.*?src="(.*?)"')
P_RE = re.compile(r'<img.*?src="(.*?)"')
TS = "timestamp"

_BOT = Client("ArknightRSS", api_id=user.id, api_hash=user.hash)


def _logs(typ: str, text: str) -> None:
    """Log arknight rss bot `str`."""
    logger.info(f"Arknight RSS\tsend {typ} to {TO}")
    logger.info(f"Arknight RSS\t{text}")


async def _send(text: str, to: int = TO) -> None:
    """Send text to `TO`."""
    async with _BOT as bot:
        await bot.send_message(
            to,
            text,
            parse_mode="html",
            disable_web_page_preview=True,
            disable_notification=True,
        )
        _logs("text", text)
        for vurl in V_RE.findall(text):
            _logs("video", vurl)
            try:
                await bot.send_video(to, vurl, disable_notification=True)
            except BaseException as e:
                await bot.send_message(to, vurl, disable_notification=True)
                logger.error(e)
                logger.error(f"Arknight RSS\t{vurl}")
        for purl in P_RE.findall(text):
            _logs("picture", purl)
            try:
                await bot.send_message(to, purl, disable_notification=True)
            except BaseException as e:
                logger.error(e)
                logger.error(f"Arknight RSS\t{purl}")


async def run() -> None:
    """Run arknight rss bot."""
    logger.info("Arknight RSS\trun:")
    etree = fromstring(get(rss.host + rss.w_ark).text)

    lbd = etree.find(".//item/pubDate")
    link = etree.find(".//item/link")
    desc = etree.find(".//item/description")

    with shelve.open("arkrss", writeback=True) as db:
        ts = db.get(TS, {TS})
        if all(map(lambda et: et is not None, (lbd, link, desc))) and (
            link.text not in ts and lbd.text not in ts
        ):
            ts.add(link.text)
            ts.add(lbd.text)
            db[TS] = ts
            db.sync()
            logger.info("run _send")
            try:
                await _send(
                    "\n".join(
                        (f"#微博: {link.text}", desc.text.replace("<br>", "\n"))
                    ),
                    TO,
                )
            except BaseException as e:
                logger.error(e)
                logger.error(
                    f"Arknight RSS\tsend error\t{(TO, link, lbd, desc)}"
                )
            try:
                await _send(
                    "\n".join(
                        (f"#微博: {link.text}", desc.text.replace("<br>", "\n"))
                    ),
                    TLG,
                )
            except BaseException as e:
                logger.error(e)
                logger.error(
                    f"Arknight RSS\tsend error\t{(TLG, link, lbd, desc)}"
                )

        ts.add(link.text)
        ts.add(lbd.text)
        db[TS] = ts
        db.sync()
        logger.info("Arknight RSS\tend.")


ark_bot = Bot(run)
