# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.list_supported_chains200_response import ListSupportedChains200Response


class TestListSupportedChains200Response(unittest.TestCase):
    """ListSupportedChains200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListSupportedChains200Response:
        """Test ListSupportedChains200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListSupportedChains200Response`
        """
        model = ListSupportedChains200Response()
        if include_optional:
            return ListSupportedChains200Response(
                data = [
                    cobo_waas2.models.chain_info.ChainInfo(
                        chain_id = 'ETH', 
                        symbol = 'ETH', 
                        icon_url = 'https://d.cobo.com/public/logos/ETH.png', 
                        explorer_tx_url = 'https://etherscan.io/tx/{txn_id}', 
                        explorer_address_url = 'https://etherscan.io/address/{address}', 
                        require_memo = False, 
                        confirming_threshold = 15, 
                        coinbase_maturity = 15, )
                    ],
                pagination = cobo_waas2.models.pagination.Pagination(
                    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1', 
                    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk', 
                    total_count = 10000, )
            )
        else:
            return ListSupportedChains200Response(
        )
        """

    def testListSupportedChains200Response(self):
        """Test ListSupportedChains200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
