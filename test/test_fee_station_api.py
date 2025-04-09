# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2 import Configuration
from cobo_waas2.api.fee_station_api import FeeStationApi


class TestFeeStationApi(unittest.TestCase):
    """FeeStationApi unit test stubs"""

    def setUp(self) -> None:
        Configuration.set_default(Configuration(
            api_private_key="c203fccc02a2269ec486d9c32ff74b5ba6ab0cdb461ee1fb0dfc616109115c06",
            host="https://api.sandbox.cobo.com/v2"
        ))
        self.api = FeeStationApi()

    def tearDown(self) -> None:
        pass

    def test_get_fee_station_transaction_by_id(self) -> None:
        """
        Test case for get_fee_station_transaction_by_id

        Get Fee Station transaction information
        """
        """
        transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

        api_response = self.api.get_fee_station_transaction_by_id(transaction_id)
        """

    def test_list_fee_station_addresses(self) -> None:
        """
        Test case for list_fee_station_addresses

        List Fee Station addresses
        """
        """
        chain_ids = 'BTC,ETH'
        addresses = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045,0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_fee_station_addresses(chain_ids=chain_ids, addresses=addresses, limit=limit, before=before, after=after)
        """

    def test_list_fee_station_transactions(self) -> None:
        """
        Test case for list_fee_station_transactions

        List all Fee Station transactions
        """
        """
        request_id = 'web_send_by_user_327_1610444045047'
        cobo_ids = '20231213122855000000000000000000,20231213122955000000000000000000'
        transaction_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,557918d2-632a-4fe1-932f-315711f05fe3'
        transaction_hashes = '239861be9a4afe080c359b7fe4a1d035945ec46256b1a0f44d1267c71de8ec28'
        types = 'Deposit,Withdrawal'
        statuses = 'Completed,Failed'
        chain_ids = 'BTC,ETH'
        token_ids = 'ETH_USDT,ETH_USDC'
        asset_ids = 'USDT,USDC'
        min_created_timestamp = 1635744000000
        max_created_timestamp = 1635744000000
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
        direction = ''

        api_response = self.api.list_fee_station_transactions(request_id=request_id, cobo_ids=cobo_ids, transaction_ids=transaction_ids, transaction_hashes=transaction_hashes, types=types, statuses=statuses, chain_ids=chain_ids, token_ids=token_ids, asset_ids=asset_ids, min_created_timestamp=min_created_timestamp, max_created_timestamp=max_created_timestamp, limit=limit, before=before, after=after, direction=direction)
        """

    def test_list_token_balances_for_fee_station(self) -> None:
        """
        Test case for list_token_balances_for_fee_station

        List Fee Station token balances
        """
        """
        token_ids = 'ETH_USDT,ETH_USDC'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_token_balances_for_fee_station(token_ids=token_ids, limit=limit, before=before, after=after)
        """


if __name__ == '__main__':
    unittest.main()
