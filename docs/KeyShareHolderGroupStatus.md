# KeyShareHolderGroupStatus

The status of the key share holder group. Possible values include: - `New`: The key share holder group has been newly created. The status will become `Valid` after you call [Create TSS request](https://www.cobo.com/developers/v2/api-references/wallets--mpc-wallets/create-tss-request) and specifying this key share holder group as the target key share holder group.  - `Valid`: The key share holder group is valid.  - `Unavailable`: The key share holder group is currently unavailable. This status appears when a key share holder uses [mobile co-signer](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/back-up-key-share-groups#mobile-co-signer) to change node. For example, when a key share holder changes to a new phone or loses their phone, and is in the process of setting up [Cobo Guard](https://manuals.cobo.com/en/guard/introduction) on their new phone. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


