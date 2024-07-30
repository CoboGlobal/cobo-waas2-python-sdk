# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.update_webhook_endpoint_by_id_request import UpdateWebhookEndpointByIdRequest


class TestUpdateWebhookEndpointByIdRequest(unittest.TestCase):
    """UpdateWebhookEndpointByIdRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateWebhookEndpointByIdRequest:
        """Test UpdateWebhookEndpointByIdRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateWebhookEndpointByIdRequest`
        """
        model = UpdateWebhookEndpointByIdRequest()
        if include_optional:
            return UpdateWebhookEndpointByIdRequest(
                subscribed_events = [
                    'wallets.transaction.created'
                    ],
                status = 'STATUS_INACTIVE',
                description = 'My webhook endpoint'
            )
        else:
            return UpdateWebhookEndpointByIdRequest(
        )
        """

    def testUpdateWebhookEndpointByIdRequest(self):
        """Test UpdateWebhookEndpointByIdRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
