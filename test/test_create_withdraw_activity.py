# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_withdraw_activity import CreateWithdrawActivity


class TestCreateWithdrawActivity(unittest.TestCase):
    """CreateWithdrawActivity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateWithdrawActivity:
        """Test CreateWithdrawActivity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateWithdrawActivity`
        """
        model = CreateWithdrawActivity()
        if include_optional:
            return CreateWithdrawActivity(
                staking_id = '0011039d-27fb-49ba-b172-6e0aa80e37ec',
                amount = '100.00',
                address = '0xdAC17F958D2ee523a2206206994597C13D831ec7',
                fee = None
            )
        else:
            return CreateWithdrawActivity(
                staking_id = '0011039d-27fb-49ba-b172-6e0aa80e37ec',
                fee = None,
        )
        """

    def testCreateWithdrawActivity(self):
        """Test CreateWithdrawActivity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
