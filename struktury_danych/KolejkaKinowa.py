from kolejka import Queue

class Customer:
    def __init__(self, name, order):
        self.name = name
        self.order = order

class McDonaldsQueue:
    def __init__(self):
        self.queue = Queue()

    def add_customer(self, imie, zamowienie):
        customer = Customer(imie, zamowienie)
        self.queue.enqueue(customer)

    def remove_customer(self):
        if not self.queue.is_empty():
            return self.queue.dequeue()

    def next_customer_order(self):
        if not self.queue.is_empty():
            next_customer = self.queue.peek()
            return next_customer.order


# Tworzymy kolejkę
mcd_queue = McDonaldsQueue()

# Dodajemy klientów do kolejki
mcd_queue.add_customer("Maciek", 'frytki')
mcd_queue.add_customer("Maks", 'Cheeseburger')
mcd_queue.add_customer("Krystian", 'McRoyal')
mcd_queue.add_customer("Kamil", 'Hamburger')

# Obsługujemy kolejkę
while not mcd_queue.queue.is_empty():
    next_customer = mcd_queue.remove_customer()
    print(f"Obslugujemy klienta o imieniu: {next_customer.name}, który zamówił: {next_customer.order}")

    if not mcd_queue.queue.is_empty():
        next_order = mcd_queue.next_customer_order()
        print(f'Nastpny klient zamówił {next_order} \n')
