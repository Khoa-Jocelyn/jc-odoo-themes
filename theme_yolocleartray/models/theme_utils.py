from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    @classmethod
    def _build_model(cls, pool, cr):
        res = super(ThemeUtils, cls)._build_model(pool, cr)
        if 'theme_yolocleartray.yolo_header_template' not in res._header_templates:
            res._header_templates.insert(0, 'theme_yolocleartray.yolo_header_template')
        return res

    def _theme_yolocleartray_post_copy(self, mod):
        self.disable_view('website.header_visibility_standard')
        self.enable_view('website.header_visibility_fixed')

        self.disable_view('website.template_header_default')
        self.enable_view('theme_yolocleartray.yolo_header_template')

        self.disable_view('website_sale.header_cart_link')
        self.enable_view('theme_yolocleartray.header_shopping_cart')
