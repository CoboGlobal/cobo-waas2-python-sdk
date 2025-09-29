# AutoFuelType

The mode of transaction fee payment using Fee Station. Currently, Fee Station supports EVM-compatible and TRON transactions initiated from MPC Wallets (Organization-Controlled). For more details, refer to [Fee Station](https://manuals.cobo.com/en/portal/fee-station/introduction). - `ProActiveAutoFuel`: Always use Fee Station to pay transaction fees. - `PassiveAutoFuel`: Use Fee Station only when the source address balance is insufficient to cover the transaction fees. - `UsePortalPreference`: Use fueling strategy based on Portal configuration.  Please note that the TRON chain does not support `PassiveAutoFuel` due to its fee delegation mechanism. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


