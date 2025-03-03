# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.babylon_eligible_airdrop import BabylonEligibleAirdrop


class TestBabylonEligibleAirdrop(unittest.TestCase):
    """BabylonEligibleAirdrop unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BabylonEligibleAirdrop:
        """Test BabylonEligibleAirdrop
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BabylonEligibleAirdrop`
        """
        model = BabylonEligibleAirdrop()
        if include_optional:
            return BabylonEligibleAirdrop(
                btc_address = None,
                babylon_address = None,
                babylon_points = '1000.50',
                airdrop_amount = '500.25',
                status = 'Registered',
                pop = cobo_waas2.models.babylon_airdrop_pop.BabylonAirdropPop(
                    baby_address = 'bbn1xjz8fs9vkmefdqaxan5kv2d09vmwzru7jhy424', 
                    btc_address = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 
                    btc_public_key = '79f71003589158b2579345540b08bbc74974c49dd5e0782e31d0de674540d513', 
                    btc_sign_baby = 'AkcwRAIgcrI2IdD2JSFVIeQmtRA3wFjjiy+qEvqbX57rn6xvWWECIDis7vHSJeR8X91uMQReG0pPQFFLpeM0ga4BW+Tt2V54ASEDefcQA1iRWLJXk0VUCwi7x0l0xJ3V4HguMdDeZ0VA1RM=', 
                    baby_sign_btc = 'FnYTm9ZbhJZY202R9YBkjGEJqeJ/n5McZBpGH38P2pt0YRcjwOh8XgoeVQTU9So7/RHVHHdKNB09DVmtQJ7xtw==', 
                    baby_public_key = 'Asezdqkvh+kLbuD75DirSwi/QFbJjFe2SquiivMaPS65', )
            )
        else:
            return BabylonEligibleAirdrop(
        )
        """

    def testBabylonEligibleAirdrop(self):
        """Test BabylonEligibleAirdrop"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
