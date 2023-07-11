from deep_translator import MyMemoryTranslator

def english_to_french(EngText):
    translator = MyMemoryTranslator(source='en', target='fr')
    FrTranslation = translator.translate(EngText)
    return FrTranslation

def french_to_english(FrText):
    translator = MyMemoryTranslator(source='fr', target='en')
    EnTranslation = translator.translate(FrText)
    return EnTranslation
