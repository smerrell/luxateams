from dataclasses import dataclass
from typing import List

import jsons


@dataclass
class AzureAd:
    authority: str


@dataclass
class AzureApplication:
    id: str
    tenant: str


@dataclass
class GraphPermission:
    scopes: List[str]


@dataclass
class Config:
    check_interval: int
    aad: AzureAd
    application: AzureApplication
    graph: GraphPermission


def load_config(config_file: str = 'config.json') -> Config:
    config: Config
    with open(config_file, 'r') as cfg:
        config = jsons.loads(cfg.read(), Config)

    return config
