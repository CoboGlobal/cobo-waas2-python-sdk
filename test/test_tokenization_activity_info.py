# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tokenization_activity_info import TokenizationActivityInfo


class TestTokenizationActivityInfo(unittest.TestCase):
    """TokenizationActivityInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenizationActivityInfo:
        """Test TokenizationActivityInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenizationActivityInfo`
        """
        model = TokenizationActivityInfo()
        if include_optional:
            return TokenizationActivityInfo(
                activity_id = 'b7c8e9d0-f1a2-3b4c-5d6e-7f8a9b0c1d2e',
                token_id = 'BTC',
                type = 'Issue',
                status = 'Processing',
                source = None,
                initiator = 'steve@example.com',
                initiator_type = 'API',
                transaction_ids = [
                    '0011039d-27fb-49ba-b172-6e0aa80e37ec'
                    ],
                created_timestamp = 1678886400000,
                updated_timestamp = 1678886400000
            )
        else:
            return TokenizationActivityInfo(
                activity_id = 'b7c8e9d0-f1a2-3b4c-5d6e-7f8a9b0c1d2e',
                token_id = 'BTC',
                type = 'Issue',
                status = 'Processing',
                source = None,
                initiator = 'steve@example.com',
                initiator_type = 'API',
                updated_timestamp = 1678886400000,
        )
        """

    def testTokenizationActivityInfo(self):
        """Test TokenizationActivityInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
