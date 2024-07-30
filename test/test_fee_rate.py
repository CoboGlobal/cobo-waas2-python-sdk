# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.fee_rate import FeeRate


class TestFeeRate(unittest.TestCase):
    """FeeRate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FeeRate:
        """Test FeeRate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FeeRate`
        """
        model = FeeRate()
        if include_optional:
            return FeeRate(
                fee_type = 'EVM_EIP_1559',
                token_id = 'BTC',
                fee_amount = '0.1',
                slow = cobo_waas2.models.utxo_fee_base_price.UtxoFeeBasePrice(
                    fee_rate = '50', ),
                recommended = cobo_waas2.models.utxo_fee_base_price.UtxoFeeBasePrice(
                    fee_rate = '50', ),
                fast = cobo_waas2.models.utxo_fee_base_price.UtxoFeeBasePrice(
                    fee_rate = '50', )
            )
        else:
            return FeeRate(
                fee_type = 'EVM_EIP_1559',
                token_id = 'BTC',
                recommended = cobo_waas2.models.utxo_fee_base_price.UtxoFeeBasePrice(
                    fee_rate = '50', ),
        )
        """

    def testFeeRate(self):
        """Test FeeRate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
