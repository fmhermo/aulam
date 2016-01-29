# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime

#class res_partner(models.Model):
#    _name = 'res.partner'
#    _inherit = 'res.partner'
#    lopd = fields.Char()
#    dni = fields.Char('DNI')

class aulamPersona(models.Model):
    _name = 'aulam.persona'
    
    nomPersona = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    lopd = fields.Char()
    dni = fields.Char('DNI')
    telefono = fields.Char('Teléfonos')
    nacimiento = fields.Date('F. Nacimiento')
    email = fields.Char('Correo electrónico')
    domicilio = fields.Char('Dirección')
    cpt = fields.Char('C. Postal', default='15895')
    localidad = fields.Char('Localidad', default='Milladoiro')
    observaciones = fields.Text('Observaciones')
    _rec_name = 'nomPersona'
    
class aulamAlumno(models.Model):
    _name = 'aulam.alumno'
    
    def annoActual(self):
        mes = datetime.date.today().month
        anno = datetime.date.today().year
        if mes > 9:
            return str(anno) + '-' + str(anno + 1)
        else:
            return str(anno - 1) + '-' + str(anno)    
    #_inherit = 'aulam.persona'
    #_inherit = 'res.partner'
    id_persona = fields.Many2one('aulam.persona', 'Persona', required=True,)
    dni = fields.Char('DNI', related='id_persona.dni')
    id_colegio = fields.Many2one('aulam.colegio','Colegio')
    id_tarifa = fields.Many2one('aulam.tarifa','Tarifa')
    id_curso = fields.Many2one('aulam.curso','Curso')
    id_calificacion = fields.One2many('aulam.calificacion','id_alumno','Calificacion')
    id_horario = fields.One2many('aulam.horario','id_alumno','Horario')
    fAlta = fields.Date('Fecha de Alta', required=True)
    fBaja = fields.Date(string='Fecha de Baja')
    hExtra = fields.Float(string='Horas Extra')
    anno = fields.Char('Año académico', default=annoActual)
    asignaturas = fields.Char(string='Asignaturas')
    telefono = fields.Char('T. Fijo', related='id_persona.telefono')
    nacimiento = fields.Date('F. Nacimiento', related='id_persona.nacimiento')
#    movil = fields.Char('Móvil', related='id_persona.mobile')
    email = fields.Char('Correo electrónico', related='id_persona.email')
    domicilio = fields.Char('Direccion', related='id_persona.domicilio')
    cpt = fields.Char('CP', related='id_persona.cpt')
    localidad = fields.Char('Localidad', related='id_persona.localidad')
    observaciones = fields.Text('Observaciones', related='id_persona.observaciones')
#    foto = fields.binary('Foto', related='id_persona.image')
    id_tutor1 = fields.Many2one('aulam.persona',required=True)
#   tlf_t1 = fields.Char('Tlf. tutor', related='id_tutor1.telefono')
    dni_t1 = fields.Char('DNI tutor', related='id_tutor1.dni')
    id_tutor2 = fields.Many2one('aulam.persona')
#    tlf_t2 = fields.Char('Tlf. auxiliar', related='id_tutor2.telefono')
    #estado = fields.Selection([
    #    ('alta', "Alta"),
    #    ('baja', "Baja"),
    #], default='alta')
    _rec_name = 'id_persona'
    
    #@api.multi
    #def action_alta(self):
    #    self.state = 'alta'
    #def action_baja(self):
    #    self.state = 'baja'
    #    self.dni = '01/02/16'

    #def temporada(self):
    #    return '2015-2016'


class aulamColegio(models.Model):
    _name = 'aulam.colegio'
    nomColegio = fields.Char('Nombre del colegio', required=True)
    email = fields.Char('Correo Electrónico')
    tlf = fields.Char('Teléfono')
    _rec_name = 'nomColegio'

class aulamCurso(models.Model):
    _name = 'aulam.curso'
    nomCurso = fields.Char('Curso', required=True)
    _rec_name = 'nomCurso'
    
    # Esta función reemplaza el rec_name con su resultado
    #def name_get(self, cr, uid, ids, context={}):
    #    if not len(ids):
    #        return []
    #    res=[]
    #    for elto in self.browse(cr, uid, ids,context=context):
    #        res.append((elto.id, elto.orden + ' de ' + elto.ciclo))    
    #    return res#
    #def _compute_name(self):
    #    self.name = "Record with value %s" % self.value
#@    @api.one
#@def _compute_name(self):
#@    self.name = str(random.randint(1, 1e6))

class aulamTarifa(models.Model):
    _name = 'aulam.tarifa'
    nomTarifa = fields.Char('Tarifa', required=True)
    importe = fields.Float('Importe', digits=(6,2))
    _rec_name = 'nomTarifa'
    
class aulamCalificacion(models.Model):
    _name = 'aulam.calificacion'
    id_alumno = fields.Many2one('aulam.alumno','Alumno')
    id_asignatura = fields.Many2one('aulam.asignatura','Asignatura')
    fecha = fields.Date(string='Fecha de la calificación')
    calificacion = fields.Float('Calificación', digits=(3,2))
    anno = fields.Char(string='Curso Académico')
    
class aulamHorario(models.Model):
    _name = 'aulam.horario'
    id_alumno = fields.Many2one('aulam.alumno','Alumno')
    anno = fields.Char('Curso Académico')
    id_wday = fields.Many2one('aulam.wday', 'Día de la semana')
    checkin = fields.Char(string='Entrada')
    checkout = fields.Char(string='Salida')

    #partner_id = fields.many2
class aulamFactura(models.Model):
    _name = 'aulam.factura'
    anno = fields.Char()
    numero = fields.Integer()
    fecha = fields.Date()
    concepto = fields.Char()
    importe = fields.Float()
    
class aulamAsignatura(models.Model):
    _name = 'aulam.asignatura'
    nomAsignatura = fields.Char('Asignatura')
    _rec_name = 'nomAsignatura'
    
class wday(models.Model):
    _name = 'aulam.wday'
    wd = fields.Char('Abreviatura')
    weekday = fields.Char('Día de la semana')
    _rec_name = 'wd'