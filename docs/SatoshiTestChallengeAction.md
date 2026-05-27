# SatoshiTestChallengeAction

The action to perform when creating a Satoshi Test challenge. - `PREPARE`: Preview the verification address and amount. The 180-minute countdown is NOT started yet. Repeated `PREPARE` calls for the same `(chain_id, from_address)` refresh the amount. - `SUBMIT`: Activate the challenge and start the 180-minute countdown. If a `PREPARE` challenge already exists for this `(chain_id, from_address)` it is activated; otherwise a new challenge is created directly in `PENDING` state (one-shot flow). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


