# ManualTestLogResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 
**id** | **int** |  | [optional] 
**test_case_version_id** | **int** | ID of the Test Case Version | [optional] 
**exe_start_date** | **datetime** | Execution start date | 
**exe_end_date** | **datetime** | Execution end date | 
**note** | **str** | Note | [optional] 
**attachments** | [**list[AttachmentResource]**](AttachmentResource.md) | Test Log attachments | [optional] 
**name** | **str** | Test Run&#39;s name | [optional] 
**planned_exe_time** | **int** |  | [optional] 
**actual_exe_time** | **int** |  | [optional] 
**build_number** | **str** | Jenkins jobs build number | [optional] 
**build_url** | **str** | Jenkins jobs build URL | [optional] 
**properties** | [**list[PropertyResource]**](PropertyResource.md) |  | [optional] 
**status** | [**StatusResource**](StatusResource.md) | Test Log status | 
**result_number** | **int** |  | [optional] 
**test_step_logs** | [**list[TestStepLogResource]**](TestStepLogResource.md) | Arrays of Test Step Log,   With called test steps, the \&quot;called_test_case_id\&quot; and \&quot;parent_test_step_id\&quot; must be included in request body. | [optional] 
**defects** | [**list[LinkedDefectResource]**](LinkedDefectResource.md) | Array of Defect | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


