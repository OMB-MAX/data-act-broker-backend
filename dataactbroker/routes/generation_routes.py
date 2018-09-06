from flask import request
from webargs import fields as webargs_fields, validate as webargs_validate
from webargs.flaskparser import use_kwargs

from dataactbroker.decorators import convert_to_submission_id
from dataactbroker.handlers.fileHandler import FileHandler
from dataactbroker.permissions import requires_login, requires_submission_perms

DATE_REGEX = '^\d{2}\/\d{2}\/\d{4}$'


def add_generation_routes(app, is_local, server_path):
    """ Create routes related to file generation

        Attributes:
            app: A Flask application
            is_local: A boolean flag indicating whether the application is being run locally or not
            server_path: A string containing the path to the server files (only applicable when run locally)
    """

    @app.route("/v1/generate_file/", methods=["POST"])
    @convert_to_submission_id
    @requires_submission_perms('writer')
    @use_kwargs({
        'file_type': webargs_fields.String(
            required=True,
            validate=webargs_validate.OneOf(('D1', 'D2', 'E', 'F'), error="Must be either D1, D2, E or F")),
        'start': webargs_fields.String(
            validate=webargs_validate.Regexp(DATE_REGEX, error="Must be in the format MM/DD/YYYY")),
        'end': webargs_fields.String(
            validate=webargs_validate.Regexp(DATE_REGEX, error="Must be in the format MM/DD/YYYY")),
        'agency_type': webargs_fields.String(
            missing='awarding',
            validate=webargs_validate.OneOf(('awarding', 'funding'),
                                            error="Must be either awarding or funding if provided")
        )
    })
    def generate_file(submission_id, file_type, start, end, agency_type):
        """ Kick of a file generation, or retrieve the cached version of the file.

            Attributes:
                submission: submission ID for which we're generating the file
                file_type: type of file to generate the job for
                start: the start date for the file to generate
                end: the end date for the file to generate
                agency_type: The type of agency (awarding or funding) to generate the file for
        """
        file_manager = FileHandler(request, is_local=is_local, server_path=server_path)
        return file_manager.generate_file(submission_id, file_type, start, end, agency_type)

    @app.route("/v1/check_generation_status/", methods=["GET"])
    @convert_to_submission_id
    @requires_submission_perms('reader')
    @use_kwargs({'file_type': webargs_fields.String(
        required=True,
        validate=webargs_validate.OneOf(('D1', 'D2', 'E', 'F'), error="Must be either D1, D2, E or F"))
    })
    def check_generation_status(submission, file_type):
        """ Return status of file generation job

            Attributes:
                submission: submission for which we're generating the file
                file_type: type of file to check the status of
        """
        file_manager = FileHandler(request, is_local=is_local, server_path=server_path)
        return file_manager.check_generation(submission, file_type)

    @app.route("/v1/generate_detached_file/", methods=["POST"])
    @requires_login
    @use_kwargs({
        'file_type': webargs_fields.String(required=True, validate=webargs_validate.OneOf(('D1', 'D2'))),
        'cgac_code': webargs_fields.String(),
        'frec_code': webargs_fields.String(),
        'start': webargs_fields.String(required=True),
        'end': webargs_fields.String(required=True),
        'agency_type': webargs_fields.String(
            missing='awarding',
            validate=webargs_validate.OneOf(('awarding', 'funding'),
                                            error="Must be either awarding or funding if provided")
        )
    })
    def generate_detached_file(file_type, cgac_code, frec_code, start, end, agency_type):
        """ Generate a file from external API, independent from a submission

            Attributes:
                file_type: type of file to be generated
                cgac_code: the code of a CGAC agency if generating for a CGAC agency
                frec_code: the code of a FREC agency if generating for a FREC agency
                start: start date in a string, formatted MM/DD/YYYY
                end: end date in a string, formatted MM/DD/YYYY
                agency_type: The type of agency (awarding or funding) to generate the file for
        """
        file_manager = FileHandler(request, is_local=is_local, server_path=server_path)
        return file_manager.generate_detached_file(file_type, cgac_code, frec_code, start, end, agency_type)

    @app.route("/v1/check_detached_generation_status/", methods=["GET"])
    @requires_login
    @use_kwargs({'job_id': webargs_fields.Int(required=True)})
    def check_detached_generation_status(job_id):
        """ Return status of file generation job """
        file_manager = FileHandler(request, is_local=is_local, server_path=server_path)
        return file_manager.check_detached_generation(job_id)
