# coding=utf-8

from __future__ import unicode_literals
from frappe import _

def get_data():
	colors = {
		"Stock": "#f39c12",
		"Selling": "#1abc9c",
		"Buying": "#c0392b",
		"HR": "#2ecc71",
		"Projects": "#8e44ad",
		"Support": "#2c3e50",
		"Accounts": "#3498db",
		"Tools": "#FFF5A7"
	}

	return [


		{"module_name": "Gray Fabric", "type": "link",
		 "link": "Form/Item Group/Gray Fabric",
		 "color": "gray", "icon": "octicon octicon-git-commit"},

		{"module_name": "Cutpiece", "type": "link",
		 "link": "Form/Item Group/Cutpiece",
		 "color": "blue", "icon": "fa fa-scissors"},

		{"module_name": "Stock Transfer", "type": "link",
		 "link": "Form/Stock Entry/New Stock Entry",
		 "color": "yellow", "icon": "octicon octicon-git-branch", "reverse": 1,},

		{"module_name": "Embroidery", "type": "link",
		 "link": "Form/Item Group/Embroidery",
		 "color": "Red", "icon": "octicon octicon-git-compare"},

		{"module_name": "Finished Goods", "type": "link",
		 "link": "Form/Item Group/Finished Goods", 
		 "color": "Green", "icon": "octicon octicon-package"},


		# old
		{
			"module_name": "Accounts",
			"color": "#3498db",
			"icon": "octicon octicon-repo",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "Stock",
			"color": "#f39c12",
			"icon": "octicon octicon-package",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "CRM",
			"color": "#EF4DB6",
			"icon": "octicon octicon-broadcast",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "Selling",
			"color": "#1abc9c",
			"icon": "octicon octicon-tag",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "Buying",
			"color": "#c0392b",
			"icon": "octicon octicon-briefcase",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "HR",
			"color": "#2ecc71",
			"icon": "octicon octicon-organization",
			"label": _("Human Resources"), "type": "module",
			"hidden": 1
		},
		{
			"module_name": "Manufacturing",
			"color": "#7f8c8d",
			"icon": "octicon octicon-tools",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "Projects",
			"color": "#8e44ad",
			"icon": "octicon octicon-rocket",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "Support",
			"color": "#2c3e50",
			"icon": "octicon octicon-issue-opened",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "Learn",
			"color": "#FF888B",
			"icon": "octicon octicon-device-camera-video",
			"type": "module",
			"is_help": True,
			"label": _("Learn"),
			"hidden": 1
		},
		{
			"module_name": "Maintenance",
			"color": "#FF888B",
			"icon": "octicon octicon-tools",
			"type": "module",
			"label": _("Maintenance"),
			"hidden": 1
		},
		{
			"module_name": "Education",
			"color": "#428B46",
			"icon": "octicon octicon-mortar-board",
			"type": "module",
			"label": _("Education"),
			"hidden": 1
		},
		{
			"module_name": "Healthcare",
			"color": "#FF888B",
			"icon": "fa fa-heartbeat",
			"type": "module",
			"label": _("Healthcare"),
			"hidden": 1
		},
		{
			"module_name": "Restaurant",
			"color": "#EA81E8",
			"icon": "🍔",
			"_doctype": "Restaurant",
			"type": "module",
			"link": "List/Restaurant",
			"label": _("Restaurant"),
			"hidden": 1
		},
		{
			"module_name": "Hotels",
			"color": "#EA81E8",
			"icon": "fa fa-bed",
			"type": "module",
			"label": _("Hotels"),
			"hidden": 1
		},
		{
			"module_name": "Agriculture",
			"color": "#8BC34A",
			"icon": "octicon octicon-globe",
			"type": "module",
			"label": _("Agriculture"),
			"hidden": 1
		},
		{
			"module_name": "Assets",
			"color": "#4286f4",
			"icon": "octicon octicon-database",
			"hidden": 1,
			"label": _("Assets"),
			"type": "module"
		},
		{
			"module_name": "Non Profit",
			"color": "#DE2B37",
			"icon": "octicon octicon-heart",
			"type": "module",
			"label": _("Non Profit"),
			"hidden": 1
		}
	]









