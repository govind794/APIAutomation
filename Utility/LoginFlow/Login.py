def loginFlow(api_response_body_json):
    license_details = api_response_body_json["response"]
    license_number = license_details['license_number']
    is_license_validated = license_details['is_license_validated']
    print(f'\n license_number: {license_number} \n is_license_validated: {is_license_validated}')
    assert 'MP70N20180008564' == license_number
    assert 1 == is_license_validated


def googleLoginFlow(api_response_body_json):
    license_details = api_response_body_json["response"]
    license_number = license_details['license_number']
    is_license_validated = license_details['is_license_validated']
    print(f'\n license_number: {license_number} \n is_license_validated: {is_license_validated}')
    assert 'MP70N20180008564' == license_number
    assert 1 == is_license_validated
