from modeltranslation.translator import translator, TranslationOptions
from games.models import Game, Stage, Phase, Material

class GameOptions(TranslationOptions):
    fields = ('title', 'description', )


class StageOptions(TranslationOptions):
    fields = ('name',)


class PhaseOptions(TranslationOptions):
    fields = ('name',)


class MaterialOptions(TranslationOptions):
    fields = ('description',)


translator.register(Game, GameOptions)
translator.register(Stage, StageOptions)
translator.register(Phase, PhaseOptions)
translator.register(Material, MaterialOptions)
