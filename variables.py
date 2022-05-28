import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

STAT_STICK = os.environ.get("STAT_STICK", "CAACAgIAAxkBAAIDwmKSV0bNuMDglK8nzEsWxyoYctK1AAKtDQACrJkgSN2Kd_L9h_lwHgQ")

PICS = os.environ.get("PICS", "https://telegra.ph/file/448878f9a10e0143a157d.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '1467649219').split()]

DB_URL = os.environ.get("mongodb+srv://Huzain:Huzain@cluster0.jfppkde.mongodb.net/?retryWrites=true&w=majority", "")

DELAY = int(os.environ.get("DELAY", "1"))
