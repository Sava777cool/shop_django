from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Watch


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'jewelry': {
        'Description': 'description',
        'Gender': 'gender',
        'Condition': 'condition',
        'Vendor code': 'vendor_code',
        'Serial number': 'serial_number',
        'Country': 'country',
        'Manufacture': 'manufacture',
        'Metal': 'metal',
        'Size': 'size',
        'Presence of gems': 'sd',
        'Gems': 'sd_volume_max',
    },
    'watch': {
        'Description': 'description',
        'Gender': 'gender',
        'Condition': 'condition',
        'Vendor code': 'vendor_code',
        'Serial number': 'serial_number',
        'Country': 'country',
        'Manufacture': 'manufacture',
        'Production year': 'production_year',
        'Case metal': 'case_metal',
        'Caliber': 'caliber',
        'Glass': 'glass',
        'Bracelet material': 'bracelet_material',
        'Bracelet size': 'bracelet_size',
        'Box availability': 'sd',
        'Box material': 'sd_volume_max',
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Watch):
        if not product.sd:
            PRODUCT_SPEC['watch'].pop('Box availability', None)
        else:
            PRODUCT_SPEC['watch']['Box material'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)



