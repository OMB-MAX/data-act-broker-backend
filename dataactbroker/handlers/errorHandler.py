from sqlalchemy.orm import joinedload

from dataactcore.models.errorModels import File, ErrorMetadata
from dataactcore.models.errorInterface import ErrorInterface
from dataactcore.models.lookups import FILE_TYPE_DICT_ID

from dataactcore.models.lookups import FILE_STATUS_DICT

class ErrorHandler(ErrorInterface) :
    """ Manages communication with the error database """

    def getErrorMetricsByJobId (self,jobId, includeFileTypes = False, interfaces = None, severityId = None) :
        """ Get error metrics for specified job, including number of errors for each field name and error type """
        resultList = []

        query = self.session.query(File).options(joinedload("file_status")).filter(File.job_id == jobId)
        queryResult = self.runUniqueQuery(query,"No files for this job", "Conflicting file records for this job")

        if not queryResult.file_status.file_status_id == FILE_STATUS_DICT['complete'] :
            return [{"field_name":"File Level Error","error_name": queryResult.file_status.name,"error_description":str(queryResult.file_status.description),"occurrences":1,"rule_failed":""}]

        queryResult = self.session.query(ErrorMetadata).options(joinedload("error_type")).filter(ErrorMetadata.job_id == jobId).filter(ErrorMetadata.severity_id == severityId).all()
        for result in queryResult:
            recordDict = {"field_name":result.field_name,"error_name": result.error_type.name, "error_description": result.error_type.description, "occurrences": str(result.occurrences), "rule_failed": result.rule_failed, "original_label":result.original_rule_label}
            if includeFileTypes:
                recordDict['source_file'] = FILE_TYPE_DICT_ID.get(result.file_type_id, '')
                recordDict['target_file'] = FILE_TYPE_DICT_ID.get(result.target_file_type_id, '')
            resultList.append(recordDict)
        return resultList
