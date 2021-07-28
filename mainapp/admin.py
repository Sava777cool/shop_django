from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin

from .models import *


class WatchAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and not instance.sd:
            self.fields['sd_volume_max'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray;'
            })

    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None
        return self.cleaned_data


class JewelryAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='jewelry'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class WatchAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = WatchAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='watch'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Jewelry, JewelryAdmin)
admin.site.register(Watch, WatchAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)

