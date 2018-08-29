from collections import OrderedDict
from sqlalchemy import func, cast, Date

from dataactcore.models.stagingModels import PublishedAwardFinancialAssistance, AwardFinancialAssistance

file_model = PublishedAwardFinancialAssistance
staging_model = AwardFinancialAssistance

mapping = OrderedDict([
    ('fain', 'fain'),
    ('awardmodificationamendmentnumber', 'award_modification_amendme'),
    ('uri', 'uri'),
    ('sai_number', 'sai_number'),
    ('totalfundingamount', 'total_funding_amount'),
    ('federalactionobligation', 'federal_action_obligation'),
    ('nonfederalfundingamount', 'non_federal_funding_amount'),
    ('facevalueofdirectloanorloanguarantee', 'face_value_loan_guarantee'),
    ('originalloansubsidycost', 'original_loan_subsidy_cost'),
    ('actiondate', 'action_date'),
    ('periodofperformancestartdate', 'period_of_performance_star'),
    ('periodofperformancecurrentenddate', 'period_of_performance_curr'),
    ('awardingagencycode', 'awarding_agency_code'),
    ('awardingagencyname', 'awarding_agency_name'),
    ('awardingsubtieragencycode', 'awarding_sub_tier_agency_c'),
    ('awardingsubtieragencyname', 'awarding_sub_tier_agency_n'),
    ('awardingofficecode', 'awarding_office_code'),
    ('awardingofficename', 'awarding_office_name'),
    ('fundingagencycode', 'funding_agency_code'),
    ('fundingagencyname', 'funding_agency_name'),
    ('fundingsubtieragencycode', 'funding_sub_tier_agency_co'),
    ('fundingsubtieragencyname', 'funding_sub_tier_agency_na'),
    ('fundingofficecode', 'funding_office_code'),
    ('fundingofficename', 'funding_office_name'),
    ('awardeeorrecipientuniqueidentifier', 'awardee_or_recipient_uniqu'),
    ('awardeeorrecipientlegalentityname', 'awardee_or_recipient_legal'),
    ('ultimateparentuniqueidentifier', 'ultimate_parent_unique_ide'),
    ('ultimateparentlegalentityname', 'ultimate_parent_legal_enti'),
    ('legalentitycountrycode', 'legal_entity_country_code'),
    ('legalentitycountryname', 'legal_entity_country_name'),
    ('legalentityaddressline1', 'legal_entity_address_line1'),
    ('legalentityaddressline2', 'legal_entity_address_line2'),
    ('legalentitycitycode', 'legal_entity_city_code'),
    ('legalentitycityname', 'legal_entity_city_name'),
    ('legalentitystatecode', 'legal_entity_state_code'),
    ('legalentitystatename', 'legal_entity_state_name'),
    ('legalentityzip5', 'legal_entity_zip5'),
    ('legalentityziplast4', 'legal_entity_zip_last4'),
    ('legalentitycountycode', 'legal_entity_county_code'),
    ('legalentitycountyname', 'legal_entity_county_name'),
    ('legalentitycongressionaldistrict', 'legal_entity_congressional'),
    ('legalentityforeigncityname', 'legal_entity_foreign_city'),
    ('legalentityforeignprovincename', 'legal_entity_foreign_provi'),
    ('legalentityforeignpostalcode', 'legal_entity_foreign_posta'),
    ('primaryplaceofperformancecode', 'place_of_performance_code'),
    ('primaryplaceofperformancecityname', 'place_of_performance_city'),
    ('primaryplaceofperformancecountycode', 'place_of_perform_county_co'),
    ('primaryplaceofperformancecountyname', 'place_of_perform_county_na'),
    ('primaryplaceofperformancestatename', 'place_of_perform_state_nam'),
    ('primaryplaceofperformancezip+4', 'place_of_performance_zip4a'),
    ('primaryplaceofperformancecongressionaldistrict', 'place_of_performance_congr'),
    ('primaryplaceofperformancecountrycode', 'place_of_perform_country_c'),
    ('primaryplaceofperformancecountryname', 'place_of_perform_country_n'),
    ('primaryplaceofperformanceforeignlocationdescription', 'place_of_performance_forei'),
    ('cfda_number', 'cfda_number'),
    ('cfda_title', 'cfda_title'),
    ('assistancetype', 'assistance_type'),
    ('assistancetypedescription', 'assistance_type_desc'),
    ('awarddescription', 'award_description'),
    ('businessfundsindicator', 'business_funds_indicator'),
    ('businessfundsindicatordescription', 'business_funds_ind_desc'),
    ('businesstypes', 'business_types'),
    ('businesstypesdescription', 'business_types_desc'),
    ('correctiondeleteindicator', 'correction_delete_indicatr'),
    ('correctiondeleteindicatordescription', 'correction_delete_ind_desc'),
    ('actiontype', 'action_type'),
    ('actiontypedescription', 'action_type_description'),
    ('recordtype', 'record_type'),
    ('recordtypedescription', 'record_type_description'),
    ('lastmodifieddate', 'modified_at')
])
db_columns = [val for key, val in mapping.items()]


