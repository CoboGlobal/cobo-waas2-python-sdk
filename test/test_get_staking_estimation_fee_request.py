# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.get_staking_estimation_fee_request import GetStakingEstimationFeeRequest


class TestGetStakingEstimationFeeRequest(unittest.TestCase):
    """GetStakingEstimationFeeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetStakingEstimationFeeRequest:
        """Test GetStakingEstimationFeeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStakingEstimationFeeRequest`
        """
        model = GetStakingEstimationFeeRequest()
        if include_optional:
            return GetStakingEstimationFeeRequest(
                activity_type = 'Stake',
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                source = None,
                pool_id = 'babylon_btc_signet',
                amount = '100.00',
                fee = None,
                extra = None,
                staking_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
            )
        else:
            return GetStakingEstimationFeeRequest(
                activity_type = 'Stake',
                pool_id = 'babylon_btc_signet',
                amount = '100.00',
                fee = None,
                extra = None,
                staking_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
        )
        """

    def testGetStakingEstimationFeeRequest(self):
        """Test GetStakingEstimationFeeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
