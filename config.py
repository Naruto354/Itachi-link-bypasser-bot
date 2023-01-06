import os


class Config(object):
    bot_token = os.environ.get("TOKEN", "")
    api_hash = os.environ.get("HASH", "") 
    api_id = os.environ.get("ID", "")
    GDTot_Crypt = os.environ.get("CRYPT","b0lDek5LSCt6ZjVRR2EwZnY4T1EvVndqeDRtbCtTWmMwcGNuKy8wYWpDaz0%3D")
    Laravel_Session = os.environ.get("Laravel_Session","")
    XSRF_TOKEN = os.environ.get("XSRF_TOKEN","")
    DCRYPT = os.environ.get("DRIVEFIRE_CRYPT","")
    KCRYPT = os.environ.get("KOLOP_CRYPT","aWFicnVaNWh4TThRbzFqdkE2U2FKNmJOTWhvWkZmbWswaUFadTB5NXJ3RT0%3D")
    HCRYPT = os.environ.get("HUBDRIVE_CRYPT","Q29hdlpLUEZTSEJLUjVZRkZQSExLODFuWGVudUlNK0ZPZlZmS1hENWxZVT0%3D")
    KATCRYPT = os.environ.get("KATDRIVE_CRYPT","")
