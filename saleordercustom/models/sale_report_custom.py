from odoo import models, fields, api


class SaleReportCustom(models.Model):
    _name = 'sale.report.custom'
    _description = 'Informe Personalitzat de Comandes'
    _auto = False  # No crear una tabla para este modelo

    user_id = fields.Many2one('res.users', string='Comercial', readonly=True)
    state = fields.Selection([
        ('draft', 'Esborrany'),
        ('sent', 'Enviat'),
        ('sale', 'Venut'),
        ('done', 'Completat'),
        ('cancel', 'Cancel·lat'),
    ], string='Estat de la comanda', readonly=True)
    order_count = fields.Integer(string='Nombre de comandes', readonly=True)
    total_amount = fields.Float(string='Suma total dels imports', readonly=True)

    @api.model
    def init(self):
        # Elimina la vista si ya existe para evitar conflictos al actualizar
        self.env.cr.execute("DROP VIEW IF EXISTS sale_report_custom")
        # Crea la vista nuevamente con la estructura actual
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW sale_report_custom AS
            SELECT
                min(so.id) AS id,
                so.user_id AS user_id,
                so.state AS state,
                COUNT(*) AS order_count,
                SUM(so.amount_total) AS total_amount
            FROM
                sale_order so
            GROUP BY
                so.user_id, so.state
        """)

    @api.model
    def action_order_list_custom(self):
        context = self._context

