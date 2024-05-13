from stos import Stack


class BrowserHistory:
    def __init__(self) -> None:
        self.history = Stack()
        self.current_page = None

    def go_to_page(self, url):
        self.history.push(self.current_page)
        self.current_page = url

    def go_back(self):
        previous_page = self.history.pop()
        if previous_page is not None:
            self.current_page = previous_page

    def print_history(self):
        print("Current page: ", self.current_page)
        print('History: ')
        for page in reversed(self.history.stack):
            print(page)