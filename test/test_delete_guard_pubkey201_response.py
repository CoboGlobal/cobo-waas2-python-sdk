# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.delete_guard_pubkey201_response import DeleteGuardPubkey201Response


class TestDeleteGuardPubkey201Response(unittest.TestCase):
    """DeleteGuardPubkey201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteGuardPubkey201Response:
        """Test DeleteGuardPubkey201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteGuardPubkey201Response`
        """
        model = DeleteGuardPubkey201Response()
        if include_optional:
            return DeleteGuardPubkey201Response(
                statement_id = '0111039d-27fb-49ba-b172-6e0aa80e37ec'
            )
        else:
            return DeleteGuardPubkey201Response(
                statement_id = '0111039d-27fb-49ba-b172-6e0aa80e37ec',
        )
        """

    def testDeleteGuardPubkey201Response(self):
        """Test DeleteGuardPubkey201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
