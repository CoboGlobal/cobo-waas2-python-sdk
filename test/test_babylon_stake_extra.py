# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.babylon_stake_extra import BabylonStakeExtra


class TestBabylonStakeExtra(unittest.TestCase):
    """BabylonStakeExtra unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BabylonStakeExtra:
        """Test BabylonStakeExtra
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BabylonStakeExtra`
        """
        model = BabylonStakeExtra()
        if include_optional:
            return BabylonStakeExtra(
                pool_type = 'Babylon',
                finality_provider_public_key = '0000000000000000000000000000000000000000000000000000000000000000',
                stake_block_time = 2000
            )
        else:
            return BabylonStakeExtra(
                pool_type = 'Babylon',
                finality_provider_public_key = '0000000000000000000000000000000000000000000000000000000000000000',
                stake_block_time = 2000,
        )
        """

    def testBabylonStakeExtra(self):
        """Test BabylonStakeExtra"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
