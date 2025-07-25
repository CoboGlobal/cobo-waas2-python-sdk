# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tokenization_update_allowlist_addresses_request import TokenizationUpdateAllowlistAddressesRequest


class TestTokenizationUpdateAllowlistAddressesRequest(unittest.TestCase):
    """TokenizationUpdateAllowlistAddressesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenizationUpdateAllowlistAddressesRequest:
        """Test TokenizationUpdateAllowlistAddressesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenizationUpdateAllowlistAddressesRequest`
        """
        model = TokenizationUpdateAllowlistAddressesRequest()
        if include_optional:
            return TokenizationUpdateAllowlistAddressesRequest(
                action = 'Grant',
                source = None,
                addresses = [{"address":"0x789abc...","note":"reason for allowing"},{"address":"0xdef012..."}],
                app_initiator = 'steve@example.com',
                fee = None
            )
        else:
            return TokenizationUpdateAllowlistAddressesRequest(
                action = 'Grant',
                source = None,
                addresses = [{"address":"0x789abc...","note":"reason for allowing"},{"address":"0xdef012..."}],
                fee = None,
        )
        """

    def testTokenizationUpdateAllowlistAddressesRequest(self):
        """Test TokenizationUpdateAllowlistAddressesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
