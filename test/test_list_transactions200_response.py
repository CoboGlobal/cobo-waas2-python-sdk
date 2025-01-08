# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.list_transactions200_response import ListTransactions200Response


class TestListTransactions200Response(unittest.TestCase):
    """ListTransactions200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListTransactions200Response:
        """Test ListTransactions200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListTransactions200Response`
        """
        model = ListTransactions200Response()
        if include_optional:
            return ListTransactions200Response(
                data = [
                    cobo_waas2.models.transaction.Transaction(
                        transaction_id = 'aff0e1cb-15b2-4e1f-9b9d-a9133715986f', 
                        cobo_id = '20231213122855000000000000000000', 
                        request_id = 'web_send_by_user_327_1610444045047', 
                        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479', 
                        type = 'Deposit', 
                        status = 'Submitted', 
                        sub_status = 'PendingDoubleCheck', 
                        failed_reason = 'Rejected by signer Cobo TSS', 
                        chain_id = 'ETH', 
                        token_id = 'ETH_USDT', 
                        asset_id = 'USDT', 
                        source = null, 
                        destination = null, 
                        result = null, 
                        fee = null, 
                        initiator = 'API Prod Key #1', 
                        initiator_type = 'API', 
                        confirmed_num = 12, 
                        confirming_threshold = 15, 
                        transaction_hash = '239861be9a4afe080c359b7fe4a1d035945ec46256b1a0f44d1267c71de8ec28', 
                        block_info = cobo_waas2.models.transaction_block_info.TransactionBlockInfo(
                            block_number = 123, 
                            block_timestamp = 1717740319, 
                            block_hash = '0xc9ee947f8bb6027c161888bf0d004bec05e7c2beec7e6b187dc512174e438735', ), 
                        raw_tx_info = cobo_waas2.models.transaction_raw_tx_info.TransactionRawTxInfo(
                            used_nonce = 9, 
                            selected_utxos = [
                                cobo_waas2.models.transaction_selected_utxo.TransactionSelectedUtxo(
                                    tx_hash = '7014d7d9b91862d7131f7543d84da3bec60e20be93c23ad01167c48b778fdemo', 
                                    vout_n = 0, 
                                    address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE', 
                                    value = '0.5', )
                                ], 
                            raw_tx = '0xa22cb4650000000000000000000000001e0049783f008a0085193e00003d00cd54003c71000000000000000000000000000000000000000000000000000000000000DEMO', ), 
                        replacement = cobo_waas2.models.transaction_replacement.Transaction_replacement(
                            replaced_by_type = 'Resend', 
                            replaced_by_transaction_id = 'aff0e1cb-15b2-4e1f-9b9d-a9133715986f', 
                            replaced_by_transaction_hash = '239861be9a4afe080c359b7fe4a1d035945ec46256b1a0f44d1267c71de8ec28', 
                            replaced_type = 'Resend', 
                            replaced_transaction_id = 'aff0e1cb-15b2-4e1f-9b9d-a9133715986f', 
                            replaced_transaction_hash = '239861be9a4afe080c359b7fe4a1d035945ec46256b1a0f44d1267c71de8ec28', ), 
                        category = [
                            'Payment'
                            ], 
                        description = 'withdrawal to exchange trading account', 
                        is_loop = False, 
                        created_timestamp = 1610445878970, 
                        updated_timestamp = 1610445878970, )
                    ],
                pagination = cobo_waas2.models.pagination.Pagination(
                    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1', 
                    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk', 
                    total_count = 10000, )
            )
        else:
            return ListTransactions200Response(
        )
        """

    def testListTransactions200Response(self):
        """Test ListTransactions200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
