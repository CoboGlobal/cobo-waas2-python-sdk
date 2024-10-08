# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_wallet_params import CreateWalletParams


class TestCreateWalletParams(unittest.TestCase):
    """CreateWalletParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateWalletParams:
        """Test CreateWalletParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateWalletParams`
        """
        model = CreateWalletParams()
        if include_optional:
            return CreateWalletParams(
                name = 'My WaaS 2.0 Wallet',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                vault_id = '',
                exchange_id = 'binance',
                apikey = 'd8f062da-39f4-4a11-8b9d-12595854237f',
                secret = '75B4F636193162488A3728B4A5797708',
                passphrase = 'sXASDKWKLLsWWEE',
                memo = 'xxx@cobo.com',
                account_identify = 'xxx@cobo.com',
                ga_code = 'sXASDKWKLLsWWEE75B4F636193162488A3728B4A5797708',
                main_wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
            )
        else:
            return CreateWalletParams(
                name = 'My WaaS 2.0 Wallet',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                vault_id = '',
                exchange_id = 'binance',
                apikey = 'd8f062da-39f4-4a11-8b9d-12595854237f',
                secret = '75B4F636193162488A3728B4A5797708',
        )
        """

    def testCreateWalletParams(self):
        """Test CreateWalletParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
