# TransactionStellarDestination

The information about the transaction destination type `STELLAR_Contract`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**contract_param** | [**TransactionStellarContractParam**](TransactionStellarContractParam.md) |  | 

## Example

```python
from cobo_waas2.models.transaction_stellar_destination import TransactionStellarDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionStellarDestination from a JSON string
transaction_stellar_destination_instance = TransactionStellarDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionStellarDestination.to_json())

# convert the object into a dict
transaction_stellar_destination_dict = transaction_stellar_destination_instance.to_dict()
# create an instance of TransactionStellarDestination from a dict
transaction_stellar_destination_from_dict = TransactionStellarDestination.from_dict(transaction_stellar_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


