# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.mpc_vault_event_data import MPCVaultEventData


class TestMPCVaultEventData(unittest.TestCase):
    """MPCVaultEventData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MPCVaultEventData:
        """Test MPCVaultEventData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MPCVaultEventData`
        """
        model = MPCVaultEventData()
        if include_optional:
            return MPCVaultEventData(
                data_type = 'Transaction',
                vault_id = 'YPdbyVaVGqXXjkUsohHw',
                project_id = '0111039d-27fb-49ba-b172-6e0aa80e37ec',
                name = 'Vault name',
                type = 'Org-Controlled',
                root_pubkeys = [
                    cobo_waas2.models.root_pubkey.RootPubkey(
                        root_pubkey = 'xpub661MyMwAqRbcG4vPNi58VQJrXW8D9VzmauuRq2rTY3oUVnKGuLTxQxvvoEXgLvZ7N9GQXQkWVgKn1rzEUUEm4NdvrBKUqjpNJEnn2UL4rYq', 
                        curve = 'SECP256K1', )
                    ],
                created_timestamp = 1718619403933
            )
        else:
            return MPCVaultEventData(
                data_type = 'Transaction',
        )
        """

    def testMPCVaultEventData(self):
        """Test MPCVaultEventData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
