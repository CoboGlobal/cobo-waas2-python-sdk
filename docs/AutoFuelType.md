# AutoFuelType

The mode of transaction fee payment using Fee Station. Currently, Fee Station supports transactions made with MPC Wallets on EVM-compatible chains, TRON, and Solana. For more details, refer to [Fee Station](https://manuals.cobo.com/en/portal/fee-station/introduction).  - `ProActiveAutoFuel`: Always use Fee Station to pay transaction fees.   - `PassiveAutoFuel`: Use Fee Station only when the source address balance is insufficient to cover transaction fees.   - `UsePortalPreference`: Use fueling strategy based on the Portal configuration.   - `DisableAutoFuel`: Do not use Fee Station for transaction fee payment under any circumstances.    If this parameter is **not specified**, it defaults to the behavior of `UsePortalPreference`.  **Note**: TRON and Solana does not support `PassiveAutoFuel` due to its fee delegation mechanism. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


