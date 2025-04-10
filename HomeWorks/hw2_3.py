class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, cpu):
        self.__cpu = cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        return {
            'Сумма': self.__cpu + self.__memory,
            'Разность': self.__cpu - self.__memory,
            'Произведение': self.__cpu * self.__memory,
            'Частное': self.__cpu / self.__memory if self.__memory != 0 else 'Деление на 0'
        }

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


    def __str__(self):
        return f'Computer(cpu={self.cpu}, memory={self.memory})'

class Phone:

    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def __str__(self):
        return f'Phone(sim_cards_list = {self.__sim_cards_list})'

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_cards_number, call_to_number):
        if 1 <= sim_cards_number <= len(self.__sim_cards_list):
            provider = self.sim_cards_list[sim_cards_number - 1]
            print(f'Идет звонок на номер {call_to_number} с сим-карты {sim_cards_number} - {provider}')
        else:
            print(f'Ошибка: Неверный номер сим-карты')

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})"


computer = Computer(cpu=4, memory=8)
phone = Phone(sim_cards_list=["Beeline", "Megacom"])
smartphone1 = SmartPhone(cpu=6, memory=16, sim_cards_list=["O!", "Beeline"])
smartphone2 = SmartPhone(cpu=8, memory=32, sim_cards_list=["Megacom"])


print("Информация об объектах:")
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)


print("\n=== Методы Computer ===")
print("make_computations:", computer.make_computations())

print("\n=== Методы Phone ===")
phone.call(1, "+996 777 66 55 44")
phone.call(2, "+996 555 44 24 56")
phone.call(3, "+996 707 00 00 00")  # тест на неправильный номер сим-карты

print("\n=== Методы SmartPhone ===")
smartphone1.use_gps("ЦУМ Бишкек")
print("make_computations:", smartphone1.make_computations())
smartphone1.call(2, "+996 777 11 22 33")

smartphone2.use_gps("Ала-Арча")
smartphone2.call(1, "+996 505 20 40 20")

print("\n=== Сравнение объектов Computer и SmartPhone ===")
print("computer == smartphone1:", computer == smartphone1)
print("computer != smartphone1:", computer != smartphone1)
print("computer < smartphone1:", computer < smartphone1)
print("computer <= smartphone1:", computer <= smartphone1)
print("computer > smartphone1:", computer > smartphone1)
print("computer >= smartphone1:", computer >= smartphone1)













