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
    dni = fields.Char('DNI')
    fAlta = fields.Date(string="Fecha de Alta")
    fBaja = fields.Date(string="Fecha de Baja")
    hExtra = fields.Float(string="Horas Extra")
    anno = fields.Char("Año académico")
    asignaturas = fields.Char(string="Asignaturas")
    telefono = fields.Char('T. Fijo', related='id_partner.phone')
    movil = fields.Char("Móvil", related='id_partner.mobile')
    nacimiento = fields.Char("F. Nacimiento")
    email = fields.Char('Email', related='id_partner.email')
    domicilio = fields.Char('Direccion', related='id_partner.street')
    cpt = fields.Char('CP', related='id_partner.zip')
    localidad = fields.Char('Localidad', related='id_partner.city')
    observaciones = fields.Text('Observaciones', related='id_partner.comment')
#    foto = fields.binary("Foto", related='id_partner.image')
    id_tutor1 = fields.Many2one('res.partner',required=True)
    id_tutor2 = fields.Many2one('res.partner')
    tlf_t1 = fields.Char('Tlf. tutor', related='id_tutor1.mobile')
    tlf_t2 = fields.Char('Tlf. auxiliar', related='id_tutor2.mobile')
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
