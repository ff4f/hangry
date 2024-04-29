from odoo import models, fields, api, exceptions, _
import requests

class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    geolocation_check_in = fields.Char("Geolocation Check In")
    geolocation_check_out = fields.Char("Geolocation Check Out")

    status = fields.Selection([('draft', 'Draft'),
                               ('reject', 'Reject'), ('approve', 'Approved')
                               ], string="Status", required=True, default='draft')

    supervisor_id = fields.Many2one('res.users', string='Supervisor')

    def action_approve(self):
        self.status = 'approve'
        self.supervisor_id = self.env.user.id

    def action_reject(self):
        self.status = 'reject'
        self.supervisor_id = self.env.user.id

    def _get_geolocation(self):
        try:
            response = requests.get('https://ipinfo.io')
            data = response.json()
            geolocation = data.get('loc') or ''
            return geolocation
        except Exception as e:
            print("Error occurred:", e)
            return None

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        geolocation = res._get_geolocation()
        if geolocation:
            res.geolocation_check_in = geolocation
        return res

    def write(self, vals):
        if vals.get('check_out'):
            geolocation = self._get_geolocation()
            if geolocation:
                vals['geolocation_check_out'] = geolocation
        return super(HrAttendance, self).write(vals)

