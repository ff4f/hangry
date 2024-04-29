from odoo import models, fields, api, exceptions, _

class WizEmployeeUser(models.TransientModel):
    _name = "wiz.employee.user"

    employee_id = fields.Many2one("hr.employee", "Employee")
    email = fields.Char("Email")
    password = fields.Char("Password", required=True)

    def action_create_user(self):
        user_id = self.env['res.users'].create({
            'name': self.employee_id.name,
            'login': self.email,
            'email': self.email,
            'password': self.password,
        })
        hr_group = ''
        if self.employee_id.type_emp == 'full':
            hr_group = self.env.ref('hangry_hr.group_hangry_hr_fulltime', raise_if_not_found=False)
        else:
            hr_group = self.env.ref('hangry_hr.group_hangry_hr_parttime', raise_if_not_found=False)

        if hr_group:
            hr_group.write({'users': [(4, user_id.id)]})

        self.employee_id.user_id = user_id.id

        return True