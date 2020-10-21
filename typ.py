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
filename : typ.py
project  : nasy_tg_bot
license  : GPL-3.0+

Nasy Telegram bots typing.
"""
# Types
from typing import Callable, Coroutine, NamedTuple, Tuple

User = NamedTuple("User", [("id", str), ("hash", str)])
RSSH = NamedTuple("RSSH", [("host", str), ("w_ark", str)])

Bot = NamedTuple("ABot", [("run", Callable[[], Coroutine[None, None, None]])])
Bots = NamedTuple(
    "Bots", [("a_bots", Tuple[Bot, ...]), ("bots", Tuple[Bot, ...])]
)