def query_data(session, agency_code, agency_type, start, end, page_start, page_stop):
    """ Request D2 file data

        Args:
            session: DB session
            agency_code: FREC or CGAC code for generation
            agency_type: The type of agency (awarding or funding) to generate the file for
            start: Beginning of period for D file
            end: End of period for D file
            page_start: Beginning of pagination
            page_stop: End of pagination

        Returns:
            The rows using the provided dates and page size for the given agency.
    """
    rows = initial_query(session).\
        filter(file_model.is_active.is_(True)).\
        filter(func.cast_as_date(file_model.action_date) >= start).\
        filter(func.cast_as_date(file_model.action_date) <= end)

    # Funding or awarding agency filtering
    if agency_type == 'funding':
        rows = rows.filter(file_model.funding_agency_code == agency_code)
    else:
        rows = rows.filter(file_model.awarding_agency_code == agency_code)

    # Slice the final query
    rows = rows.slice(page_start, page_stop)

    return rows


def query_published_fabs_data(session, submission_id, page_start, page_stop):
    """ Request published FABS file data

        Args:
            session: DB session
            submission_id: Submission ID for generation
            page_start: Beginning of pagination
            page_stop: End of pagination

        Returns:
            A query to gather published data from the provided submission with the provided slice
    """
    return initial_query(session).filter(file_model.submission_id == submission_id).slice(page_start, page_stop)


def initial_query(session):
    """ Creates the initial query for D2 files.

        Args:
            session: The current DB session

        Returns:
            The base query (a select from the PublishedAwardFinancialAssistance table with the specified columns).
    """
    return session.query(
        file_model.fain,
        file_model.award_modification_amendme,
        file_model.uri,
        file_model.sai_number,
        file_model.total_funding_amount,
        file_model.federal_action_obligation,
        file_model.non_federal_funding_amount,
        file_model.face_value_loan_guarantee,
        file_model.original_loan_subsidy_cost,
        func.to_char(cast(file_model.action_date, Date), 'YYYYMMDD'),
        func.to_char(cast(file_model.period_of_performance_star, Date), 'YYYYMMDD'),
        func.to_char(cast(file_model.period_of_performance_curr, Date), 'YYYYMMDD'),
        file_model.awarding_agency_code,
        file_model.awarding_agency_name,
        file_model.awarding_sub_tier_agency_c,
        file_model.awarding_sub_tier_agency_n,
        file_model.awarding_office_code,
        file_model.awarding_office_name,
        file_model.funding_agency_code,
        file_model.funding_agency_name,
        file_model.funding_sub_tier_agency_co,
        file_model.funding_sub_tier_agency_na,
        file_model.funding_office_code,
        file_model.funding_office_name,
        file_model.awardee_or_recipient_uniqu,
        file_model.awardee_or_recipient_legal,
        file_model.ultimate_parent_unique_ide,
        file_model.ultimate_parent_legal_enti,
        file_model.legal_entity_country_code,
        file_model.legal_entity_country_name,
        file_model.legal_entity_address_line1,
        file_model.legal_entity_address_line2,
        file_model.legal_entity_city_code,
        file_model.legal_entity_city_name,
        file_model.legal_entity_state_code,
        file_model.legal_entity_state_name,
        file_model.legal_entity_zip5,
        file_model.legal_entity_zip_last4,
        file_model.legal_entity_county_code,
        file_model.legal_entity_county_name,
        file_model.legal_entity_congressional,
        file_model.legal_entity_foreign_city,
        file_model.legal_entity_foreign_provi,
        file_model.legal_entity_foreign_posta,
        file_model.place_of_performance_code,
        file_model.place_of_performance_city,
        file_model.place_of_perform_county_co,
        file_model.place_of_perform_county_na,
        file_model.place_of_perform_state_nam,
        file_model.place_of_performance_zip4a,
        file_model.place_of_performance_congr,
        file_model.place_of_perform_country_c,
        file_model.place_of_perform_country_n,
        file_model.place_of_performance_forei,
        file_model.cfda_number,
        file_model.cfda_title,
        file_model.assistance_type,
        file_model.assistance_type_desc,
        file_model.award_description,
        file_model.business_funds_indicator,
        file_model.business_funds_ind_desc,
        file_model.business_types,
        file_model.business_types_desc,
        file_model.correction_delete_indicatr,
        file_model.correction_delete_ind_desc,
        file_model.action_type,
        file_model.action_type_description,
        file_model.record_type,
        file_model.record_type_description,
        func.to_char(cast(file_model.modified_at, Date), 'YYYYMMDD'))
