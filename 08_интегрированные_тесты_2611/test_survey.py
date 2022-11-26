import unittest
from survey import Survey


class TestSurvey(unittest.TestCase):

    def setUp(self):
        """Создает вопрос и набор ответов для всех тестов"""
        quest = 'What is your favorite prog lang?'
        self.my_surv = Survey(quest)
        self.languages = ['Python', 'C++', 'Swift']

    def test_save_single_response(self):
        self.my_surv.save_response(self.languages[0])  # запишу первый элементт из списка вопросов
        self.assertIn(self.languages[0], self.my_surv.responses)
        """Проверяет наличие первого аргумента внутри 
        коллекции (второго аргумента) - работает как обычный 
        оператор in - проверяет наличие одного элемента 
        в последовательности"""

    def test_save_multiple_responses(self):
        for i in range(len(self.languages)):  # повторить <длина списка ответов>
            self.my_surv.save_response(self.languages[i])  # сохранить каждый ответ в опросе
        for i in range(len(self.languages)):
            self.assertIn(self.languages[i], self.my_surv.responses)


if __name__ == "__main__":
    unittest.main()
