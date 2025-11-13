# FeeStationSponsorTransactionDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_fee_amount** | **str** | The total amount used to sponsor the gas fee required for executing the main transaction on behalf of the user. | 
**commission_fee** | **str** | The commission fee charged for sponsoring the gas fee.  | 

## Example

```python
from cobo_waas2.models.fee_station_sponsor_transaction_description import FeeStationSponsorTransactionDescription

# TODO update the JSON string below
json = "{}"
# create an instance of FeeStationSponsorTransactionDescription from a JSON string
fee_station_sponsor_transaction_description_instance = FeeStationSponsorTransactionDescription.from_json(json)
# print the JSON string representation of the object
print(FeeStationSponsorTransactionDescription.to_json())

# convert the object into a dict
fee_station_sponsor_transaction_description_dict = fee_station_sponsor_transaction_description_instance.to_dict()
# create an instance of FeeStationSponsorTransactionDescription from a dict
fee_station_sponsor_transaction_description_from_dict = FeeStationSponsorTransactionDescription.from_dict(fee_station_sponsor_transaction_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


