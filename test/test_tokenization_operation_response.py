# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse


class TestTokenizationOperationResponse(unittest.TestCase):
    """TokenizationOperationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenizationOperationResponse:
        """Test TokenizationOperationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenizationOperationResponse`
        """
        model = TokenizationOperationResponse()
        if include_optional:
            return TokenizationOperationResponse(
                activity_id = 'b7c8e9d0-f1a2-3b4c-5d6e-7f8a9b0c1d2e'
            )
        else:
            return TokenizationOperationResponse(
                activity_id = 'b7c8e9d0-f1a2-3b4c-5d6e-7f8a9b0c1d2e',
        )
        """

    def testTokenizationOperationResponse(self):
        """Test TokenizationOperationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
