# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_bip137_destination import TransactionBIP137Destination


class TestTransactionBIP137Destination(unittest.TestCase):
    """TransactionBIP137Destination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionBIP137Destination:
        """Test TransactionBIP137Destination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionBIP137Destination`
        """
        model = TransactionBIP137Destination()
        if include_optional:
            return TransactionBIP137Destination(
                destination_type = 'Address',
                message_bip137 = ''
            )
        else:
            return TransactionBIP137Destination(
                destination_type = 'Address',
                message_bip137 = '',
        )
        """

    def testTransactionBIP137Destination(self):
        """Test TransactionBIP137Destination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
