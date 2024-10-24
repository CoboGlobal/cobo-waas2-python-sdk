# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.refresh_token201_response import RefreshToken201Response


class TestRefreshToken201Response(unittest.TestCase):
    """RefreshToken201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RefreshToken201Response:
        """Test RefreshToken201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RefreshToken201Response`
        """
        model = RefreshToken201Response()
        if include_optional:
            return RefreshToken201Response(
                access_token = 'AnCEPEp5Q8qjAOA1Lb6kVd2OlkCyJnMTeMPdLbPOM8cz176Eb5y7EJoUjJJ0vkzz',
                token_type = 'Bearer',
                scope = '',
                expires_in = 43199,
                refresh_token = 'rK49jI0zt49gsttzscscik15Asmlpu1TdcxqguJJS8B9f6ilJEC0y3PbVqwsEAw5'
            )
        else:
            return RefreshToken201Response(
        )
        """

    def testRefreshToken201Response(self):
        """Test RefreshToken201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()