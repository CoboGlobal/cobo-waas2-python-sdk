# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_evm_contract_destination import TransactionEvmContractDestination


class TestTransactionEvmContractDestination(unittest.TestCase):
    """TransactionEvmContractDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionEvmContractDestination:
        """Test TransactionEvmContractDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionEvmContractDestination`
        """
        model = TransactionEvmContractDestination()
        if include_optional:
            return TransactionEvmContractDestination(
                destination_type = 'Address',
                address = '0x0406db8351aa6839169bb363f63c2c808fee8f99',
                value = '1.5',
                calldata = '0xa22cb4650000000000000000000000001e0049783f008a0085193e00003d00cd54003c71000000000000000000000000000000000000000000000000000000000000DEMO'
            )
        else:
            return TransactionEvmContractDestination(
                destination_type = 'Address',
                address = '0x0406db8351aa6839169bb363f63c2c808fee8f99',
                calldata = '0xa22cb4650000000000000000000000001e0049783f008a0085193e00003d00cd54003c71000000000000000000000000000000000000000000000000000000000000DEMO',
        )
        """

    def testTransactionEvmContractDestination(self):
        """Test TransactionEvmContractDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
