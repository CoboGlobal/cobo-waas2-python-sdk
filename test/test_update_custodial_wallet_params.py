# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.update_custodial_wallet_params import UpdateCustodialWalletParams


class TestUpdateCustodialWalletParams(unittest.TestCase):
    """UpdateCustodialWalletParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateCustodialWalletParams:
        """Test UpdateCustodialWalletParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCustodialWalletParams`
        """
        model = UpdateCustodialWalletParams()
        if include_optional:
            return UpdateCustodialWalletParams(
                wallet_type = 'Custodial',
                name = 'My WaaS 2.0 Wallet'
            )
        else:
            return UpdateCustodialWalletParams(
                wallet_type = 'Custodial',
        )
        """

    def testUpdateCustodialWalletParams(self):
        """Test UpdateCustodialWalletParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
