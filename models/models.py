# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class new(models.Model):
     _name = 'new.new'
     _description = 'new.new'
      
     name = fields.Char('Name')
     date = fields.Date(string='Date', readonly="True")
     state = fields.Char('State')

     def cnfrm(self):
         self.date=date.today()
         self.state="SUCCESS"


     
