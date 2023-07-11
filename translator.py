from deep_translator import MyMemoryTranslator

def english_to_french(EngText):
    translator = MyMemoryTranslator(source='en', target='fr')
    FrTranslation = translator.translate(EngText)
    return FrTranslation
