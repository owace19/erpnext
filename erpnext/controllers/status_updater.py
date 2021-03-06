# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt, comma_or, nowdate, getdate
from frappe import _
from frappe.model.document import Document

def validate_status(status, options):
	if status not in options:
		frappe.throw(_("Status must be one of {0}").format(comma_or(options)))

status_map = {
	"Lead": [
		["Lost Quotation", "has_lost_quotation"],
		["Opportunity", "has_opportunity"],
		["Quotation", "has_quotation"],
		["Converted", "has_customer"],
	],
	"Opportunity": [
		["Lost", "eval:self.status=='Lost'"],
		["Lost", "has_lost_quotation"],
		["Quotation", "has_active_quotation"],
		["Converted", "has_ordered_quotation"],
		["Closed", "eval:self.status=='Closed'"]
	],
	"Quotation": [
		["Draft", None],
		["Open", "eval:self.docstatus==1"],
		["Lost", "eval:self.status=='Lost'"],
		["Ordered", "has_sales_order"],
		["Cancelled", "eval:self.docstatus==2"],
	],
	"Sales Order": [
		["Draft", None],
		["To Deliver and Bill", "eval:self.per_delivered < 100 and self.per_completed < 100 and self.docstatus == 1"],
		["To Bill", "eval:self.per_delivered == 100 and self.per_completed < 100 and self.docstatus == 1"],
		["To Deliver", "eval:self.per_delivered < 100 and (self.grand_total == 0 or self.per_completed == 100) and self.docstatus == 1"],
		["Completed", "eval:self.per_delivered == 100 and (self.grand_total == 0 or self.per_completed == 100) and self.docstatus == 1"],
		["Completed", "eval:self.order_type == 'Maintenance' and (self.grand_total == 0 or self.per_completed == 100) and self.docstatus == 1"],
		["Cancelled", "eval:self.docstatus==2"],
		["Closed", "eval:self.status=='Closed'"],
	],
	"Sales Invoice": [
		["Draft", None],
		["Submitted", "eval:self.docstatus==1"],
		["Paid", "eval:self.outstanding_amount==0 and self.docstatus==1"],
		["Return", "eval:self.is_return==1 and self.docstatus==1"],
		["Credit Note Issued", "eval:self.outstanding_amount < 0 and self.docstatus==1"],
		["Unpaid", "eval:self.outstanding_amount > 0 and getdate(self.due_date) >= getdate(nowdate()) and self.docstatus==1"],
		["Overdue", "eval:self.outstanding_amount > 0 and getdate(self.due_date) < getdate(nowdate()) and self.docstatus==1"],
		["Cancelled", "eval:self.docstatus==2"],
	],
	"Purchase Invoice": [
		["Draft", None],
		["Submitted", "eval:self.docstatus==1"],
		["Paid", "eval:self.outstanding_amount==0 and self.docstatus==1"],
		["Return", "eval:self.is_return==1 and self.docstatus==1"],
		["Debit Note Issued", "eval:self.outstanding_amount < 0 and self.docstatus==1"],
		["Unpaid", "eval:self.outstanding_amount > 0 and getdate(self.due_date) >= getdate(nowdate()) and self.docstatus==1"],
		["Overdue", "eval:self.outstanding_amount > 0 and getdate(self.due_date) < getdate(nowdate()) and self.docstatus==1"],
		["Cancelled", "eval:self.docstatus==2"],
	],
	"Purchase Order": [
		["Draft", None],
		["To Receive and Bill", "eval:self.per_received < 100 and self.per_completed < 100 and self.docstatus == 1"],
		["To Bill", "eval:self.per_received == 100 and self.per_completed < 100 and self.docstatus == 1"],
		["To Receive", "eval:self.per_received < 100 and (self.grand_total == 0 or self.per_completed == 100) and self.docstatus == 1"],
		["Completed", "eval:self.per_received == 100 and (self.grand_total == 0 or self.per_completed == 100) and self.docstatus == 1"],
		["Delivered", "eval:self.status=='Delivered'"],
		["Cancelled", "eval:self.docstatus==2"],
		["Closed", "eval:self.status=='Closed'"],
	],
	"Delivery Note": [
		["Draft", None],
		["To Bill", "eval:self.per_completed < 100 and self.docstatus == 1"],
		["Completed", "eval:(self.grand_total == 0 or self.per_completed == 100) and self.docstatus == 1"],
		["Return", "eval:self.is_return and self.docstatus == 1"],
		["Cancelled", "eval:self.docstatus==2"],
		["Closed", "eval:self.status=='Closed'"],
	],
	"Purchase Receipt": [
		["Draft", None],
		["To Bill", "eval:self.per_completed < 100 and self.docstatus == 1"],
		["Completed", "eval:(self.grand_total == 0 or self.per_completed == 100) and self.docstatus == 1"],
		["Return", "eval:self.is_return and self.docstatus == 1"],
		["Cancelled", "eval:self.docstatus==2"],
		["Closed", "eval:self.status=='Closed'"],
	],
	"Material Request": [
		["Draft", None],
		["Stopped", "eval:self.status == 'Stopped'"],
		["Cancelled", "eval:self.docstatus == 2"],
		["Pending", "eval:self.status != 'Stopped' and self.per_ordered == 0 and self.docstatus == 1"],
		["Partially Ordered", "eval:self.status != 'Stopped' and self.per_ordered < 100 and self.per_ordered > 0 and self.docstatus == 1"],
		["Ordered", "eval:self.status != 'Stopped' and self.per_ordered == 100 and self.docstatus == 1 and self.material_request_type == 'Purchase'"],
		["Transferred", "eval:self.status != 'Stopped' and self.per_ordered == 100 and self.docstatus == 1 and self.material_request_type == 'Material Transfer'"],
		["Issued", "eval:self.status != 'Stopped' and self.per_ordered == 100 and self.docstatus == 1 and self.material_request_type == 'Material Issue'"],
		["Manufactured", "eval:self.status != 'Stopped' and self.per_ordered == 100 and self.docstatus == 1 and self.material_request_type == 'Manufacture'"]
	],
	"Bank Transaction": [
		["Unreconciled", "eval:self.docstatus == 1 and self.unallocated_amount>0"],
		["Reconciled", "eval:self.docstatus == 1 and self.unallocated_amount<=0"]
	],
	"Landed Cost Voucher": [
		["Draft", None],
		["Submitted", "eval:self.docstatus==1"],
		["Paid", "eval:self.grand_total and self.outstanding_amount <= 0 and self.docstatus==1"],
		["Unpaid", "eval:self.outstanding_amount > 0 and getdate(self.due_date) >= getdate(nowdate()) and self.docstatus==1"],
		["Overdue", "eval:self.outstanding_amount > 0 and getdate(self.due_date) < getdate(nowdate()) and self.docstatus==1"],
		["Cancelled", "eval:self.docstatus==2"],
	],
	"Employee Advance": [
		["Draft", None],
		["Unpaid", "eval:self.docstatus==1"],
		["Unclaimed", "eval:self.paid_amount and self.paid_amount == self.advance_amount and self.docstatus==1"],
		["Claimed", "eval:self.paid_amount and self.balance_amount == 0 and self.docstatus==1"],
		["Cancelled", "eval:self.docstatus==2"],
	],
	"Expense Claim": [
		["Draft", None],
		["Submitted", "eval:self.docstatus==1"],
		["Unpaid", "eval:self.approval_status == 'Approved' and self.outstanding_amount > 0 and self.docstatus==1"],
		["Paid", "eval:self.approval_status == 'Approved' and self.outstanding_amount == 0 and self.docstatus==1"],
		["Rejected", "eval:self.approval_status == 'Rejected' and self.docstatus==1"],
		["Cancelled", "eval:self.docstatus==2"],
	]
}

