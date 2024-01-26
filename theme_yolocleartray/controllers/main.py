from dateutil import parser
from odoo import fields, SUPERUSER_ID, _
from odoo.http import request, route, Controller


class Main(Controller):

    @route('/consultant-register', type='http', auth="public", website=True)
    def consultant_register(self, **kw):
        if request.httprequest.method == 'POST':
            user = request.env.user
            customer = user.partner_id
            internal_users = request.env['res.users'].sudo().search([('share', '=', False)])
            start_date = parser.isoparse(kw.get('appointment_date', ''))
            end_date = fields.Datetime.add(start_date, hours=1)
            if user._is_public():
                old_contact = request.env['res.partner'].sudo().search([
                    '&', ('name', 'ilike', kw.get('name', 'Website Visitor')),
                    '|', ('phone', '=', kw.get('phone', '')),
                    ('mobile', '=', kw.get('phone', ''))
                ])
                if not old_contact:
                    customer = self._create_contact(**kw)
                else:
                    customer = old_contact
            participants = (internal_users.partner_id | customer)
            request.env['calendar.event'].with_user(SUPERUSER_ID).create({
                'name': _("Consulting For Customers %s") % customer.name,
                'partner_ids': [(6, 0, participants.ids)],
                'start': start_date,
                'stop': end_date,
                'description': kw.get('content', '')
            })
            return request.render('website.contactus_thanks', {})
        return request.redirect('/contactus')

    def _create_contact(self, **kw):
        return request.env['res.partner'].with_user(SUPERUSER_ID).create({
            'name': kw.get('name', 'Website Visitor'),
            'email': kw.get('email', False),
            'phone': kw.get('phone', False),
            'type': 'contact',
            'company_type': 'person'
        })
