# ReportDownloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | The temporary URL used to download the payment report. | 

## Example

```python
from cobo_waas2.models.report_download_response import ReportDownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDownloadResponse from a JSON string
report_download_response_instance = ReportDownloadResponse.from_json(json)
# print the JSON string representation of the object
print(ReportDownloadResponse.to_json())

# convert the object into a dict
report_download_response_dict = report_download_response_instance.to_dict()
# create an instance of ReportDownloadResponse from a dict
report_download_response_from_dict = ReportDownloadResponse.from_dict(report_download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


