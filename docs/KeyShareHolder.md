# KeyShareHolder

The data for MPC Wallets' key share holder information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The key share holder name. | [optional] 
**type** | [**KeyShareHolderType**](KeyShareHolderType.md) |  | [optional] 
**tss_node_id** | **str** | The key share holder&#39;s TSS Node ID. | [optional] 
**online** | **bool** | Whether the key share holder&#39;s TSS Node is online. - &#x60;true&#x60;: The TSS Node is online.  - &#x60;false&#x60;: The TSS Node is offline.  | [optional] 
**signer** | **bool** | Whether the key share holder&#39;s TSS Node is a designated transaction signer. - &#x60;true&#x60;: The TSS Node is a designated transaction signer.  - &#x60;false&#x60;: The TSS Node is not a designated transaction signer.  | [optional] 
**status** | [**KeyShareHolderStatus**](KeyShareHolderStatus.md) |  | [optional] 
**account_id** | **str** | The key share holder&#39;s Cobo Portal account ID. | [optional] 

## Example

```python
from cobo_waas2.models.key_share_holder import KeyShareHolder

# TODO update the JSON string below
json = "{}"
# create an instance of KeyShareHolder from a JSON string
key_share_holder_instance = KeyShareHolder.from_json(json)
# print the JSON string representation of the object
print(KeyShareHolder.to_json())

# convert the object into a dict
key_share_holder_dict = key_share_holder_instance.to_dict()
# create an instance of KeyShareHolder from a dict
key_share_holder_from_dict = KeyShareHolder.from_dict(key_share_holder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


