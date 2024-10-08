# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2 import Configuration
from cobo_waas2.api.wallets_exchange_wallet_api import WalletsExchangeWalletApi


class TestWalletsExchangeWalletApi(unittest.TestCase):
    """WalletsExchangeWalletApi unit test stubs"""

    def setUp(self) -> None:
        Configuration.set_default(Configuration(
            api_private_key="c203fccc02a2269ec486d9c32ff74b5ba6ab0cdb461ee1fb0dfc616109115c06",
            host="https://api.sandbox.cobo.com/v2"
        ))
        self.api = WalletsExchangeWalletApi()

    def tearDown(self) -> None:
        pass

    def test_list_asset_balances_for_exchange_wallet(self) -> None:
        """
        Test case for list_asset_balances_for_exchange_wallet

        List asset balances
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        trading_account_types = 'Trading,Funding'
        asset_ids = 'USDT,USDC'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_asset_balances_for_exchange_wallet(wallet_id, trading_account_types=trading_account_types, asset_ids=asset_ids, limit=limit, before=before, after=after)
        """

    def test_list_exchanges(self) -> None:
        """
        Test case for list_exchanges

        List supported exchanges
        """
        """

        api_response = self.api.list_exchanges()
        """

    def test_list_supported_assets_for_exchange(self) -> None:
        """
        Test case for list_supported_assets_for_exchange

        List supported assets
        """
        """
        exchange_id = cobo_waas2.ExchangeId()
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_supported_assets_for_exchange(exchange_id, limit=limit, before=before, after=after)
        """

    def test_list_supported_chains_for_exchange(self) -> None:
        """
        Test case for list_supported_chains_for_exchange

        List supported chains
        """
        """
        exchange_id = cobo_waas2.ExchangeId()
        asset_id = 'USDT'

        api_response = self.api.list_supported_chains_for_exchange(exchange_id, asset_id)
        """


if __name__ == '__main__':
    unittest.main()
