# DownloadReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** | The report ID. | 

## Example

```python
from cobo_waas2.models.download_report_request import DownloadReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadReportRequest from a JSON string
download_report_request_instance = DownloadReportRequest.from_json(json)
# print the JSON string representation of the object
print(DownloadReportRequest.to_json())

# convert the object into a dict
download_report_request_dict = download_report_request_instance.to_dict()
# create an instance of DownloadReportRequest from a dict
download_report_request_from_dict = DownloadReportRequest.from_dict(download_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


