# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Prescription Sale Stock - US",
    "summary": "Provides US Locale to Medical Prescription Sale Stock",
    "version": "10.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "post_init_hook": "_inherit_medication_template_vals",
    "depends": [
        "medical_base_us",
        "sale_stock_medical_prescription",
        "medical_prescription_us",
    ],
    "data": [
        "views/procurement_order_view.xml",
        "views/res_company_view.xml",
    ],
    "demo": [
        "demo/medical_patient_demo.xml",
        "demo/medical_medicament_demo.xml",
        "demo/medical_medicament_ndc_demo.xml",
        "demo/medical_pharmacy_demo.xml",
        "demo/medical_physician_demo.xml",
        "demo/medical_patient_medication_demo.xml",
        "demo/medical_prescription_order_demo.xml",
        "demo/medical_prescription_order_line_demo.xml",
        "demo/sale_order_demo.xml",
        "demo/sale_order_line_demo.xml",
        "demo/procurement_order_demo.xml",
    ],
}
