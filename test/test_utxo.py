# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.utxo import UTXO


class TestUTXO(unittest.TestCase):
    """UTXO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UTXO:
        """Test UTXO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UTXO`
        """
        model = UTXO()
        if include_optional:
            return UTXO(
                tx_hash = 'dd7e1cecf6bbde1844ee1815b780711a1e306a718bcd23cd64401b48ef88eb83',
                vout_n = 0,
                address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE',
                token_id = 'BTC',
                value = '0.5',
                is_coinbase = False,
                is_locked = False,
                confirmed_number = 66716
            )
        else:
            return UTXO(
        )
        """

    def testUTXO(self):
        """Test UTXO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
