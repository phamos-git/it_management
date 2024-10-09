import frappe

def delete_custom_fields():
    custom_fields = {
        "Task": [
            "it_landscape",
            "customer",
            "user_account",
            "configuration_item",
            "github_sync_id",
            "it_management_table",
            "section_break_42"
        ],
        "Delivery Note": ["issue"],
        "Issue": [
            "it_landscape",
            "filter_based_on_customer",
            "full_customer_name",
            "task",
            "contact_html",
            "configuration_item",
            "it_management_table",
            "section_break_43"
        ],
        "Maintenance Schedule" : [
            "it_management_table",
            "section_break_9"
        ],
        "IT Service Report" : [
            "employee_name"
        ],
        "Project" : [
            "it_landscape",
            "customer_name",
            "configuration_item",
            "github_sync_id"
        ]
    }

    for doctype, fields in custom_fields.items():
        for fieldname in fields:
            custom_field_name = f"{doctype}-{fieldname}"
            try:
                frappe.delete_doc("Custom Field", custom_field_name, force=True)
                print(f"Custom Field {custom_field_name} deleted")
            except frappe.DoesNotExistError:
                print(f"Custom Field {custom_field_name} does not exist")