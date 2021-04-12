from dataclasses import dataclass
from typing import Dict, List, Tuple

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


def to_rgb(hex: str) -> Tuple[int, int, int]:
    color_hex = hex.lstrip('#')
    return tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))


@dataclass
class Config:
    check_interval: int
    aad: AzureAd
    application: AzureApplication
    graph: GraphPermission
    activity_map: Dict[str, str]


def load_config(config_file: str = 'config.json') -> Config:
    config: Config
    with open(config_file, 'r') as cfg:
        config = jsons.loads(cfg.read(), Config)

    return config
