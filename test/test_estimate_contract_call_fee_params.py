# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.estimate_contract_call_fee_params import EstimateContractCallFeeParams


class TestEstimateContractCallFeeParams(unittest.TestCase):
    """EstimateContractCallFeeParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimateContractCallFeeParams:
        """Test EstimateContractCallFeeParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimateContractCallFeeParams`
        """
        model = EstimateContractCallFeeParams()
        if include_optional:
            return EstimateContractCallFeeParams(
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                request_type = 'Transfer',
                chain_id = 'ETH',
                source = None,
                destination = None,
                fee_type = 'EVM_EIP_1559',
                replaced_transaction_id = 'aff0e1cb-15b2-4e1f-9b9d-a9133715986f'
            )
        else:
            return EstimateContractCallFeeParams(
                request_type = 'Transfer',
                chain_id = 'ETH',
                source = None,
                destination = None,
        )
        """

    def testEstimateContractCallFeeParams(self):
        """Test EstimateContractCallFeeParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
