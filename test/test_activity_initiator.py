# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.activity_initiator import ActivityInitiator


class TestActivityInitiator(unittest.TestCase):
    """ActivityInitiator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityInitiator:
        """Test ActivityInitiator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityInitiator`
        """
        model = ActivityInitiator()
        if include_optional:
            return ActivityInitiator(
                initiator = 'vanya@cobo.com'
            )
        else:
            return ActivityInitiator(
        )
        """

    def testActivityInitiator(self):
        """Test ActivityInitiator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
