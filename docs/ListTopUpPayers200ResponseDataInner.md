# ListTopUpPayers200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. | 
**payer_id** | **str** | A unique identifier assigned by Cobo to track and identify individual payers. | 
**developer_fee_rate** | **str** | The developer fee rate applied to top-up transactions made by this payer. Expressed as a decimal string where \&quot;0.1\&quot; represents 10%. | 
**created_timestamp** | **int** | The creation time of the payer, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The last update time of the payer, represented as a UNIX timestamp in seconds. | [optional] 
**transactions** | [**List[PaymentTransaction]**](PaymentTransaction.md) | An array of top-up transactions associated with this payer. | [optional] 

## Example

```python
from cobo_waas2.models.list_top_up_payers200_response_data_inner import ListTopUpPayers200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTopUpPayers200ResponseDataInner from a JSON string
list_top_up_payers200_response_data_inner_instance = ListTopUpPayers200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListTopUpPayers200ResponseDataInner.to_json())

# convert the object into a dict
list_top_up_payers200_response_data_inner_dict = list_top_up_payers200_response_data_inner_instance.to_dict()
# create an instance of ListTopUpPayers200ResponseDataInner from a dict
list_top_up_payers200_response_data_inner_from_dict = ListTopUpPayers200ResponseDataInner.from_dict(list_top_up_payers200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