'''
		{"module_name": "Item", "_doctype": "Item", "type": "list",
			"color": colors["Stock"], "icon": "octicon octicon-package"},
		{"module_name": "Item Price", "_doctype": "Item Price", "type": "list",
			"color": colors["Stock"], "icon": "fa fa-usd"},
		{"module_name": "Pricing Rule", "_doctype": "Pricing Rule", "type": "list",
			"color": colors["Stock"], "icon": "fa fa-usd"},

		{"module_name": "Customer", "_doctype": "Customer", "type": "list",
			"color": colors["Selling"], "icon": "octicon octicon-tag"},
		{"module_name": "Supplier", "_doctype": "Supplier", "type": "list",
			"color": colors["Buying"], "icon": "octicon octicon-briefcase"},
		{"module_name": "Letter of Credit", "_doctype": "Letter of Credit", "type": "list",
			"color": colors["Buying"], "icon": "fa fa-university"},
		{"module_name": "Account", "_doctype": "Account", "type": "link", "link": "Tree/Account", "label": _("Chart of Accounts"),
			"color": colors["Accounts"], "icon": "fa fa-sitemap"},

		{"module_name": "Project", "_doctype": "Project", "type": "list",
			"color": colors["Projects"], "icon": "octicon octicon-rocket"},
		{"module_name": "Task", "_doctype": "Task", "type": "list",
			"color": colors["Projects"], "icon": "octicon octicon-rocket"},

		{"module_name": "Sales Order", "_doctype": "Sales Order", "type": "list",
			"color": colors["Selling"], "icon": "fa fa-file-text"},
		{"module_name": "Purchase Order", "_doctype": "Purchase Order", "type": "list",
			"color": colors["Buying"], "icon": "fa fa-file-text"},
		{"module_name": "Delivery Note", "_doctype": "Delivery Note", "type": "list",
			"color": colors["Stock"], "icon": "fa fa-truck"},
		{"module_name": "Purchase Receipt", "_doctype": "Purchase Receipt", "type": "list",
			"color": colors["Stock"], "icon": "fa fa-truck"},
		{"module_name": "Sales Invoice", "_doctype": "Sales Invoice", "type": "list",
			"color": colors["Accounts"], "icon": "fa fa-file-text"},
		{"module_name": "Purchase Invoice", "_doctype": "Purchase Invoice", "type": "list",
			"color": colors["Accounts"], "icon": "fa fa-file-text"},

		{"module_name": "Stock Entry", "_doctype": "Stock Entry", "type": "list",
			"color": colors["Stock"], "icon": "fa fa-truck"},
		{"module_name": "Stock Reconciliation", "_doctype": "Stock Reconciliation", "type": "list",
			"color": colors["Stock"], "icon": "fa fa-files-o"},

		{"module_name": "Journal Entry", "_doctype": "Journal Entry", "type": "list",
			"color": colors["Accounts"], "icon": "fa fa-book"},
		{"module_name": "Payment Entry", "_doctype": "Payment Entry", "type": "list",
			"color": colors["Accounts"], "icon": "fa fa-money"},
		{"module_name": "Payment Reconciliation", "_doctype": "Payment Reconciliation", "type": "list",
			"color": colors["Accounts"], "icon": "fa fa-files-o"},

		{"module_name": "Leaderboard", "type": "page", "link": "leaderboard", "label": _("Leaderboard"),
			"color": "#589494", "icon": "octicon octicon-graph"},

		{"module_name": "General Ledger", "_report": "General Ledger", "type": "query-report", "link": "query-report/General Ledger",
			"color": colors["Accounts"], "icon": "fa fa-book"},
		{"module_name": "Accounts Receivable", "_report": "Accounts Receivable", "type": "query-report", "link": "query-report/Accounts Receivable",
			"color": colors["Selling"], "icon": "fa fa-tasks"},
		{"module_name": "Accounts Payable", "_report": "Accounts Payable", "type": "query-report", "link": "query-report/Accounts Payable",
			"color": colors["Buying"], "icon": "fa fa-tasks"},
		{"module_name": "Customer Ledger Summary", "_report": "Customer Ledger Summary", "type": "query-report", "link": "query-report/Customer Ledger Summary",
			"color": colors["Selling"], "icon": "fa fa-book"},
		{"module_name": "Supplier Ledger Summary", "_report": "Supplier Ledger Summary", "type": "query-report", "link": "query-report/Supplier Ledger Summary",
			"color": colors["Buying"], "icon": "fa fa-book"},
		{"module_name": "Customer Credit Balance", "_report": "Customer Credit Balance", "type": "query-report", "link": "query-report/Customer Credit Balance",
			"color": colors["Selling"], "icon": "fa fa-credit-card"},

		{"module_name": "Stock Ledger", "_report": "Stock Ledger", "type": "query-report", "link": "query-report/Stock Ledger",
			"color": colors["Stock"], "icon": "fa fa-exchange"},
		{"module_name": "Stock Balance", "_report": "Stock Balance", "type": "query-report", "link": "query-report/Stock Balance",
			"color": colors["Stock"], "icon": "octicon octicon-package"},

		{"module_name": "Sales Analytics", "_report": "Sales Analytics", "type": "query-report", "link": "query-report/Sales Analytics",
			"color": colors["Selling"], "icon": "fa fa-line-chart"},
		{"module_name": "Sales Details", "_report": "Sales Details", "type": "query-report", "link": "query-report/Sales Details",
			"color": colors["Selling"], "icon": "fa fa-list"},

		{"module_name": "Purchase Analytics", "_report": "Purchase Analytics", "type": "query-report", "link": "query-report/Purchase Analytics",
			"color": colors["Buying"], "icon": "fa fa-line-chart"},
		{"module_name": "Purchase Details", "_report": "Purchase Details", "type": "query-report", "link": "query-report/Purchase Details",
			"color": colors["Buying"], "icon": "fa fa-list"},

		{"module_name": "Trial Balance", "_report": "Trial Balance", "type": "query-report", "link": "query-report/Trial Balance",
			"color": colors["Accounts"], "icon": "fa fa-balance-scale"},
		{"module_name": "Trial Balance for Party", "_report": "Trial Balance for Party", "type": "query-report", "link": "query-report/Trial Balance for Party",
			"color": colors["Accounts"], "icon": "fa fa-balance-scale"},
'''