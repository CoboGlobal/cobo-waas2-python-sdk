# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.account import Account


class TestAccount(unittest.TestCase):
    """Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Account:
        """Test Account
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Account`
        """
        model = Account()
        if include_optional:
            return Account(
                token_id = 'ETH_USDT',
                address = '0xF8e4bfc10A2821DF52D3322cB5170E5E9276b537',
                merchant_balance = '0.15',
                psp_balance = '0.15',
                created_timestamp = 1610445878970,
                updated_timestamp = 1610445878970
            )
        else:
            return Account(
                token_id = 'ETH_USDT',
                address = '0xF8e4bfc10A2821DF52D3322cB5170E5E9276b537',
                merchant_balance = '0.15',
                psp_balance = '0.15',
        )
        """

    def testAccount(self):
        """Test Account"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
