# PayoutDestinationDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The destination address. | 
**amount** | **str** | The amount of cryptocurrency to send to the destination. | 
**email** | **str** | The email of the destination. | [optional] 
**note** | **str** | The note of the destination. | [optional] 
**loop_enabled** | **bool** | Enable loop mode for standard transfers when source is asset wallet. Only applicable when: - &#x60;payout_mode&#x60; is &#x60;Normal&#x60; - &#x60;source_type&#x60; is asset wallet  | [optional] [default to False]
**network_fee** | [**PayoutFeeData**](PayoutFeeData.md) |  | [optional] 
**status** | [**PayoutTransactionStatus**](PayoutTransactionStatus.md) |  | [optional] 
**transaction_id** | **str** | The transaction ID of the destination. | [optional] 

## Example

```python
from cobo_waas2.models.payout_destination_detail import PayoutDestinationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutDestinationDetail from a JSON string
payout_destination_detail_instance = PayoutDestinationDetail.from_json(json)
# print the JSON string representation of the object
print(PayoutDestinationDetail.to_json())

# convert the object into a dict
payout_destination_detail_dict = payout_destination_detail_instance.to_dict()
# create an instance of PayoutDestinationDetail from a dict
payout_destination_detail_from_dict = PayoutDestinationDetail.from_dict(payout_destination_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


