import streamlit as st
import indicFunctions as fn
import romanFucntions as rn
import sys
from indicnlp import common
from indicnlp import loader
from indicnlp.transliterate.unicode_transliterate import ItransTransliterator
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

# The path to the local git repo for Indic NLP library
INDIC_NLP_LIB_HOME = r"indic_nlp_library"

# The path to the local git repo for Indic NLP Resources
INDIC_NLP_RESOURCES = r"indic_nlp_resources"

# Add library to Python path
sys.path.append(r'{}\src'.format(INDIC_NLP_LIB_HOME))

# Set environment variable for resources folder
common.set_resources_path(INDIC_NLP_RESOURCES)

loader.load()


def main():
    st.beta_set_page_config(page_title='Indian NLP', page_icon='💥',
                            layout='centered', initial_sidebar_state="expanded")
    st.title("A Translation Application based on NLP for Indian Languages")
    st.subheader("Built By - Mihir Pesswani")
    st.title("NLP for Indian Language")
    st.sidebar.title("Hindi Languages NLP")
    menu = ["Home"]
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        st.subheader("1. Indian Language Translation")
        lang1 = ['Hindi', 'Telegu', 'Gujrati', 'Punjabi',
                 'Kannada', 'Bengali', 'Malayalam', 'Odia', 'Tamil', 'Assamese', 'Sinhala']
        lang2 = ['Hindi', 'Telegu', 'Gujrati', 'Punjabi',
                 'Kannada', 'Bengali', 'Malayalam', 'Odia', 'Tamil', 'Assamese', 'Sinhala']

        l1 = st.selectbox('Choose Text Language', lang1)
        l2 = st.selectbox('Choose Translation Language', lang2)
        input_text = st.text_area(f"Enter Text in {l1}.")
        btn = st.button("Translate")

        # Hindi
        if l1 == 'Hindi':
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToHindi(input_text)
                    st.success(output)
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToTelegu(input_text)
                    st.success(output)
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToGujrati(input_text)
                    st.success(output)
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToBengali(input_text)
                    st.success(output)
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToMalyalam(input_text)
                    st.success(output)
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToKannada(input_text)
                    st.success(output)
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToOdia(input_text)
                    st.success(output)
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToTamil(input_text)
                    st.success(output)
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToAssamese(input_text)
                    st.success(output)
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.HindiToSinhala(input_text)
                    st.success(output)

        # Telegu
        if l1 == 'Telegu':
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToTelegu(input_text)
                    st.success(output)
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToHindi(input_text)
                    st.success(output)
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToGujrati(input_text)
                    st.success(output)
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToBengali(input_text)
                    st.success(output)
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToMalyalam(input_text)
                    st.success(output)
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToKannada(input_text)
                    st.success(output)
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToOdia(input_text)
                    st.success(output)
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToTamil(input_text)
                    st.success(output)
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToAssamese(input_text)
                    st.success(output)
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TeleguToSinhala(input_text)
                    st.success(output)

        # Gujrati
        if l1 == 'Gujrati':
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToGujrati(input_text)
                    st.success(output)
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToTelegu(input_text)
                    st.success(output)
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToHindi(input_text)
                    st.success(output)
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToBengali(input_text)
                    st.success(output)
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToMalyalam(input_text)
                    st.success(output)
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToKannada(input_text)
                    st.success(output)
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToOdia(input_text)
                    st.success(output)
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToTamil(input_text)
                    st.success(output)
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToAssamese(input_text)
                    st.success(output)
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.GujratiToSinhala(input_text)
                    st.success(output)

        # Bengali
        if l1 == 'Bengali':
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToBengali(input_text)
                    st.success(output)
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToTelegu(input_text)
                    st.success(output)
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToGujrati(input_text)
                    st.success(output)
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToHindi(input_text)
                    st.success(output)
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToMalyalam(input_text)
                    st.success(output)
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToKannada(input_text)
                    st.success(output)
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToOdia(input_text)
                    st.success(output)
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToTamil(input_text)
                    st.success(output)
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToAssamese(input_text)
                    st.success(output)
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.BengaliToSinhala(input_text)
                    st.success(output)

        # Punjabi
        if l1 == 'Punjabi':
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToTelegu(input_text)
                    st.success(output)
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToGujrati(input_text)
                    st.success(output)
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToHindi(input_text)
                    st.success(output)
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToBengali(input_text)
                    st.success(output)
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToMalyalam(input_text)
                    st.success(output)
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToKannada(input_text)
                    st.success(output)
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToOdia(input_text)
                    st.success(output)
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToTamil(input_text)
                    st.success(output)
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToAssamese(input_text)
                    st.success(output)
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.PunjabiToSinhala(input_text)
                    st.success(output)

        # Malayalam
        if l1 == 'Malayalam':
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToMalayalam(input_text)
                    st.success(output)
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToTelegu(input_text)
                    st.success(output)
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToGujrati(input_text)
                    st.success(output)
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToHindi(input_text)
                    st.success(output)
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToBengali(input_text)
                    st.success(output)
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToKannada(input_text)
                    st.success(output)
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToOdia(input_text)
                    st.success(output)
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToTamil(input_text)
                    st.success(output)
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToAssamese(input_text)
                    st.success(output)
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.MalayalamToSinhala(input_text)
                    st.success(output)

        # Tamil
        if l1 == 'Tamil':
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToTamil(input_text)
                    st.success(output)
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToTelegu(input_text)
                    st.success(output)
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToGujrati(input_text)
                    st.success(output)
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToHindi(input_text)
                    st.success(output)
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToMalyalam(input_text)
                    st.success(output)
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToKannada(input_text)
                    st.success(output)
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToOdia(input_text)
                    st.success(output)
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToBengali(input_text)
                    st.success(output)
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToAssamese(input_text)
                    st.success(output)
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.TamilToSinhala(input_text)
                    st.success(output)

        # Kannada
        if l1 == 'Kannada':
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToKannada(input_text)
                    st.success(output)
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToTelegu(input_text)
                    st.success(output)
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToGujrati(input_text)
                    st.success(output)
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToHindi(input_text)
                    st.success(output)
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToMalyalam(input_text)
                    st.success(output)
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToBengali(input_text)
                    st.success(output)
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToOdia(input_text)
                    st.success(output)
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToTamil(input_text)
                    st.success(output)
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToAssamese(input_text)
                    st.success(output)
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.KannadaToSinhala(input_text)
                    st.success(output)

        # Odia
        if l1 == 'Odia':
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToOdia(input_text)
                    st.success(output)
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToTelegu(input_text)
                    st.success(output)
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToGujrati(input_text)
                    st.success(output)
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToHindi(input_text)
                    st.success(output)
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToMalyalam(input_text)
                    st.success(output)
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToKannada(input_text)
                    st.success(output)
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToBengali(input_text)
                    st.success(output)
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToTamil(input_text)
                    st.success(output)
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToAssamese(input_text)
                    st.success(output)
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.OdiaToSinhala(input_text)
                    st.success(output)

        # Assamese
        if l1 == 'Assamese':
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToAssamese(input_text)
                    st.success(output)
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToTelegu(input_text)
                    st.success(output)
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToGujrati(input_text)
                    st.success(output)
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToHindi(input_text)
                    st.success(output)
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToMalyalam(input_text)
                    st.success(output)
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToKannada(input_text)
                    st.success(output)
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToOdia(input_text)
                    st.success(output)
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToTamil(input_text)
                    st.success(output)
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToBengali(input_text)
                    st.success(output)
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.AssameseToSinhala(input_text)
                    st.success(output)

        # Sinhala
        if l1 == 'Sinhala':
            if l2 == 'Sinhala':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToSinhala(input_text)
                    st.success(output)
            if l2 == 'Telegu':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToTelegu(input_text)
                    st.success(output)
            if l2 == 'Gujrati':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToGujrati(input_text)
                    st.success(output)
            if l2 == 'Hindi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToHindi(input_text)
                    st.success(output)
            if l2 == 'Punjabi':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToPunjabi(input_text)
                    st.success(output)
            if l2 == 'Malayalam':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToMalyalam(input_text)
                    st.success(output)
            if l2 == 'Kannada':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToKannada(input_text)
                    st.success(output)
            if l2 == 'Odia':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToOdia(input_text)
                    st.success(output)
            if l2 == 'Tamil':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToTamil(input_text)
                    st.success(output)
            if l2 == 'Assamese':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToAssamese(input_text)
                    st.success(output)
            if l2 == 'Bengali':
                if btn:
                    st.text(f"Translated to {l2}")
                    output = fn.SinhalaToBengali(input_text)
                    st.success(output)

        # Roman
        st.subheader("2. Indian Languages to Roman Script Translation")
        lg = st.selectbox('Choose the Text Language', lang1)
        input_text1 = st.text_area(f"Enter Text in {lg}")
        btn1 = st.button("Roman Translate")
        if lg == 'Hindi':
            if btn1:
                output = rn.Hindi(input_text1)
                st.success(output)
        if lg == 'Telegu':
            if btn1:
                output = rn.Telegu(input_text1)
                st.success(output)
        if lg == 'Gujrati':
            if btn1:
                output = rn.Gujrati(input_text1)
                st.success(output)
        if lg == 'Bengali':
            if btn1:
                output = rn.Bengali(input_text1)
                st.success(output)
        if lg == 'Kannada':
            if btn1:
                output = rn.Kannada(input_text1)
                st.success(output)
        if lg == 'Punjabi':
            if btn1:
                output = rn.Punjabi(input_text1)
                st.success(output)
        if lg == 'Malayalam':
            if btn1:
                output = rn.Malayalam(input_text1)
                st.success(output)
        if lg == 'Odia':
            if btn1:
                output = rn.Odia(input_text1)
                st.success(output)
        if lg == 'Tamil':
            if btn1:
                output = rn.Tamil(input_text1)
                st.success(output)
        if lg == 'Assamese':
            if btn1:
                output = rn.Assamese(input_text1)
                st.success(output)
        if lg == 'Sinhala':
            if btn1:
                output = rn.Sinhala(input_text1)
                st.success(output)

    hide_footer_style = """<style>
    .reportview-container .main footer {visibility : hidden;}
    #MainMenu {visibility: hidden;}
      
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
