# Создайте два стека. В одном будет храниться вся история браузера, 
# а во втором — страницы, на которых пользователь нажал кнопку «Назад».
# Если записать их отдельно, получится добавить возможность нажать
# кнопку «Вперед» и вернуться на предыдущую страницу.
class BrowserHistory:
    def __init__(self):
        self.history_stack = [] 
        self.forward_stack = []  

# Создайте функцию, которая сохранит открытую страницу в стек. 
# При этом каждый раз, когда открывается абсолютно новая страница,
# стек со страницами «Вперед» должен очищаться,
# так как начинается новая ветка истории просмотра.
    def open_page(self, url):
        print(f"Открыта страница: {url}")
        self.history_stack.append(url)
        self.forward_stack.clear()

# Создайте функцию, которая извлекает последний элемент 
# из стека общей истории и возвращает пользователя назад, 
# на последний сайт, который был открыт
    def go_back(self):
        if len(self.history_stack) > 1: 
            url = self.history_stack.pop()
            self.forward_stack.append(url)
            print(f"Возвращаемся назад на страницу: {self.history_stack[-1]}")
        else:
            print("История «Назад» пуста")

# Создайте функцию, которая извлекает последний элемент 
# из стека со страницами, к которым можно перейти по кнопке «Вперед»,
# и возвращает пользователя на этот сайт
    def go_forward(self):
        if self.forward_stack:
            url = self.forward_stack.pop()
            self.history_stack.append(url)
            print(f"Переходим вперед на страницу: {url}")
        else:
            print("История «Вперед» пуста")

# Пример использования
if __name__ == "__main__":
    browser_history = BrowserHistory()
    browser_history.open_page("yandex.ru")
    browser_history.open_page("vk.com")
    browser_history.open_page("wikipedia.org")
    browser_history.go_back()  # Вернуться на wikipedia.org
    browser_history.go_back()  # Вернуться на vk.com
    browser_history.go_forward()  # Вперед на wikipedia.org
    browser_history.open_page("mail.ru")  # Открываем новую страницу
    browser_history.go_back()  # Вернуться на wikipedia.org
    browser_history.go_forward()  # Вперед на mail.ru