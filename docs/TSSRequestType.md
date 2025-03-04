# TSSRequestType

The TSS request type. Possible values include: - `KeyGen`: This is a key generation request to create a [root extended public key](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/tss-node-deployment#tss-node-on-cobo-portal-and-mpc-root-extended-public-key) and key shares for your [Main Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups) after you've created the Main Group with [Create key share holder group](https://www.cobo.com/developers/v2/api-references/wallets--mpc-wallets/create-key-share-holder-group). You only need to do this once per [organization](https://manuals.cobo.com/en/portal/organization/introduction).  - `KeyGenFromKeyGroup`: This is a request to use the [Main Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups) to create key shares for your [Signing Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups) or [Recovery Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups) after you've created these key share holder groups with [Create key share holder group](https://www.cobo.com/developers/v2/api-references/wallets--mpc-wallets/create-key-share-holder-group).  - `Recovery`: This is a request to create key shares using the [Recovery Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups) for a key share holder in the [Main Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups) if their key share has been lost (e.g. by losing their phone). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


