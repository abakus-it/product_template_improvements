from openerp import models, fields, api
from openerp.exceptions import ValidationError

class product_template_improvements(models.Model):
    _inherit = ['product.template']

    @api.constrains('default_code')
    def check_default_code(self):
        if self.default_code and len(self.default_code)>0:
            cr = self.env.cr
            uid = self.env.user.id
            product_template_obj = self.pool.get('product.template')
            product_templates = product_template_obj.search(cr, uid, [('default_code', '=', self.default_code), ('id', '!=', self.id)])
            if len(product_templates) > 0:
                raise ValidationError('The internal reference already set on another product. As this field is supposed to be unique, please enter another one.')

    @api.constrains('barcode')
    def check_barcode(self):
        if self.barcode and len(self.barcode)>0:
            cr = self.env.cr
            uid = self.env.user.id
            product_template_obj = self.pool.get('product.template')
            product_templates = product_template_obj.search(cr, uid, [('barcode', '=', self.barcode), ('id', '!=', self.id)])
            if len(product_templates) > 0:
                raise ValidationError('The  barcode is already set on another product. As this field is supposed to be unique, please enter another one.')
