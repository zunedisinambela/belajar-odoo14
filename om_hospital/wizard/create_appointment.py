from odoo import api, fields, models, _


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    date_appointment = fields.Date(string='Date', required=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)

    def action_create_appointment(self):
        print("Button is Clicked")
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment,
        }
        self.env['hospital.appointment'].create(vals)
