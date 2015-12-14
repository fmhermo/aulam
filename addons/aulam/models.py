# -*- coding: utf-8 -*-

from openerp import models, fields

class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    lopd = fields.Char()
            
class aulamAlumno(models.Model):
    _name = 'aulam.alumno'
    #_inherit = 'aulam.persona'
    #_inherit = 'res.partner'
    id_partner = fields.Many2one('res.partner',required=True)
    id_colegio = fields.Many2one('aulam.colegio','Colegio')
    id_tarifa = fields.Many2one('aulam.tarifa','Tarifa')
    id_curso = fields.Many2one('aulam.curso','Curso')
    id_calificacion = fields.One2many('aulam.calificacion','id_alumno','Calificacion')
    id_horario = fields.One2many('aulam.horario','id_alumno','Horario')
    fAlta = fields.Date(string="Fecha de Alta")
    fBaja = fields.Date(string="Fecha de Baja")
    hExtra = fields.Float(string="Horas Extra")
    anno = fields.Char("Año académico")
    asignaturas = fields.Char(string="Asignaturas")
    mobile = fields.Char("Móvil", related='id_partner.mobile')
    id_tutor1 = fields.Many2one('res.partner',required=True)
    _rec_name = 'id_partner'


class aulamColegio(models.Model):
    _name = 'aulam.colegio'
    nomColegio = fields.Char(string="Nombre del colegio")
    email = fields.Char(string="Correo Electrónico")
    tlf = fields.Char(string="Teléfono")
    _rec_name = 'nomColegio'

class aulamCurso(models.Model):
    _name = 'aulam.curso'
    orden = fields.Char(string="Orden de curso")
    ciclo = fields.Char(string="Nombre del ciclo")

    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        res=[]
        for elto in self.browse(cr, uid, ids,context=context):
            res.append((elto.id, elto.orden + ' de ' + elto.ciclo))    
        return res

class aulamTarifa(models.Model):
    _name = 'aulam.tarifa'
    nomTarifa = fields.Char(string="Tarifa")
    importe = fields.Float(digits=(6, 2), string="Importe")
    _rec_name = 'nomTarifa'
    
class aulamCalificacion(models.Model):
    _name = 'aulam.calificacion'
    id_alumno = fields.Many2one('aulam.alumno','Alumno')
    asignatura = fields.Char(string="Asigantura")
    fecha = fields.Date(string="Fecha de la calificación")
    calificacion = fields.Float(string="Calificación")
    anno = fields.Char(string="Curso Académico")
    
class aulamHorario(models.Model):
    _name = 'aulam.horario'
    id_alumno = fields.Many2one('aulam.alumno','Alumno')
    anno = fields.Char(string="Curso Académico")
    wDay = fields.Char(string="Día de la semana")
    checkin = fields.Char(string="Entrada")
    checkout = fields.Char(string="Salida")

    #partner_id = fields.many2
class aulamFactura(models.Model):
    _name = 'aulam.factura'
    anno = fields.Char()
    numero = fields.Integer()
    fecha = fields.Date()
    concepto = fields.Char()
    importe = fields.Float()
