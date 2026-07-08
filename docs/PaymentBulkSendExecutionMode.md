# PaymentBulkSendExecutionMode

The execution mode of the bulk send. - `Strict`: The bulk send is executed in strict mode. All-or-nothing is enforced at the validation stage: if any item fails validation, the entire batch is rejected and no items are sent. Note that this all-or-nothing guarantee applies at validation only, not at execution. After validation passes, individual items may still be rejected by risk control or fail during on-chain execution, which can result in a `PartiallyCompleted` bulk send status. - `Partial`: The bulk send is executed in partial mode, which means some bulk send items can be successfully executed and some can be failed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


