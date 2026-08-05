# PaymentBulkSendExecutionMode

Specifies how the batch handles item-level validation failures. The required `execution_mode` field is a string enum and must be set to either `Strict` or `Partial`; no default is applied if you omit it. It is not a `strict_mode` boolean flag.  - `Strict`: If any item in the batch fails validation, no items are executed.   Every item is marked `NotExecuted`, and the batch fails. The batch also   fails in `Strict` mode if the fund sweep needed to fund it only partially   completes. - `Partial`: Item validation failures are isolated to the affected items.   Failed items are marked `NotExecuted`, while all other validated items in   the batch continue to be processed normally.  Use `Partial` when one item's validation failure should not block the rest of the batch. Because outcomes can differ by item, check each item's result and `validation_status` individually instead of assuming that a batch-level outcome applies to every item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


