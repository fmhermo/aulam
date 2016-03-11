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
    
    def _get_annoActual(self, cr, uid, context=None):
        print "Yo!"
        mes = datetime.date.today().month
        anno = datetime.date.today().year
        if mes > 9:
            actual = str(anno) + '-' + str(anno + 1)
        else:
            actual = str(anno - 1) + '-' + str(anno)
        print actual
            
        res = self.pool.get('aulam.season').search(cr, uid, [('anno','=',actual)], context=context)
        return res and res[0] or False   
    
    _defaults = {
        #This makes the function go off that sets EUR.
        'id_season': _get_annoActual
    } 
    #_inherit = 'aulam.persona'
    #_inherit = 'res.partner'
    nomAlumno = fields.Char('Nombre', required=True)
    #id_persona = fields.Many2one('aulam.persona', 'Persona', required=True,)
    #dni = fields.Char('DNI', related='id_persona.dni')
    id_colegio = fields.Many2one('aulam.colegio','Colegio')
    id_tarifa = fields.Many2one('aulam.tarifa','Tarifa')
    id_curso = fields.Many2one('aulam.curso','Curso')
    id_calificacion = fields.One2many('aulam.calificacion','id_alumno','Calificacion')
    id_evaluacion = fields.One2many('aulam.evaluacion','id_alumno','Evaluaciones')
    id_horario = fields.One2many('aulam.horario','id_alumno','Horario')
    id_horariov = fields.One2many('aulam.horariov','id_alumno','Horario de Vacaciones')
    fAlta = fields.Date('Fecha de Alta', required=True)
    fBaja = fields.Date(string='Fecha de Baja')
    hExtra = fields.Float(string='Horas Extra')
    id_season = fields.Many2one('aulam.season', 'Año académico')
    asignaturas = fields.Char(string='Asignaturas')
    #telefono = fields.Char('T. Fijo', related='id_persona.telefono')
    telefono = fields.Char('Teléfono')
    nacimiento = fields.Date('F. Nacimiento')
    lopd = fields.Char()
    #nacimiento = fields.Date('F. Nacimiento', related='id_persona.nacimiento')
    nacimiento = fields.Date('F. Nacimiento')
#    movil = fields.Char('Móvil', related='id_persona.mobile')
    #email = fields.Char('Correo electrónico', related='id_persona.email')
    email = fields.Char('Correo electrónico')
    #domicilio = fields.Char('Direccion', related='id_persona.domicilio')
    domicilio = fields.Char('Direccion')
    cpt = fields.Char('CP', default='15895')
    #localidad = fields.Char('Localidad', related='id_persona.localidad')
    localidad = fields.Char('Localidad', default='Milladoiro')
    #observaciones = fields.Text('Observaciones', related='id_persona.observaciones')
    observaciones = fields.Text('Observaciones')
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
    _rec_name = 'nomAlumno'
    
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
    fecha = fields.Date(string='Fecha')
    calificacion = fields.Float('Calificación', digits=(3,2))
    anno = fields.Char(string='Curso Académico')
    
class aulamEvaluacion(models.Model):
    _name = 'aulam.evaluacion'
    id_alumno = fields.Many2one('aulam.alumno','Alumno')
    id_evaluacion = fields.Selection([('primera', 'Primera'), ('segunda', 'Segunda'), ('tercera', 'Tercera')])
    id_asignatura = fields.Many2one('aulam.asignatura','Asignatura')
    fecha = fields.Date(string='Fecha de la evaluación')
    calificacion = fields.Char('Calificación')
    anno = fields.Char(string='Curso Académico')
    
class aulamHorario(models.Model):
    _name = 'aulam.horario'
    id_alumno = fields.Many2one('aulam.alumno','Alumno')
    anno = fields.Char('Curso Académico')
    wday = fields.Selection([('Lu', 'Lunes'),
                             ('Ma', 'Martes'),
                             ('Mi', 'Miércoles'),
                             ('Ju', 'Jueves'),
                             ('Vi', 'Viernes')])
    #id_wday = fields.Many2one('aulam.wday', 'Día de la semana')
    checkin = fields.Char(string='Entrada')
    checkout = fields.Char(string='Salida')
class aulamHorarioV(models.Model):
    _name = 'aulam.horariov'
    id_alumno = fields.Many2one('aulam.alumno','Alumno')
    anno = fields.Char('Curso Académico')
    wday = fields.Selection([('Lu', 'Lunes'),
                             ('Ma', 'Martes'),
                             ('Mi', 'Miércoles'),
                             ('Ju', 'Jueves'),
                             ('Vi', 'Viernes')])
    #id_wday = fields.Many2one('aulam.wday', 'Día de la semana')
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
    
class aulamSeason(models.Model):
    _name = 'aulam.season'
    anno = fields.Char('Curso Académico')
    _rec_name = 'anno'
    