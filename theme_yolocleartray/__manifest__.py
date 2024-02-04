{
    "name": "Theme Yolo Clear Tray",
    "summary": "Theme, Layout, Snippets for website Yolo Clear Tray",
    "description": "Theme for website Yolo Clear Tray",
    "author": "Jocelyn",
    "website": "https://jocelyn.com/",
    "category": "Theme/Corporate",
    "sequence": 130,
    "version": "0.1.0",
    "depends": ['website_sale', 'website_crm', 'website_event', 'website_blog'],
    "data": [
        'data/website_data.xml',
        'data/attachment_data.xml',
        'data/pages/home.xml',
        'data/pages/introduce.xml',
        'data/pages/expect.xml',
        'data/menu_data.xml',
        'views/website_templates.xml',
    ],
    "images": [],
    'assets': {
        'web._assets_primary_variables': [
            'theme_yolocleartray/static/src/scss/mixins.scss',
        ],
        'web.assets_frontend': [
            'theme_yolocleartray/static/src/scss/style.scss',
        ],

    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "price": 99.9,
    "currency": "EUR",
    "license": "OPL-1"
}
