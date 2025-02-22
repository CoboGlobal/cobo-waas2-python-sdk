# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.safe_wallet_delegates_transfer import SafeWalletDelegatesTransfer


class TestSafeWalletDelegatesTransfer(unittest.TestCase):
    """SafeWalletDelegatesTransfer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SafeWalletDelegatesTransfer:
        """Test SafeWalletDelegatesTransfer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SafeWalletDelegatesTransfer`
        """
        model = SafeWalletDelegatesTransfer()
        if include_optional:
            return SafeWalletDelegatesTransfer(
                request_type = 'Transfer',
                token_id = 'ETH',
                amount = '0.1',
                address = '0x1234567890123456789012345678901234567890'
            )
        else:
            return SafeWalletDelegatesTransfer(
                request_type = 'Transfer',
                token_id = 'ETH',
        )
        """

    def testSafeWalletDelegatesTransfer(self):
        """Test SafeWalletDelegatesTransfer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
