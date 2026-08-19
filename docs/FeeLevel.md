# FeeLevel

The transaction fee level. Specify this property if you want Cobo to calculate the transaction fee for you based on the selected level, instead of providing the fee-related properties yourself. Possible values are: - `Slow`: A lower transaction fee, which may lead to a longer confirmation time. - `Recommended`: The recommended transaction fee, which balances the fee cost and the confirmation time. - `Fast`: A higher transaction fee for a shorter confirmation time.  You can call [Estimate transaction fee](https://www.cobo.com/developers/v2/api-references/transactions/estimate-transaction-fee) to view the estimated transaction fee of each fee level.  <Note>You cannot specify both `fee_level` and `fee` in the same request. If you specify both, the request fails.</Note>  <Note>This property does not take effect in the following cases, and the transaction fee is determined by Cobo: - The transaction uses the fixed fee model. For more information about the fee models, refer to [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models). - The transaction is initiated from Custodial Wallets (Asset Wallets) or Exchange Wallets. </Note> 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


