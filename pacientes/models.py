from django.db import models

class Paciente(models.Model):
  queixa_choices = (
    ('TDAH', 'TDAH'),
    ('D', 'Depressão'),
    ('A', 'Ansiedade'),
    ('TAG', 'Transtorno de ansiedade generalizada'),
  )
  nome = models.CharField(max_length = 100)
  email = models.EmailField()
  telefone = models.CharField(max_length = 255, null=True, blank=True)
  foto = models.ImageField(upload_to='fotos', null=True, blank=True)
  pagamento_em_dia = models.BooleanField(default=True)
  queixa = models.CharField(max_length = 4, choices=queixa_choices)

  def __str__(self):
    return self.nome