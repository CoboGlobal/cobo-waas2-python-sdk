# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.swap_quote import SwapQuote


class TestSwapQuote(unittest.TestCase):
    """SwapQuote unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwapQuote:
        """Test SwapQuote
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SwapQuote`
        """
        model = SwapQuote()
        if include_optional:
            return SwapQuote(
                quote_id = '2ec094034044ffa50f4294d48363fef31eb5755fc783ba3837a03c91b4904659',
                pay_token_id = 'BTC',
                pay_amount = '100',
                receive_token_id = 'ETH_WBTC',
                receive_amount = '100',
                fee_token_id = 'BTC',
                fee_amount = '0.3',
                estimated_network_fee_amount = '0.3',
                min_receive_amount = '0',
                max_pay_amount = '10000',
                quote_expired_timestamp = 1677587393000
            )
        else:
            return SwapQuote(
                quote_id = '2ec094034044ffa50f4294d48363fef31eb5755fc783ba3837a03c91b4904659',
                pay_token_id = 'BTC',
                pay_amount = '100',
                receive_token_id = 'ETH_WBTC',
                receive_amount = '100',
                fee_token_id = 'BTC',
                fee_amount = '0.3',
                quote_expired_timestamp = 1677587393000,
        )
        """

    def testSwapQuote(self):
        """Test SwapQuote"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
