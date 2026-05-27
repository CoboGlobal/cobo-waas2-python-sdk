# SatoshiTestChallengeStatus

The lifecycle status of a Satoshi Test challenge. - `PREPARE`: Challenge created (address and amount returned); the 180-minute countdown is not started yet. - `PENDING`: Challenge submitted; countdown active, waiting for the counterparty's on-chain transfer. - `MATCHED`: An on-chain transfer matching the expected amount has been observed; waiting for block confirmations. - `VERIFIED`: The matched transfer reached confirmation — the address is verified. - `EXPIRED`: Challenge was not matched within 180 minutes. - `DELETED`: Challenge was cancelled by the client. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


