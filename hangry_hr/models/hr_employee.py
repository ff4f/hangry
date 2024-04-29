from odoo import models, fields, api, exceptions, _
from odoo.exceptions import AccessError, UserError, ValidationError

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    type_emp = fields.Selection([
        ('part', 'Part Time'),
        ('full', 'Full Time')
    ], string="Type Employee", default='full')

    # resource_calendar_ids = fields.Many2one('resource.calendar', 'Working Hours', )

    def action_create_user(self):
        """ Opens a wizard to compose an email, with relevant mail template loaded by default """
        self.ensure_one()
        if self.user_id:
            raise ValidationError(_("%s already has user", self.name))
        lang = self.env.context.get('lang')
        ctx = {
            'default_model': 'hr.employee',
            'default_employee_id': self.id,
            'default_email': self.work_email or self.private_email,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'wiz.employee.user',
            'views': [(False, 'form')],
            # 'view_id': False,
            'target': 'new',
            'context': ctx,
        }