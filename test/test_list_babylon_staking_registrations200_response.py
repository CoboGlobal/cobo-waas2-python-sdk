# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.list_babylon_staking_registrations200_response import ListBabylonStakingRegistrations200Response


class TestListBabylonStakingRegistrations200Response(unittest.TestCase):
    """ListBabylonStakingRegistrations200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListBabylonStakingRegistrations200Response:
        """Test ListBabylonStakingRegistrations200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListBabylonStakingRegistrations200Response`
        """
        model = ListBabylonStakingRegistrations200Response()
        if include_optional:
            return ListBabylonStakingRegistrations200Response(
                data = [
                    cobo_waas2.models.babylon_staking_registration.BabylonStakingRegistration(
                        id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479', 
                        staking_id = '3f2840ce-44eb-450b-aa81-d3f84b772efb', 
                        babylon_address = null, 
                        btc_address = null, 
                        status = 'Processing', 
                        staked_amount = '500.25', 
                        error_message = 'User rejected', 
                        created_timestamp = 1677587333000, 
                        updated_timestamp = 1677587400000, )
                    ],
                pagination = cobo_waas2.models.pagination.Pagination(
                    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1', 
                    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk', 
                    total_count = 10000, )
            )
        else:
            return ListBabylonStakingRegistrations200Response(
        )
        """

    def testListBabylonStakingRegistrations200Response(self):
        """Test ListBabylonStakingRegistrations200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
