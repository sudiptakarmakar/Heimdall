from config.local import Config as LocalConfig
from config.dev import Config as DevConfig
from config.prod import Config as ProdConfig


class Config:
    local = LocalConfig
    dev = DevConfig
    prod = ProdConfig
