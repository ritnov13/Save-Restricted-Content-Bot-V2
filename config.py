# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21058641"))
API_HASH = getenv("API_HASH", "7b40956ba81901f2ffe02350f500a144")
BOT_TOKEN = getenv("BOT_TOKEN", "7838660297:AAE4tB6RJn101sPkACQRxo46b7FDaL9Z4XY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7843043976").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1002413119767")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002413119767"))
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "BQFBVFEAiurI19WiH_B2qrbACe844BuNHWJQ9ezHyhC7TZ1GYpeNTWWzEeIppTq3EhwmiAAv_iuw1aRZyUjf99YfADF40v7EAvTUC_-wLHQNLhPrPq-jm6rK2tPpeFJsWMXNOVHUVH8IEPZKw6MBcJEtryG-X4sfzamdrZSFiqlLRxuFqpbwpRGC_Nr_KH4S51O8MqtsatImIs--ZM63IjdAVtky178nfFGTGRkTs8qKwpqAGtcFwWcct7gArY5S6ERPXDG99LXTivHoCJ08tMdxmEMfwtJcfak21Ovq2F0QSsKf_na5pi9nOXGVg0U9XIst4-IN_oTv3cRgqecpUVvQ9oTqQQAAAAHTe1qIAA")
