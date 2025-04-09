# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_cosmos_contract_destination import TransactionCosmosContractDestination


class TestTransactionCosmosContractDestination(unittest.TestCase):
    """TransactionCosmosContractDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionCosmosContractDestination:
        """Test TransactionCosmosContractDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionCosmosContractDestination`
        """
        model = TransactionCosmosContractDestination()
        if include_optional:
            return TransactionCosmosContractDestination(
                destination_type = 'Address',
                cosmos_messages = [
                    cobo_waas2.models.cosmos_message.Cosmos Message(
                        type_url = '/babylon.btcstaking.v1.MsgCreateBTCDelegation', 
                        message = 'eyJ0eXBlIjoiYmFiY29zZS5idGNzdGFnaW5nLnYxLk1zZ0NyZWF0ZUJUQ0RlbGVnYXRpb24iLCJtZXNzYWdlIjp7ImNvbW1hbmRfaWQiOiJjb21tYW5kX2lkIiwibWVzc2FnZV92YWx1ZSI6Im1lc3NhZ2VfdmFsdWUiLCJtZXNzYWdlX3R5cGUiOiJtZXNzYWdlX3R5cGUifX0=', )
                    ],
                value = '1.5'
            )
        else:
            return TransactionCosmosContractDestination(
                destination_type = 'Address',
                cosmos_messages = [
                    cobo_waas2.models.cosmos_message.Cosmos Message(
                        type_url = '/babylon.btcstaking.v1.MsgCreateBTCDelegation', 
                        message = 'eyJ0eXBlIjoiYmFiY29zZS5idGNzdGFnaW5nLnYxLk1zZ0NyZWF0ZUJUQ0RlbGVnYXRpb24iLCJtZXNzYWdlIjp7ImNvbW1hbmRfaWQiOiJjb21tYW5kX2lkIiwibWVzc2FnZV92YWx1ZSI6Im1lc3NhZ2VfdmFsdWUiLCJtZXNzYWdlX3R5cGUiOiJtZXNzYWdlX3R5cGUifX0=', )
                    ],
        )
        """

    def testTransactionCosmosContractDestination(self):
        """Test TransactionCosmosContractDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
