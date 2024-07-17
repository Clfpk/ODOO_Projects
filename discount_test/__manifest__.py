{
    'name': "My Discount Module",
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'version': '1.0',
    'depends': ['base', 'point_of_sale', 'web', 'pos_restaurant', 'pos_self_order', 'product'],
    'data': ['discount_button/discount_button.xml'],
    'assets': {
        'point_of_sale._assets_pos': [
            'discount_button/discount_button.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
