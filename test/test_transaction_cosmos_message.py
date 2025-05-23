# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_cosmos_message import TransactionCosmosMessage


class TestTransactionCosmosMessage(unittest.TestCase):
    """TransactionCosmosMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionCosmosMessage:
        """Test TransactionCosmosMessage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionCosmosMessage`
        """
        model = TransactionCosmosMessage()
        if include_optional:
            return TransactionCosmosMessage(
                type_url = '/babylon.btcstaking.v1.MsgCreateBTCDelegation',
                message = 'eyJ0eXBlIjoiYmFiY29zZS5idGNzdGFnaW5nLnYxLk1zZ0NyZWF0ZUJUQ0RlbGVnYXRpb24iLCJtZXNzYWdlIjp7ImNvbW1hbmRfaWQiOiJjb21tYW5kX2lkIiwibWVzc2FnZV92YWx1ZSI6Im1lc3NhZ2VfdmFsdWUiLCJtZXNzYWdlX3R5cGUiOiJtZXNzYWdlX3R5cGUifX0='
            )
        else:
            return TransactionCosmosMessage(
                type_url = '/babylon.btcstaking.v1.MsgCreateBTCDelegation',
                message = 'eyJ0eXBlIjoiYmFiY29zZS5idGNzdGFnaW5nLnYxLk1zZ0NyZWF0ZUJUQ0RlbGVnYXRpb24iLCJtZXNzYWdlIjp7ImNvbW1hbmRfaWQiOiJjb21tYW5kX2lkIiwibWVzc2FnZV92YWx1ZSI6Im1lc3NhZ2VfdmFsdWUiLCJtZXNzYWdlX3R5cGUiOiJtZXNzYWdlX3R5cGUifX0=',
        )
        """

    def testTransactionCosmosMessage(self):
        """Test TransactionCosmosMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
