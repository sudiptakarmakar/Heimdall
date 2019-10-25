from config.local import get_local_config
from config.dev import get_dev_config
from config.prod import get_prod_config


class Config:
    local = get_local_config
    dev = get_dev_config
    prod = get_prod_config
