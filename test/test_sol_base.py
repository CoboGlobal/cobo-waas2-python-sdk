# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.sol_base import SOLBase


class TestSOLBase(unittest.TestCase):
    """SOLBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SOLBase:
        """Test SOLBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SOLBase`
        """
        model = SOLBase()
        if include_optional:
            return SOLBase(
                base_fee = '0.000005',
                rent_amount = '0.00001 '
            )
        else:
            return SOLBase(
        )
        """

    def testSOLBase(self):
        """Test SOLBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
