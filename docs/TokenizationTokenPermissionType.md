# TokenizationTokenPermissionType

The type of permission for token operations. Each permission grants specific capabilities:  - `ManagePermissions`: Ability to grant and revoke permissions to addresses.  - `ManageAccessAndControls`: Ability to manage access control mechanisms including allowlist and blocklist operations.  - `MintTokens`: Ability to mint tokens and increase the total supply.  - `BurnTokens`: Ability to burn tokens and decrease the total supply.  - `RecoverTokens`: Ability to recover tokens from specified addresses.  - `UpgradeContract`: Ability to upgrade the smart contract implementation.  - `PauseContract`: Ability to pause and unpause the contract.  - `FreezeAccounts`: Ability to freeze and unfreeze addresses.  - `UpdateMetadata`: Ability to update token metadata.  - `WrapTokens`: Ability to wrap and unwrap tokens for wrapped token implementations.  - `PermanentDelegate`: An immutable delegate authority that cannot be changed once set. Has unlimited control over all token accounts including transfer and burn operations.  Supported permissions by chain: - **EVM (CoboERC20)**: ManagePermissions, ManageAccessAndControls, MintTokens, BurnTokens, RecoverTokens, UpgradeContract, PauseContract - **EVM (CoboERC20Wrapper)**: ManagePermissions, ManageAccessAndControls, MintTokens, WrapTokens, RecoverTokens, UpgradeContract, PauseContract - **Solana (SPL Token 2022)**: MintTokens, PauseContract, FreezeAccounts, UpdateMetadata, PermanentDelegate 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


