{
    "name": "Sale Order Custom",  # The name that will appear in the App list
    "version": "1.0",  # Version
    "author": "Andreu Gisbert Bel",  # Author
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base", "sale"],  # dependencies
    "data": [
        "views/sale_order_views.xml",
        "views/sale_order_menus.xml",
        "reports/sale_order_report_extension.xml",
        "security/ir.model.access.csv",
        "reports/report_sale_order_custom.xml",
        "reports/sale_order_reports.xml"


    ],
    "installable": True,
    'license': 'LGPL-3',
}
