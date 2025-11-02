{
    'name': 'Red Button Style',
    'version': '1.0',
    'summary': 'Changes the primary button color to red.',
    'description': 'A simple module to override the default Odoo primary button color and make it red.',
    'author': 'Ibraheem Barakat (via s3eedah)',
    'category': 'Themes',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'red_button_style/static/src/css/custom_styles.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
