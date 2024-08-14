from modeltranslation.translator import register,TranslationOptions,translator
from .models import *

@register(Fakultet)
class FakultetTranslationOptions(TranslationOptions):
    fields=("nomi","kurs")
    
@register(Savollar)
class SavollarTranslationOptions(TranslationOptions):
    fields=("kurs","fakultet","savol","variant1","variant2","variant3","variant4","javob")

@register(Jadval)
class JadvalTranslationOptions(TranslationOptions):
    fields=("kurs","fakultet","ismi","togri_javob","notogri_javob")