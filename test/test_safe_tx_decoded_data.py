# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.safe_tx_decoded_data import SafeTxDecodedData


class TestSafeTxDecodedData(unittest.TestCase):
    """SafeTxDecodedData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SafeTxDecodedData:
        """Test SafeTxDecodedData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SafeTxDecodedData`
        """
        model = SafeTxDecodedData()
        if include_optional:
            return SafeTxDecodedData(
                method = 'transfer',
                parameters = [
                    cobo_waas2.models.safe_tx_decoded_data_parameters.SafeTxDecodedDataParameters(
                        name = 'recipient', 
                        type = 'address', 
                        value = '0x1234567890abcdef1234567890abcdef12345678', 
                        value_decoded = [
                            cobo_waas2.models.safe_tx_sub_transaction.SafeTxSubTransaction(
                                operation = 'Call', 
                                to = '0xabcdefabcdefabcdefabcdefabcdefabcdef', 
                                value = '1 ETH', 
                                wei = '1000000000000000000', 
                                data = '0xabcdef...', 
                                data_decoded = cobo_waas2.models.safe_tx_decoded_data.SafeTxDecodedData(
                                    method = 'transfer', ), 
                                to_contract_name = 'UniswapV2Router', )
                            ], )
                    ]
            )
        else:
            return SafeTxDecodedData(
        )
        """

    def testSafeTxDecodedData(self):
        """Test SafeTxDecodedData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
