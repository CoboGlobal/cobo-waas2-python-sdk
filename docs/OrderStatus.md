# OrderStatus

The current status of the pay-in order: - `Pending`: The order has been created and is awaiting payment. No incoming transaction has been detected. - `Processing`: An incoming transaction has been detected at the recipient address. - `Completed`: The payment has been fully received and is now complete. - `Expired`: The order has reached its expiration time without receiving any payment, or the order has been cancelled by the [Update pay-in order](https://www.cobo.com/payments/en/api-references/payment/update-pay-in-order) operation. - `Underpaid`: The order has reached its expiration time. A payment was received but the amount is less than the order's required amount. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


