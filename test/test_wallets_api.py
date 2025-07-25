# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2 import Configuration
from cobo_waas2.api.wallets_api import WalletsApi


class TestWalletsApi(unittest.TestCase):
    """WalletsApi unit test stubs"""

    def setUp(self) -> None:
        Configuration.set_default(Configuration(
            api_private_key="c203fccc02a2269ec486d9c32ff74b5ba6ab0cdb461ee1fb0dfc616109115c06",
            host="https://api.sandbox.cobo.com/v2"
        ))
        self.api = WalletsApi()

    def tearDown(self) -> None:
        pass

    def test_batch_check_utxo(self) -> None:
        """
        Test case for batch_check_utxo

        Batch check UTXOs
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        batch_check_utxo_request = cobo_waas2.BatchCheckUtxoRequest()

        api_response = self.api.batch_check_utxo(wallet_id, batch_check_utxo_request=batch_check_utxo_request)
        """

    def test_check_address_chains_validity(self) -> None:
        """
        Test case for check_address_chains_validity

        Check address validity across chains
        """
        """
        address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
        chain_ids = 'BTC,ETH'

        api_response = self.api.check_address_chains_validity(address, chain_ids)
        """

    def test_check_address_validity(self) -> None:
        """
        Test case for check_address_validity

        Check address validity
        """
        """
        chain_id = 'ETH'
        address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'

        api_response = self.api.check_address_validity(chain_id, address)
        """

    def test_check_addresses_validity(self) -> None:
        """
        Test case for check_addresses_validity

        Check addresses validity
        """
        """
        chain_id = 'ETH'
        addresses = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045,0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'

        api_response = self.api.check_addresses_validity(chain_id, addresses)
        """

    def test_create_address(self) -> None:
        """
        Test case for create_address

        Create addresses in wallet
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        create_address_request = cobo_waas2.CreateAddressRequest()

        api_response = self.api.create_address(wallet_id, create_address_request=create_address_request)
        """

    def test_create_token_listing_request(self) -> None:
        """
        Test case for create_token_listing_request

        Create token listing request
        """
        """
        create_token_listing_request_request = cobo_waas2.CreateTokenListingRequestRequest()

        api_response = self.api.create_token_listing_request(create_token_listing_request_request)
        """

    def test_create_wallet(self) -> None:
        """
        Test case for create_wallet

        Create wallet
        """
        """
        create_wallet_params = cobo_waas2.CreateWalletParams()

        api_response = self.api.create_wallet(create_wallet_params=create_wallet_params)
        """

    def test_delete_wallet_by_id(self) -> None:
        """
        Test case for delete_wallet_by_id

        Delete wallet
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

        api_response = self.api.delete_wallet_by_id(wallet_id)
        """

    def test_get_chain_by_id(self) -> None:
        """
        Test case for get_chain_by_id

        Get chain information
        """
        """
        chain_id = 'ETH'

        api_response = self.api.get_chain_by_id(chain_id)
        """

    def test_get_max_transferable_value(self) -> None:
        """
        Test case for get_max_transferable_value

        Get maximum transferable value
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        token_id = 'ETH_USDT'
        fee_rate = '10'
        to_address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE'
        from_address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE'

        api_response = self.api.get_max_transferable_value(wallet_id, token_id, fee_rate, to_address, from_address=from_address)
        """

    def test_get_max_transferable_value_with_fee_model(self) -> None:
        """
        Test case for get_max_transferable_value_with_fee_model

        Estimate maximum transferable value
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        get_max_transferable_value_with_fee_model_request = cobo_waas2.GetMaxTransferableValueWithFeeModelRequest()

        api_response = self.api.get_max_transferable_value_with_fee_model(wallet_id, get_max_transferable_value_with_fee_model_request=get_max_transferable_value_with_fee_model_request)
        """

    def test_get_token_by_id(self) -> None:
        """
        Test case for get_token_by_id

        Get token information
        """
        """
        token_id = 'ETH_USDT'

        api_response = self.api.get_token_by_id(token_id)
        """

    def test_get_token_listing_request_by_request_id(self) -> None:
        """
        Test case for get_token_listing_request_by_request_id

        Get token listing request
        """
        """
        request_id = '123e4567e89b12d3a456426614174000'

        api_response = self.api.get_token_listing_request_by_request_id(request_id)
        """

    def test_get_wallet_by_id(self) -> None:
        """
        Test case for get_wallet_by_id

        Get wallet information
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

        api_response = self.api.get_wallet_by_id(wallet_id)
        """

    def test_list_address_balances_by_token(self) -> None:
        """
        Test case for list_address_balances_by_token

        List address balances by token
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        token_id = 'ETH_USDT'
        addresses = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045,0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_address_balances_by_token(wallet_id, token_id, addresses=addresses, limit=limit, before=before, after=after)
        """

    def test_list_addresses(self) -> None:
        """
        Test case for list_addresses

        List wallet addresses
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        chain_ids = 'BTC,ETH'
        addresses = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045,0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_addresses(wallet_id, chain_ids=chain_ids, addresses=addresses, limit=limit, before=before, after=after)
        """

    def test_list_enabled_chains(self) -> None:
        """
        Test case for list_enabled_chains

        List enabled chains
        """
        """
        wallet_type = cobo_waas2.WalletType()
        wallet_subtype = cobo_waas2.WalletSubtype()
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_enabled_chains(wallet_type=wallet_type, wallet_subtype=wallet_subtype, limit=limit, before=before, after=after)
        """

    def test_list_enabled_tokens(self) -> None:
        """
        Test case for list_enabled_tokens

        List enabled tokens
        """
        """
        wallet_type = cobo_waas2.WalletType()
        wallet_subtype = cobo_waas2.WalletSubtype()
        chain_ids = 'BTC,ETH'
        token_ids = 'ETH_USDT,ETH_USDC'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_enabled_tokens(wallet_type=wallet_type, wallet_subtype=wallet_subtype, chain_ids=chain_ids, token_ids=token_ids, limit=limit, before=before, after=after)
        """

    def test_list_supported_chains(self) -> None:
        """
        Test case for list_supported_chains

        List supported chains
        """
        """
        wallet_type = cobo_waas2.WalletType()
        wallet_subtype = cobo_waas2.WalletSubtype()
        chain_ids = 'BTC,ETH'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_supported_chains(wallet_type=wallet_type, wallet_subtype=wallet_subtype, chain_ids=chain_ids, limit=limit, before=before, after=after)
        """

    def test_list_supported_tokens(self) -> None:
        """
        Test case for list_supported_tokens

        List supported tokens
        """
        """
        wallet_type = cobo_waas2.WalletType()
        wallet_subtype = cobo_waas2.WalletSubtype()
        chain_ids = 'BTC,ETH'
        token_ids = 'ETH_USDT,ETH_USDC'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_supported_tokens(wallet_type=wallet_type, wallet_subtype=wallet_subtype, chain_ids=chain_ids, token_ids=token_ids, limit=limit, before=before, after=after)
        """

    def test_list_token_balances_for_address(self) -> None:
        """
        Test case for list_token_balances_for_address

        List token balances by address
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
        token_ids = 'ETH_USDT,ETH_USDC'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_token_balances_for_address(wallet_id, address, token_ids=token_ids, limit=limit, before=before, after=after)
        """

    def test_list_token_balances_for_wallet(self) -> None:
        """
        Test case for list_token_balances_for_wallet

        List token balances by wallet
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        token_ids = 'ETH_USDT,ETH_USDC'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_token_balances_for_wallet(wallet_id, token_ids=token_ids, limit=limit, before=before, after=after)
        """

    def test_list_token_listing_requests(self) -> None:
        """
        Test case for list_token_listing_requests

        List token listing requests
        """
        """
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
        status = cobo_waas2.TokenListingRequestStatus()

        api_response = self.api.list_token_listing_requests(limit=limit, before=before, after=after, status=status)
        """

    def test_list_utxos(self) -> None:
        """
        Test case for list_utxos

        List UTXOs
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        token_id = 'ETH_USDT'
        address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
        tx_hash = 'dd7e1cecf6bbde1844ee1815b780711a1e306a718bcd23cd64401b48ef88eb83'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_utxos(wallet_id, token_id, address=address, tx_hash=tx_hash, limit=limit, before=before, after=after)
        """

    def test_list_wallets(self) -> None:
        """
        Test case for list_wallets

        List all wallets
        """
        """
        wallet_type = cobo_waas2.WalletType()
        wallet_subtype = cobo_waas2.WalletSubtype()
        project_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_wallets(wallet_type=wallet_type, wallet_subtype=wallet_subtype, project_id=project_id, vault_id=vault_id, limit=limit, before=before, after=after)
        """

    def test_lock_utxos(self) -> None:
        """
        Test case for lock_utxos

        Lock UTXOs
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        lock_utxos_request = cobo_waas2.LockUtxosRequest()

        api_response = self.api.lock_utxos(wallet_id, lock_utxos_request=lock_utxos_request)
        """

    def test_refresh_address_balances_by_token(self) -> None:
        """
        Test case for refresh_address_balances_by_token

        Refresh address balances by token
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        token_id = 'ETH_USDT'
        refresh_address_balances_by_token_request = cobo_waas2.RefreshAddressBalancesByTokenRequest()

        api_response = self.api.refresh_address_balances_by_token(wallet_id, token_id, refresh_address_balances_by_token_request=refresh_address_balances_by_token_request)
        """

    def test_unlock_utxos(self) -> None:
        """
        Test case for unlock_utxos

        Unlock UTXOs
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        lock_utxos_request = cobo_waas2.LockUtxosRequest()

        api_response = self.api.unlock_utxos(wallet_id, lock_utxos_request=lock_utxos_request)
        """

    def test_update_wallet_by_id(self) -> None:
        """
        Test case for update_wallet_by_id

        Update wallet
        """
        """
        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        update_wallet_params = cobo_waas2.UpdateWalletParams()

        api_response = self.api.update_wallet_by_id(wallet_id, update_wallet_params=update_wallet_params)
        """


if __name__ == '__main__':
    unittest.main()
