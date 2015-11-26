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
    fAlta = fields.Date()
    fBaja = fields.Date()
    hExtra = fields.Float()
    anno = fields.Char()
    asignaturas = fields.Char()
    _rec_name = 'id_partner'
    

class aulamColegio(models.Model):
    _name = 'aulam.colegio'
    nomColegio = fields.Char()
    email = fields.Char()
    tlf = fields.Char()
    _rec_name = 'nomColegio'

class aulamCurso(models.Model):
    _name = 'aulam.curso'
    orden = fields.Char()
    ciclo = fields.Char()

class aulamTarifa(models.Model):
    _name = 'aulam.tarifa'
    nomTarifa = fields.Char()
    importe = fields.Float()
    
class aulamCalificacion(models.Model):
    _name = 'aulam.calificacion'
    id_alumno = fields.Many2one('aulam.alumno','Alumno')
    asignatura = fields.Char()
    fecha = fields.Date()
    calificacion = fields.Float()
    anno = fields.Char()
    
class aulamHorario(models.Model):
    _name = 'aulam.horario'
    id_alumno = fields.Many2one('aulam.alumno','Alumno')
    anno = fields.Char()
    wDay = fields.Char()
    checkin = fields.Char()
    checkout = fields.Char()


    #partner_id = fields.many2
class aulamFactura(models.Model):
    _name = 'aulam.factura'
    anno = fields.Char()
    numero = fields.Integer()
    fecha = fields.Date()
    concepto = fields.Char()
    importe = fields.Float()
