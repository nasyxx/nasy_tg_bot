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
filename : __init__.py
project  : bots
license  : GPL-3.0+

Nasy Telegram bots
"""
# Types
from typ import Bots

# Local
from .arknight_rss import ark_bot

bots = Bots((ark_bot,), tuple())
