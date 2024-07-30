# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_fixed_fee import TransactionFixedFee


class TestTransactionFixedFee(unittest.TestCase):
    """TransactionFixedFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionFixedFee:
        """Test TransactionFixedFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionFixedFee`
        """
        model = TransactionFixedFee()
        if include_optional:
            return TransactionFixedFee(
                max_fee_amount = '0.1',
                fee_type = 'EVM_EIP_1559',
                token_id = 'TRON',
                fee_used = '0.1'
            )
        else:
            return TransactionFixedFee(
                fee_type = 'EVM_EIP_1559',
        )
        """

    def testTransactionFixedFee(self):
        """Test TransactionFixedFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
