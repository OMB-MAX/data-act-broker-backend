from tests.unit.dataactcore.factories.staging import DetachedAwardFinancialAssistanceFactory
from tests.unit.dataactvalidator.utils import number_of_errors, query_columns
from tests.unit.dataactcore.factories.domain import StateCongressionalFactory

_FILE = 'fabs43_detached_award_financial_assistance_4'


def test_column_headers(database):
    expected_subset = {'row_number', 'place_of_performance_code', 'place_of_performance_congr',
                       'uniqueid_afa_generated_unique'}
    actual = set(query_columns(_FILE, database))
    assert expected_subset == actual


def test_success(database):
    """ Test PrimaryPlaceOfPerformanceCongressionalDistrict exists in the state indicated by the
        PrimaryPlaceOfPerformanceCode or is 90 in a state with multiple districts or when PrimaryPlaceOfPerformanceCode
        is 00*****. Districts that were created under the 2000 census or later are considered valid. This rule is
        ignored when PrimaryPlaceOfPerformanceCode is blank.
    """
    state_congr_1 = StateCongressionalFactory(congressional_district_no='01', state_code='NY', census_year=None)
    state_congr_2 = StateCongressionalFactory(congressional_district_no='02', state_code='NY', census_year=None)
    state_congr_3 = StateCongressionalFactory(congressional_district_no='03', state_code='NY', census_year=2000)

    det_award_1 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='NY12345',
                                                          place_of_performance_congr='01',
                                                          correction_delete_indicatr='')
    det_award_2 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='ny*****',
                                                          place_of_performance_congr='02',
                                                          correction_delete_indicatr=None)
    det_award_3 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='Ny12345',
                                                          place_of_performance_congr='03',
                                                          correction_delete_indicatr='c')
    det_award_4 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='Ny12345',
                                                          place_of_performance_congr='90',
                                                          correction_delete_indicatr='C')
    det_award_5 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='00*****',
                                                          place_of_performance_congr='90',
                                                          correction_delete_indicatr='')
    det_award_6 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='NY12345',
                                                          place_of_performance_congr='',
                                                          correction_delete_indicatr='')
    det_award_7 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='Ny12345',
                                                          place_of_performance_congr='',
                                                          correction_delete_indicatr='')
    det_award_8 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='Ny12345',
                                                          place_of_performance_congr=None,
                                                          correction_delete_indicatr='')
    # Test ignoring blank/empty string ppop codes
    det_award_9 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='',
                                                          place_of_performance_congr='03',
                                                          correction_delete_indicatr='')
    det_award_10 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code=None,
                                                           place_of_performance_congr='03',
                                                           correction_delete_indicatr='')
    # Ignore correction delete indicator of D
    det_award_11 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='nY12345',
                                                           place_of_performance_congr='09',
                                                           correction_delete_indicatr='d')

    errors = number_of_errors(_FILE, database, models=[det_award_1, det_award_2, det_award_3, det_award_4, det_award_5,
                                                       det_award_6, det_award_7, det_award_8, det_award_9, det_award_10,
                                                       det_award_11, state_congr_1, state_congr_2, state_congr_3])
    assert errors == 0


def test_failure(database):
    """ Test failure PrimaryPlaceOfPerformanceCongressionalDistrict exists in the state indicated by the
        PrimaryPlaceOfPerformanceCode or is 90 in a state with multiple districts or when PrimaryPlaceOfPerformanceCode
        is 00*****. Districts that were created under the 2000 census or later are considered valid.
    """
    state_congr_1 = StateCongressionalFactory(congressional_district_no='01', state_code='NY', census_year=None)
    state_congr_2 = StateCongressionalFactory(congressional_district_no='02', state_code='NY', census_year=None)
    state_congr_3 = StateCongressionalFactory(congressional_district_no='01', state_code='PA', census_year=None)
    state_congr_4 = StateCongressionalFactory(congressional_district_no='03', state_code='NJ', census_year=1999)

    det_award_1 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='nY12345',
                                                          place_of_performance_congr='03',
                                                          correction_delete_indicatr='')
    det_award_2 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='PA12345',
                                                          place_of_performance_congr='02',
                                                          correction_delete_indicatr=None)
    det_award_3 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='PA**345',
                                                          place_of_performance_congr='90',
                                                          correction_delete_indicatr='c')
    det_award_4 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='00*****',
                                                          place_of_performance_congr='01',
                                                          correction_delete_indicatr='C')
    det_award_5 = DetachedAwardFinancialAssistanceFactory(place_of_performance_code='NJ12345',
                                                          place_of_performance_congr='03',
                                                          correction_delete_indicatr='')

    errors = number_of_errors(_FILE, database, models=[det_award_1, det_award_2, det_award_3, det_award_4, det_award_5,
                                                       state_congr_1, state_congr_2, state_congr_3,
                                                       state_congr_4])
    assert errors == 5
