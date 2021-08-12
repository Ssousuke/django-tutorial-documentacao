import datetime
from django.test import TestCase
from django.utils import timezone
from polls.models import Question


class QuestionModelTest(TestCase):
    """
    Aqui criamos uma subclasse de django.test.TestCase com um método que cria uma instância de com uma data no futuro.
    Então verificamos a saída  no qual deve ser False.
    """

    def test_publicacoes_recentes_com_datas_futuras(self):
        data = timezone.now() + datetime.timedelta(days=30)
        questao_futura = Question(pub_date=data)
        self.assertIs(questao_futura.was_published_recently(), False)
