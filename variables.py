import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

STAT_STICK = os.environ.get("STAT_STICK", "CAACAgIAAxkBAAIDwmKSV0bNuMDglK8nzEsWxyoYctK1AAKtDQACrJkgSN2Kd_L9h_lwHgQ")

PICS = os.environ.get("PICS", "https://telegra.ph/file/448878f9a10e0143a157d.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '900873119').split()]

DB_URL = os.environ.get("DB_URL", "")

DELAY = int(os.environ.get("DELAY", "1"))
