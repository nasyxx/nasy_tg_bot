#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""
心之憂矣於我歸處 Python ♡ Nasy

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
import xml.etree.ElementTree as ET

# DataBase
import shelve

# Telegram
from pyrogram import Client

# Others
from httpx import get
from loguru import logger

# Config
from config import rss, user
from typ import Bot

TO = "-1001385481497"
V_RE = re.compile(r'<video.*?src="(.*?)"')
P_RE = re.compile(r'<img.*?src="(.*?)"')


def _logs(typ: str, text: str) -> None:
    """Log arknight rss bot `str`."""
    logger.info(f"Arknight RSS\tsend {typ} to {TO}")
    logger.info(f"Arknight RSS\t{text}")


def _send(text: str) -> None:
    """Send text to `TO`."""
    with Client("ArknightRSS", api_id=user.id, api_hash=user.hash) as bot:
        bot.send_message(
            TO, text, parse_mode="html", disable_notification=True
        )
        _logs("text", text)
        for vurl in V_RE.findall(text):
            try:
                _logs("video", vurl)
                bot.send_video(TO, vurl, disable_natification=True)
            except BaseException:
                logger.error(e)
                logger.error(f"Arknight RSS\t{vurl}")
        for purl in P_RE.findall(text):
            try:
                _logs("picture", purl)
                bot.send_message(TO, purl, disable_notification=True)
            except BaseException as e:
                logger.error(e)
                logger.error(f"Arknight RSS\t{purl}")


def run() -> None:
    """Run arknight rss bot."""
    logger.info("Arknight RSS\trun:")
    etree = ET.fromstring(get(rss.host + rss.w_ark).text)

    lbd = etree.find(".//item/pubDate")
    link = etree.find(".//item/link")
    desc = etree.find(".//item/description")

    logger.debug(lbd.text)
    logger.debug(link.text)
    logger.debug(desc.text)
    with shelve.open("arkrss", writeback=True) as db:
        ts = db.get("timestamp", {"timestamp"})
        logger.debug(ts)
        if all(
            map(lambda et: isinstance(et, ET.Element), (lbd, link, desc))
        ) and (link.text in ts or lbd.text in ts):
            ts.add(link.text)
            ts.add(lbd.text)
            db["timestamp"] = ts
            db.sync()
            try:
                # _send("\n".join((f"{link}", desc.text.replace("<br>", "\n"))))
                1
            except BaseException as e:
                logger.error(e)
                logger.error(f"Arknight RSS\tsend error\t{(link,lbd,desc)}")

        ts.add(link.text)
        ts.add(lbd.text)
        db["timestamp"] = ts
        db.sync()
        logger.info("Arknight RSS\tend.")

ark_bot = Bot(run)
