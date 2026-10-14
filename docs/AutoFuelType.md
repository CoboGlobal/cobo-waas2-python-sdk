# AutoFuelType

Whether Billing Center pays the on-chain transaction fee for this transaction, and under what condition.  On-chain fees are charged in a chain's gas token, which is usually not the token you are sending. Without Billing Center, the source address must hold that gas token or the transaction fails. When Billing Center covers the fee, the source address does not need to hold any gas token.  For more details, refer to [Billing Center](https://manuals.cobo.com/en/portal/billing-center/introduction).  **Accepted values**  - `ProActiveAutoFuel`: Always have Billing Center pay the fee, without touching the gas token in the source address. - `PassiveAutoFuel`: Use the gas token in the source address when it is sufficient; otherwise have Billing Center pay the fee. - `UsePortalPreference`: Follow the per-chain sponsorship rules configured on Cobo Portal, under **Billing Center** > **Settings**. - `DisableAutoFuel`: Never use Billing Center. The transaction pays its fee from the source address and fails if the balance is insufficient.  If this parameter is **not specified**, it defaults to `UsePortalPreference`.  **Support and limitations**  - Applies to transactions from MPC Wallets and Custodial Wallets (Web3 Wallets) on EVM-compatible chains, TRON, Solana, and Tempo. Other chains, such as BTC, are not supported, and the source address must hold the fee itself. - TRON, Solana, and Tempo do not support `PassiveAutoFuel` due to their fee delegation mechanisms. - The per-chain sponsorship rules on Cobo Portal apply only to API transactions that pass `UsePortalPreference`. They do not affect transfers initiated from the Cobo Portal interface. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


