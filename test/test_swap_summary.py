# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.swap_summary import SwapSummary


class TestSwapSummary(unittest.TestCase):
    """SwapSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwapSummary:
        """Test SwapSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SwapSummary`
        """
        model = SwapSummary()
        if include_optional:
            return SwapSummary(
                total_usd_value = '12345.67',
                activity_count = 100
            )
        else:
            return SwapSummary(
                total_usd_value = '12345.67',
                activity_count = 100,
        )
        """

    def testSwapSummary(self):
        """Test SwapSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
