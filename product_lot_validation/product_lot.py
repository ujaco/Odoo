# -*- coding: utf-8 -*-
import openerp
from openerp.osv import fields, osv
from datetime import datetime


class stock_production_lot(osv.osv):
    _inherit = 'stock.production.lot'

    def _check_unique_name(self, cursor, user, ids, context=None):
        for lot in self.browse(cursor, user, ids, context=context):
            if lot.name:
                val = self.pool.get("stock.production.lot").search(cursor, user, [('name', '=',lot.name ),('product_id', '=',lot.product_id.id ),('id','not in',ids)])
                if val:
                    return False
        return True
    

    def _check_date(self, cursor, user, ids, context=None):
        import pydevd;pydevd.settrace()
        for lot in self.browse(cursor, user, ids, context=context):
            life_date = datetime.strptime(lot.life_date, "%Y-%m-%d %H:%M:%S").date()
            if life_date < datetime.today().date():
                return False
        return True
    
    _columns = {
        'life_date': fields.datetime('End of Life Date',
            help='This is the date on which the goods with this Serial Number may become dangerous and must not be consumed.', required = True),
        }
    
    _constraints = [
        (_check_unique_name, 'Error: The batch number already exists for the product', ['name']),
        (_check_date, 'Error: Expiry date must be greater than today', ['life_date']),

    ]
