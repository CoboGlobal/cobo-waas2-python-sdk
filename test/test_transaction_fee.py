# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_fee import TransactionFee


class TestTransactionFee(unittest.TestCase):
    """TransactionFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionFee:
        """Test TransactionFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionFee`
        """
        model = TransactionFee()
        if include_optional:
            return TransactionFee(
                fee_type = 'EVM_EIP_1559',
                token_id = 'TRON',
                effective_gas_price = '100000000',
                fee_used = '0.1',
                gas_used = '100000000',
                max_fee_per_gas = '9000000000000',
                max_priority_fee_per_gas = '1000000000000',
                gas_limit = '21000',
                gas_price = '100000000',
                max_fee_amount = '0.1',
                fee_rate = '50'
            )
        else:
            return TransactionFee(
                fee_type = 'EVM_EIP_1559',
        )
        """

    def testTransactionFee(self):
        """Test TransactionFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
