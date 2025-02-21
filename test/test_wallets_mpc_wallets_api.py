# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2 import Configuration
from cobo_waas2.api.wallets_mpc_wallets_api import WalletsMPCWalletsApi


class TestWalletsMPCWalletsApi(unittest.TestCase):
    """WalletsMPCWalletsApi unit test stubs"""

    def setUp(self) -> None:
        Configuration.set_default(Configuration(
            api_private_key="c203fccc02a2269ec486d9c32ff74b5ba6ab0cdb461ee1fb0dfc616109115c06",
            host="https://api.sandbox.cobo.com/v2"
        ))
        self.api = WalletsMPCWalletsApi()

    def tearDown(self) -> None:
        pass

    def test_cancel_tss_request_by_id(self) -> None:
        """
        Test case for cancel_tss_request_by_id

        Cancel TSS request
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        tss_request_id = '20240711114129000132315000003970'

        api_response = self.api.cancel_tss_request_by_id(vault_id, tss_request_id)
        """

    def test_create_key_share_holder_group(self) -> None:
        """
        Test case for create_key_share_holder_group

        Create key share holder group
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        create_key_share_holder_group_request = cobo_waas2.CreateKeyShareHolderGroupRequest()

        api_response = self.api.create_key_share_holder_group(vault_id, create_key_share_holder_group_request=create_key_share_holder_group_request)
        """

    def test_create_mpc_project(self) -> None:
        """
        Test case for create_mpc_project

        Create project
        """
        """
        create_mpc_project_request = cobo_waas2.CreateMpcProjectRequest()

        api_response = self.api.create_mpc_project(create_mpc_project_request=create_mpc_project_request)
        """

    def test_create_mpc_vault(self) -> None:
        """
        Test case for create_mpc_vault

        Create vault
        """
        """
        create_mpc_vault_request = cobo_waas2.CreateMpcVaultRequest()

        api_response = self.api.create_mpc_vault(create_mpc_vault_request=create_mpc_vault_request)
        """

    def test_create_tss_request(self) -> None:
        """
        Test case for create_tss_request

        Create TSS request
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        create_tss_request_request = cobo_waas2.CreateTssRequestRequest()

        api_response = self.api.create_tss_request(vault_id, create_tss_request_request=create_tss_request_request)
        """

    def test_delete_key_share_holder_group_by_id(self) -> None:
        """
        Test case for delete_key_share_holder_group_by_id

        Delete key share holder group
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        key_share_holder_group_id = 'e8257ac8-76b8-4d1e-a1f9-eec4cb931dce'

        api_response = self.api.delete_key_share_holder_group_by_id(vault_id, key_share_holder_group_id)
        """

    def test_get_key_share_holder_by_tss_node_id(self) -> None:
        """
        Test case for get_key_share_holder_by_tss_node_id

        Get key share holder by tss node id
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        tss_node_id = 'coboBTGDvjJG99pABegvPYmavrcTU3SkjTLHVdsko8dWBga4w'

        api_response = self.api.get_key_share_holder_by_tss_node_id(vault_id, tss_node_id)
        """

    def test_get_key_share_holder_group_by_id(self) -> None:
        """
        Test case for get_key_share_holder_group_by_id

        Get key share holder group information
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        key_share_holder_group_id = 'e8257ac8-76b8-4d1e-a1f9-eec4cb931dce'

        api_response = self.api.get_key_share_holder_group_by_id(vault_id, key_share_holder_group_id)
        """

    def test_get_mpc_project_by_id(self) -> None:
        """
        Test case for get_mpc_project_by_id

        Get project information
        """
        """
        project_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

        api_response = self.api.get_mpc_project_by_id(project_id)
        """

    def test_get_mpc_vault_by_id(self) -> None:
        """
        Test case for get_mpc_vault_by_id

        Get vault information
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

        api_response = self.api.get_mpc_vault_by_id(vault_id)
        """

    def test_get_tss_request_by_id(self) -> None:
        """
        Test case for get_tss_request_by_id

        Get TSS request
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        tss_request_id = '20240711114129000132315000003970'

        api_response = self.api.get_tss_request_by_id(vault_id, tss_request_id)
        """

    def test_list_cobo_key_holders(self) -> None:
        """
        Test case for list_cobo_key_holders

        List all Cobo key share holders
        """
        """

        api_response = self.api.list_cobo_key_holders()
        """

    def test_list_key_share_holder_groups(self) -> None:
        """
        Test case for list_key_share_holder_groups

        List all key share holder groups
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        key_share_holder_group_type = cobo_waas2.KeyShareHolderGroupType()
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_key_share_holder_groups(vault_id, key_share_holder_group_type=key_share_holder_group_type, limit=limit, before=before, after=after)
        """

    def test_list_key_share_holders(self) -> None:
        """
        Test case for list_key_share_holders

        List all key share holders
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        key_share_holder_group_ids = 'dc0cac48-9add-4243-9c7a-b8badac8a198,5558bd1b-d221-4e2b-8c29-f6c97d9e6aca'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_key_share_holders(vault_id, key_share_holder_group_ids=key_share_holder_group_ids, limit=limit, before=before, after=after)
        """

    def test_list_mpc_projects(self) -> None:
        """
        Test case for list_mpc_projects

        List all projects
        """
        """
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_mpc_projects(limit=limit, before=before, after=after)
        """

    def test_list_mpc_vaults(self) -> None:
        """
        Test case for list_mpc_vaults

        List all vaults
        """
        """
        vault_type = cobo_waas2.MPCVaultType()
        project_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_mpc_vaults(vault_type, project_id=project_id, limit=limit, before=before, after=after)
        """

    def test_list_tss_requests(self) -> None:
        """
        Test case for list_tss_requests

        List TSS requests
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        key_share_holder_group_id = 'a3a45e99-5a12-444f-867a-ffe0ebb1bb30'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_tss_requests(vault_id, key_share_holder_group_id, limit=limit, before=before, after=after)
        """

    def test_update_key_share_holder_group_by_id(self) -> None:
        """
        Test case for update_key_share_holder_group_by_id

        Update key share holder group
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        key_share_holder_group_id = 'e8257ac8-76b8-4d1e-a1f9-eec4cb931dce'
        update_key_share_holder_group_by_id_request = cobo_waas2.UpdateKeyShareHolderGroupByIdRequest()

        api_response = self.api.update_key_share_holder_group_by_id(vault_id, key_share_holder_group_id, update_key_share_holder_group_by_id_request=update_key_share_holder_group_by_id_request)
        """

    def test_update_mpc_project_by_id(self) -> None:
        """
        Test case for update_mpc_project_by_id

        Update project name
        """
        """
        project_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        update_mpc_project_by_id_request = cobo_waas2.UpdateMpcProjectByIdRequest()

        api_response = self.api.update_mpc_project_by_id(project_id, update_mpc_project_by_id_request=update_mpc_project_by_id_request)
        """

    def test_update_mpc_vault_by_id(self) -> None:
        """
        Test case for update_mpc_vault_by_id

        Update vault name
        """
        """
        vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        update_mpc_vault_by_id_request = cobo_waas2.UpdateMpcVaultByIdRequest()

        api_response = self.api.update_mpc_vault_by_id(vault_id, update_mpc_vault_by_id_request=update_mpc_vault_by_id_request)
        """


if __name__ == '__main__':
    unittest.main()
