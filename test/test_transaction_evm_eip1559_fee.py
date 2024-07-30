# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_evm_eip1559_fee import TransactionEvmEip1559Fee


class TestTransactionEvmEip1559Fee(unittest.TestCase):
    """TransactionEvmEip1559Fee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionEvmEip1559Fee:
        """Test TransactionEvmEip1559Fee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionEvmEip1559Fee`
        """
        model = TransactionEvmEip1559Fee()
        if include_optional:
            return TransactionEvmEip1559Fee(
                max_fee_per_gas = '9000000000000',
                max_priority_fee_per_gas = '1000000000000',
                gas_limit = '21000',
                fee_type = 'EVM_EIP_1559',
                token_id = 'ETH',
                effective_gas_price = '100000000',
                fee_used = '0.1',
                gas_used = '100000000'
            )
        else:
            return TransactionEvmEip1559Fee(
                fee_type = 'EVM_EIP_1559',
        )
        """

    def testTransactionEvmEip1559Fee(self):
        """Test TransactionEvmEip1559Fee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
