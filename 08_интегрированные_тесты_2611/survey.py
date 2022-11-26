class Survey:
    """Сбор ответов на вопросы"""
    def __init__(self, question):
        """Запоминает вопрос и создает список для ответов"""
        self.question = question
        self.responses = []
    def show_question(self):
        """Выводит вопрос на консаоль"""
        print(self.question)
    def save_response(self, response):
        """Сохраняет ответ в список"""
        self.responses.append(response)
    def show_result(self):
        print('Survey res:')
        for response in self.responses:
            print(f'- {response}')


