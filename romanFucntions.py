from indicnlp.transliterate.unicode_transliterate import ItransTransliterator


def Hindi(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'hi')
    return output


def Telegu(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'te')
    return output


def Gujrati(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'gu')
    return output


def Punjabi(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'pa')
    return output


def Kannada(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'kn')
    return output


def Bengali(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'bn')
    return output


def Malayalam(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'ml')
    return output


def Odia(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'od')
    return output


def Tamil(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'ta')
    return output


def Sinhala(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'si')
    return output


def Assamese(input_text):
    output = ItransTransliterator.to_itrans(input_text, 'as')
    return output
