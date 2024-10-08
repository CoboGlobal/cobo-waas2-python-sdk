# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.eigen_layer_lst_stake_extra import EigenLayerLstStakeExtra


class TestEigenLayerLstStakeExtra(unittest.TestCase):
    """EigenLayerLstStakeExtra unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EigenLayerLstStakeExtra:
        """Test EigenLayerLstStakeExtra
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EigenLayerLstStakeExtra`
        """
        model = EigenLayerLstStakeExtra()
        if include_optional:
            return EigenLayerLstStakeExtra(
                pool_type = 'Babylon',
                operator = '0xdAC17F958D2ee523a2206206994597C13D831ec7'
            )
        else:
            return EigenLayerLstStakeExtra(
                pool_type = 'Babylon',
        )
        """

    def testEigenLayerLstStakeExtra(self):
        """Test EigenLayerLstStakeExtra"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
