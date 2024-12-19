# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.eth_staking_extra import EthStakingExtra


class TestEthStakingExtra(unittest.TestCase):
    """EthStakingExtra unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EthStakingExtra:
        """Test EthStakingExtra
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EthStakingExtra`
        """
        model = EthStakingExtra()
        if include_optional:
            return EthStakingExtra(
                pool_type = 'Babylon',
                pos_chain = 'Ethereum',
                beacon_validators = [
                    cobo_waas2.models.eth_staking_extra_all_of_beacon_validators.EthStakingExtra_allOf_beacon_validators(
                        pubkey = '0x123456789abcdef', 
                        status = 'Active', 
                        apy = 0.02, 
                        staked_amount = '100.00', 
                        rewards_received = '10.00', 
                        updated_timestamp = 1640995200000, )
                    ]
            )
        else:
            return EthStakingExtra(
                pool_type = 'Babylon',
                pos_chain = 'Ethereum',
        )
        """

    def testEthStakingExtra(self):
        """Test EthStakingExtra"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
