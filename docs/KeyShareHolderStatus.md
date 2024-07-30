# KeyShareHolderStatus

The status of key share holder's TSS Node. Possible values include: - `Valid`: The TSS Node is configured and activated.  - `NotConfigured`: The TSS Node has not been configured. This status is only applicable to [mobile co-signer](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/back-up-key-share-groups#mobile-co-signer) using the [Cobo Guard](https://manuals.cobo.com/en/guard/introduction).  - `NotActivated`: The TSS Node has not been activated. This status is only applicable to [mobile co-signer](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/back-up-key-share-groups#mobile-co-signer) using the [Cobo Guard](https://manuals.cobo.com/en/guard/introduction).  - `Changed`: The TSS Node has been changed. This happens when the key share holder sets up their [Cobo Guard](https://manuals.cobo.com/en/guard/introduction) on a new phone. This `Changed` status serves as a reminder for you to call [Create TSS request](/api-references/v2/wallets--mpc-wallet/create-a-tss-request-to-generate-key-secrets-for-a-tss-group) with the `KeyGenFromKeyGroup` and `Recovery` action `type` to finalize the setup of the key share holder's new phone. Once all set, the old TSS Node with the `Changed` status will be deleted. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


