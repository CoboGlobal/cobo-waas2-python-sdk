# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_stake_activity201_response import CreateStakeActivity201Response


class TestCreateStakeActivity201Response(unittest.TestCase):
    """CreateStakeActivity201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateStakeActivity201Response:
        """Test CreateStakeActivity201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateStakeActivity201Response`
        """
        model = CreateStakeActivity201Response()
        if include_optional:
            return CreateStakeActivity201Response(
                activity_id = '0111039d-27fb-49ba-b172-6e0aa80e37ec',
                staking_id = '0111039d-27fb-49ba-b172-6e0aa80e37ec'
            )
        else:
            return CreateStakeActivity201Response(
                activity_id = '0111039d-27fb-49ba-b172-6e0aa80e37ec',
        )
        """

    def testCreateStakeActivity201Response(self):
        """Test CreateStakeActivity201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
