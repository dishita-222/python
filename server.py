import ibm_watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('<API_KEY>')
translator = ibm_watson.LanguageTranslatorV3(
    version='<VERSION>',
    authenticator=authenticator
)

translator.set_service_url('<SERVICE_URL>')

def englishToFrench(text):
    translation = translator.translate(
        text=text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(text):
    translation = translator.translate(
        text=text,
        source='fr',
        target='en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

def test_englishToFrench():
    assertEqual(englishToFrench('Hello'), 'Bonjour')
    assertNotEqual(englishToFrench('Goodbye'), 'Au revoir')

def test_frenchToEnglish():
    assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    assertNotEqual(frenchToEnglish('Au revoir'), 'Goodbye')

if __name__ == '__main__':
    test_englishToFrench()
    test_frenchToEnglish()
