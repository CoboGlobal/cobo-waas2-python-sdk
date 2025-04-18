# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class StakingPoolId(str, Enum):
    """
    The ID of the staking pool. A staking pool is a pairing of a staking protocol and a specific type of token. Currently, `berachain_bgt` and `berachain_bgt_testnet` are not supported.
    """

    """
    allowed enum values
    """
    BABYLON_BTC_SIGNET = 'babylon_btc_signet'
    BABYLON_BTC = 'babylon_btc'
    BEACON_ETH = 'beacon_eth'
    BEACON_ETH_HOLESKY = 'beacon_eth_holesky'
    CORE_BTC = 'core_btc'
    CORE_XTN = 'core_xtn'
    SKY_FARM_ETH_USDC = 'sky_farm_eth_usdc'
    BITHIVE_SIGNET = 'bithive_signet'
    BITHIVE = 'bithive'
    BEACON_BERA = 'beacon_bera'
    BEACON_BERA_TESTNET = 'beacon_bera_testnet'
    BERACHAIN_BGT = 'berachain_bgt'
    BERACHAIN_BGT_TESTNET = 'berachain_bgt_testnet'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StakingPoolId from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


