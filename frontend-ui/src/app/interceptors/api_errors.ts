// This file contains all documented backend api errors with corresponding user messages
export let api_supported_errors: any = {
    "InvalidPayloadError": "Sorry,the data uploaded is invalid / malformed",
    "UserDoesNotExist": "Sorry,the user does not exist in the system",
    "PermissionDeniedError": "You are not allowed to perform this action",
    "FileUploadError": "Sorry, an error occurred while uploading the resource.If this persists, please contact the system administrator",
    "InvalidFileError": "Sorry,the file uploaded is invalid",
    "UnsupportedFileFormatError": "Sorry,the file format uploaded is unsupported.Kindly use valid xml files",
    "NoFilesforUploadError": "Kindly select a file to upload",
    "FileDoesNotExistError": "Sorry, the file does not exist in the system",
    "SystemError": "Sorry, an error occurred.Please try again.If this persists,please contact the system administrator",
};