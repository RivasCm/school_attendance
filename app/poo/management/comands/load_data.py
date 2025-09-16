# poo/management/commands/load_data.py
import json
from django.core.management.base import BaseCommand
from personal.models import Alumno, Profesor
from school.models import Especialidad, Curso, Materia
from evaluation.models import Nota, ProfesorMateriaCurso
from datetime import date

class Command(BaseCommand):
    help = 'Carga datos de prueba desde un archivo JSON.'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='El nombre del archivo JSON con los datos')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'El archivo {json_file} no fue encontrado.'))
            return

        self.stdout.write(self.style.SUCCESS('Iniciando la carga de datos...'))

        # Cargar Especialidades
        for esp_data in data.get('especialidades', []):
            Especialidad.objects.get_or_create(**esp_data)

        # Cargar Cursos
        for cur_data in data.get('cursos', []):
            Curso.objects.get_or_create(**cur_data)
        
        # Cargar Materias (con relación a Cursos)
        for mat_data in data.get('materias', []):
            curso_nombre = mat_data.pop('curso_nombre')
            try:
                curso = Curso.objects.get(nombre_curso=curso_nombre)
                Materia.objects.get_or_create(id_curso=curso, **mat_data)
            except Curso.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Curso "{curso_nombre}" no encontrado para la materia "{mat_data["nombre_materia"]}". Saltando.'))

        # Cargar Profesores
        for prof_data in data.get('profesores', []):
            esp_nombre = prof_data.pop('especialidad_nombre')
            try:
                especialidad = Especialidad.objects.get(nombre_especialidad=esp_nombre)
                Profesor.objects.get_or_create(id_especialidad=especialidad, **prof_data)
            except Especialidad.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Especialidad "{esp_nombre}" no encontrada para el profesor "{prof_data["nombre"]}". Saltando.'))

        # Cargar Alumnos
        for alu_data in data.get('alumnos', []):
            Alumno.objects.get_or_create(**alu_data)
            
        # Cargar Notas (con relaciones a Alumno y Materia)
        for nota_data in data.get('notas', []):
            alumno_nombre = nota_data.pop('alumno_nombre')
            materia_nombre = nota_data.pop('materia_nombre')
            try:
                alumno = Alumno.objects.get(nombre=alumno_nombre)
                materia = Materia.objects.get(nombre_materia=materia_nombre)
                Nota.objects.get_or_create(id_alumno=alumno, id_materia=materia, **nota_data)
            except (Alumno.DoesNotExist, Materia.DoesNotExist) as e:
                self.stdout.write(self.style.WARNING(f'Error al encontrar Alumno o Materia para una nota. Saltando. Error: {e}'))

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente.'))