# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tss_key_reshare_request import TSSKeyReshareRequest


class TestTSSKeyReshareRequest(unittest.TestCase):
    """TSSKeyReshareRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TSSKeyReshareRequest:
        """Test TSSKeyReshareRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TSSKeyReshareRequest`
        """
        model = TSSKeyReshareRequest()
        if include_optional:
            return TSSKeyReshareRequest(
                old_group_id = 'mMedDioOKhTlhGyQRzMv',
                root_pub_key = 'xpub661MyMwAqRbcG4vPNi58VQJrXW8D9VzmauuRq2rTY3oUVnKGuLTxQxvvoEXgLvZ7N9GQXQkWVgKn1rzEUUEm4NdvrBKUqjpNJEnn2UL4rYq',
                curve = 0,
                used_node_ids = [
                    '["coboAbCdEfGhIjKlMnOpQrStUvWxYz1234567890abcdefghi","coboBTGDvjJG99pABegvPYmavrcTU3SkjTLHVdsko8dWBga4w"]'
                    ],
                old_threshold = 2,
                new_threshold = 2,
                new_node_ids = [
                    '["coboAbCdEfGhIjKlMnOpQrStUvWxYz1234567890abcdefghi","coboBTGDvjJG99pABegvPYmavrcTU3SkjTLHVdsko8dWBga4w"]'
                    ],
                task_id = '20231213122855000000000000000000',
                biz_task_id = '20231213122855000000000000000000'
            )
        else:
            return TSSKeyReshareRequest(
        )
        """

    def testTSSKeyReshareRequest(self):
        """Test TSSKeyReshareRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
