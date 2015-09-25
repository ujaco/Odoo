##############################################################################

{
    'name': 'Product Lot Validation',
    'version': '1.0',
    'author': 'Shyam, EduSeva Technologies',
    'summary': 'Expiry date mandatory and greater than 0. Duplicate lots not allowed',
    'description': """
This module makes the end of life date mandatory and greater than today.Also prevents the duplicate creation of lots with the same name for the same product""",
    'depends': ['stock','product_expiry'],
    'application': True,
    'data': ['product_lot_view.xml'],
	#'demo': ['todo.task.csv','todo_data.xml']
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