class StatusUpdater(Document):
	"""
		Updates the status of the calling records
		Delivery Note: Update Delivered Qty, Update Percent and Validate over delivery
		Sales Invoice: Update Billed Amt, Update Percent and Validate over billing
		Installation Note: Update Installed Qty, Update Percent Qty and Validate over installation
	"""

	def update_prevdoc_status(self):
		self.update_qty()
		self.validate_qty()

	def set_status(self, update=False, status=None, update_modified=True):
		if self.is_new():
			if self.get('amended_from'):
				self.status = 'Draft'
			return

		if self.doctype in status_map:
			_status = self.status

			if status and update:
				self.db_set("status", status)

			sl = status_map[self.doctype][:]
			sl.reverse()
			for s in sl:
				if not s[1]:
					self.status = s[0]
					break
				elif s[1].startswith("eval:"):
					if frappe.safe_eval(s[1][5:], None, { "self": self.as_dict(), "getdate": getdate,
							"nowdate": nowdate, "get_value": frappe.db.get_value }):
						self.status = s[0]
						break
				elif getattr(self, s[1])():
					self.status = s[0]
					break

			if self.status != _status and self.status not in ("Cancelled", "Partially Ordered",
																"Ordered", "Issued", "Transferred"):
				self.add_comment("Label", _(self.status))

			if update:
				self.db_set('status', self.status, update_modified = update_modified)

	def validate_qty(self):
		"""Validates qty at row level"""
		self.tolerance = {}
		self.global_tolerance = None

		for args in self.status_updater:
			if "target_ref_field" not in args:
				# if target_ref_field is not specified, the programmer does not want to validate qty / amount
				continue

			# get unique transactions to update
			for d in self.get_all_children():
				if hasattr(d, 'qty') and d.qty < 0 and not self.get('is_return'):
					frappe.throw(_("For an item {0}, quantity must be positive number").format(d.item_code))

				if hasattr(d, 'qty') and d.qty > 0 and self.get('is_return'):
					frappe.throw(_("For an item {0}, quantity must be negative number").format(d.item_code))

				if d.doctype == args['source_dt'] and d.get(args["join_field"]):
					args['name'] = d.get(args['join_field'])

					if "ignore_overflow" in args:
						if callable(args['ignore_overflow']):
							if args['ignore_overflow'](d):
								continue
						elif args['ignore_overflow']:
							continue

					# get all qty where qty > target_field
					item = frappe.db.sql("""select item_code, `{target_ref_field}`,
						{target_field}, parenttype, parent from `tab{target_dt}`
						where `{target_ref_field}` < {target_field}
						and name=%s and docstatus=1""".format(**args),
						args['name'], as_dict=1)
					if item:
						item = item[0]
						item['idx'] = d.idx
						item['target_ref_field'] = args['target_ref_field'].replace('_', ' ')

						# if not item[args['target_ref_field']]:
						# 	msgprint(_("Note: System will not check over-delivery and over-booking for Item {0} as quantity or amount is 0").format(item.item_code))
						if args.get('no_tolerance'):
							item['reduce_by'] = item[args['target_field']] - item[args['target_ref_field']]
							if item['reduce_by'] > .01:
								self.limits_crossed_error(args, item)

						elif item[args['target_ref_field']]:
							self.check_overflow_with_tolerance(item, args)

	def check_overflow_with_tolerance(self, item, args):
		"""
			Checks if there is overflow condering a relaxation tolerance
		"""
		# check if overflow is within tolerance
		tolerance, self.tolerance, self.global_tolerance = get_tolerance_for(item['item_code'],
			self.tolerance, self.global_tolerance)
		overflow_percent = ((item[args['target_field']] - item[args['target_ref_field']]) /
		 	item[args['target_ref_field']]) * 100

		if overflow_percent - tolerance > 0.01:
			item['max_allowed'] = flt(item[args['target_ref_field']] * (100+tolerance)/100)
			item['reduce_by'] = item[args['target_field']] - item['max_allowed']

			self.limits_crossed_error(args, item)

	def limits_crossed_error(self, args, item):
		'''Raise exception for limits crossed'''
		frappe.throw(_('This document is over limit by {0} {1} for item {4}. Are you making another {3} against the same {2}?')
			.format(
				frappe.bold(_(item["target_ref_field"].title())),
				frappe.bold(item["reduce_by"]),
				frappe.bold(_(args.get('target_dt'))),
				frappe.bold(_(self.doctype)),
				frappe.bold(item.get('item_code'))
			) + '<br><br>' +
				_('To allow over-billing or over-ordering, update "Allowance" in Stock Settings or the Item.'),
			title = _('Limit Crossed'))

	def update_qty(self, update_modified=True):
		"""Updates qty or amount at row level

			:param update_modified: If true, updates `modified` and `modified_by` for target parent doc
		"""
		for args in self.status_updater:
			# condition to include current record (if submit or no if cancel)
			if self.docstatus == 1:
				args['cond'] = ' or parent="%s"' % self.name.replace('"', '\"')
			else:
				args['cond'] = ' and parent!="%s"' % self.name.replace('"', '\"')

			updated_parents = []
			if "update_children" in args and callable(args['update_children']):
				updated_parents = args["update_children"](update_modified)
			elif args.get('update_children', True):
				self._update_children(args, update_modified)

			if "percent_join_field" in args or "percent_join_name" in args:
				if not updated_parents:
					if args.get('percent_join_name'):
						updated_parents.append(args.get('percent_join_name'))
					elif args.get('percent_join_field'):
						updated_parents = [d.get(args['percent_join_field']) for d in self.get_all_children(args['source_dt'])]

				updated_parents = set(updated_parents)
				self._update_percent_field_in_targets(args, updated_parents, update_modified)

	def _update_children(self, args, update_modified):
		"""Update quantities or amount in child table"""
		for d in self.get_all_children():
			if d.doctype != args['source_dt']:
				continue

			self._update_modified(args, update_modified)

			# updates qty in the child table
			args['detail_id'] = d.get(args['join_field'])

			args['second_source_condition'] = ""
			if args.get('second_source_dt') and args.get('second_source_field') \
					and args.get('second_join_field'):
				if not args.get("second_source_extra_cond"):
					args["second_source_extra_cond"] = ""

				args['second_source_condition'] = """ + ifnull((select sum(%(second_source_field)s)
					from `tab%(second_source_dt)s`
					where `%(second_join_field)s`="%(detail_id)s"
					and (`tab%(second_source_dt)s`.docstatus=1) %(second_source_extra_cond)s), 0) """ % args

			if args['detail_id']:
				if not args.get("extra_cond"): args["extra_cond"] = ""

				frappe.db.sql("""update `tab%(target_dt)s`
					set %(target_field)s = (
						(select ifnull(sum(%(source_field)s), 0)
							from `tab%(source_dt)s` where `%(join_field)s`="%(detail_id)s"
							and (docstatus=1 %(cond)s) %(extra_cond)s)
						%(second_source_condition)s
					)
					%(update_modified)s
					where name='%(detail_id)s'""" % args)

	def _update_percent_field_in_targets(self, args, targets, update_modified=True):
		"""Update percent field in parent transaction"""
		for name in targets:
			if name:
				args['name'] = name
				self._update_percent_field(args, update_modified)

	def _update_percent_field(self, args, update_modified=True):
		"""Update percent field in parent transaction"""

		self._update_modified(args, update_modified)

		if args.get('target_parent_field'):
			frappe.db.sql("""update `tab%(target_parent_dt)s`
				set %(target_parent_field)s = round(
					ifnull((select
						ifnull(sum(if(%(target_ref_field)s > %(target_field)s, abs(%(target_field)s), abs(%(target_ref_field)s))), 0)
						/ sum(abs(%(target_ref_field)s)) * 100
					from `tab%(target_dt)s` where parent="%(name)s" having sum(abs(%(target_ref_field)s)) > 0), 0), 6)
					%(update_modified)s
				where name='%(name)s'""" % args)

			# update field
			if args.get('status_field'):
				frappe.db.sql("""update `tab%(target_parent_dt)s`
					set %(status_field)s = if(%(target_parent_field)s<0.001,
						'Not %(keyword)s', if(%(target_parent_field)s>=99.999999,
						'Fully %(keyword)s', 'Partly %(keyword)s'))
					where name='%(name)s'""" % args)

			if update_modified:
				target = frappe.get_doc(args["target_parent_dt"], args["name"])
				target.set_status(update=True)
				target.notify_update()

	def _update_modified(self, args, update_modified):
		args['update_modified'] = ''
		if update_modified:
			args['update_modified'] = ', modified = now(), modified_by = "{0}"'\
				.format(frappe.db.escape(frappe.session.user))

	def update_billing_status_for_zero_amount(self, ref_dt, ref_fieldname):
		zero_amount_refdoc = set([d.get(ref_fieldname) for d in self.get("items", [])
			if d.get(ref_fieldname) and d.base_net_amount == 0])

		for ref_dn in zero_amount_refdoc:
			ref_doc_qty = flt(frappe.db.sql("""
				select ifnull(sum(qty), 0)
				from `tab{0} Item` i, `tab{0}` p
				where i.parent = p.name and p.name=%s and p.docstatus=1
			""".format(ref_dt), ref_dn)[0][0])

			zero_amount_qty = flt(frappe.db.sql("""
				select ifnull(sum(qty), 0)
				from `tab{0} Item` i, `tab{0}` p
				where i.parent = p.name and {1} = %s and i.base_net_amount = 0 and p.docstatus=1 and p.is_return = 0
			""".format(self.doctype, ref_fieldname), ref_dn)[0][0])

			ref_doc = frappe.get_doc(ref_dt, ref_dn)
			if zero_amount_qty >= ref_doc_qty:
				ref_doc.db_set("per_completed", 100)
			else:
				ref_doc.update_billing_percentage()

			ref_doc.set_status(update=True)

def get_tolerance_for(item_code, item_tolerance={}, global_tolerance=None):
	"""
		Returns the tolerance for the item, if not set, returns global tolerance
	"""
	if item_tolerance.get(item_code):
		return item_tolerance[item_code], item_tolerance, global_tolerance

	tolerance = flt(frappe.db.get_value('Item',item_code,'tolerance') or 0)

	if not tolerance:
		if global_tolerance == None:
			global_tolerance = flt(frappe.db.get_value('Stock Settings', None, 'tolerance'))
		tolerance = global_tolerance

	item_tolerance[item_code] = tolerance
	return tolerance, item_tolerance, global_tolerance
