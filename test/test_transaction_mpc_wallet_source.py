# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_mpc_wallet_source import TransactionMPCWalletSource


class TestTransactionMPCWalletSource(unittest.TestCase):
    """TransactionMPCWalletSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionMPCWalletSource:
        """Test TransactionMPCWalletSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionMPCWalletSource`
        """
        model = TransactionMPCWalletSource()
        if include_optional:
            return TransactionMPCWalletSource(
                source_type = 'ExternalAddress',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku',
                included_utxos = [
                    cobo_waas2.models.transaction_utxo.TransactionUtxo(
                        tx_hash = '7014d7d9b91862d7131f7543d84da3bec60e20be93c23ad01167c48b778fdemo', 
                        vout_n = 0, )
                    ],
                excluded_utxos = [
                    cobo_waas2.models.transaction_utxo.TransactionUtxo(
                        tx_hash = '7014d7d9b91862d7131f7543d84da3bec60e20be93c23ad01167c48b778fdemo', 
                        vout_n = 0, )
                    ]
            )
        else:
            return TransactionMPCWalletSource(
                source_type = 'ExternalAddress',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
        )
        """

    def testTransactionMPCWalletSource(self):
        """Test TransactionMPCWalletSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
