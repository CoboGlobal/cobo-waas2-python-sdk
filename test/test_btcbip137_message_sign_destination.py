# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.btcbip137_message_sign_destination import BTCBIP137MessageSignDestination


class TestBTCBIP137MessageSignDestination(unittest.TestCase):
    """BTCBIP137MessageSignDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BTCBIP137MessageSignDestination:
        """Test BTCBIP137MessageSignDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BTCBIP137MessageSignDestination`
        """
        model = BTCBIP137MessageSignDestination()
        if include_optional:
            return BTCBIP137MessageSignDestination(
                destination_type = 'EVM_EIP_191_Signature',
                message_bip137 = ''
            )
        else:
            return BTCBIP137MessageSignDestination(
                destination_type = 'EVM_EIP_191_Signature',
                message_bip137 = '',
        )
        """

    def testBTCBIP137MessageSignDestination(self):
        """Test BTCBIP137MessageSignDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
