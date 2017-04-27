# RangeDataResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | [**RangeData**](RangeData.md) |  | [optional] [default to null]
**Message** | **string** | Human readable descriptions of the response condition | [optional] [default to null]
**NextUrl** | **string** | A fully qualified URL, including required query parameters, for the  next page of results. If there is no next page to query for, this will  be empty.  | [optional] [default to null]
**Page** | **int32** | The one based page index that the result corresponds to. Only included during paging.  | [optional] [default to null]
**PagedRegion** | **string** | The entire region that the collection of pages represents. Only included during data paging.  | [optional] [default to null]
**PerPage** | **int32** | The maximum number of items in a page. A page is not guaranteed to have exactly this many items. Only included during paging.  | [optional] [default to null]
**RequestId** | **string** | A unique identifier for the request | [optional] [default to null]
**Revision** | **int32** | The revision number of this spreadsheet | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


