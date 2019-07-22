import schematics_to_swagger

from tests import models


WEATHER_REPORT_DEFINITION = {
    'title': 'WeatherReport',
    'type': 'object',
    'description': 'Some sample class for Weather report',
    'properties': {
        'city': {
            'type': 'string',
            'maxLength': 50
        },
        'temperature': {
            'type': 'number',
            'format': 'double',
            'required': True
        },
        'taken_at': {
            'type': 'string',
            'format': 'date-time'
        }
    }
}


def test_model_to_definition():
    expected = WEATHER_REPORT_DEFINITION
    definition = schematics_to_swagger.model_to_definition(models.WeatherReport)
    assert expected == definition


def test_read_models_from_module():
    expected = {
        'WeatherReport': WEATHER_REPORT_DEFINITION
    }
    data = schematics_to_swagger.read_models_from_module(models)
    assert expected == data
