# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_deposit_from_loop_source import TransactionDepositFromLoopSource


class TestTransactionDepositFromLoopSource(unittest.TestCase):
    """TransactionDepositFromLoopSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionDepositFromLoopSource:
        """Test TransactionDepositFromLoopSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionDepositFromLoopSource`
        """
        model = TransactionDepositFromLoopSource()
        if include_optional:
            return TransactionDepositFromLoopSource(
                source_type = 'DepositFromAddress'
            )
        else:
            return TransactionDepositFromLoopSource(
                source_type = 'DepositFromAddress',
        )
        """

    def testTransactionDepositFromLoopSource(self):
        """Test TransactionDepositFromLoopSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
