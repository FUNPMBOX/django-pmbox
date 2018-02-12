from django.contrib import admin
from games.models import Game, Stage, Phase, Material
from modeltranslation.admin import TranslationAdmin

class TranslatableAdminMixin(TranslationAdmin):
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class GameAdmin(TranslatableAdminMixin):
    filter_horizontal = ('material', 'phase', 'stage')
    fields = ('duration', 'max_people', 'title', 'short_description', 'description', 'stage', 'phase', 'material')


class StageAdmin(TranslatableAdminMixin):
    pass


class PhaseAdmin(TranslatableAdminMixin):
    pass


class MaterialAdmin(TranslatableAdminMixin):
    pass


admin.site.register(Game, GameAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Phase, PhaseAdmin)
admin.site.register(Material, MaterialAdmin)
