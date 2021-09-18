class Netbook:
    def __init__(self,model_name):
        self.model = model_name
        self.kharakteristics = []
        self.processor()
        self.ram()
        self.video_card()
        self.HDD()
        self.display_size()

    def processor(self):
        self.kharakteristics.append('Intel® Core™ i5 CPU M 450 @ 2.40GHz × 4 ')

    def ram(self):
        self.kharakteristics.append('4 Гб DDR4')

    def video_card(self):
        self.kharakteristics.append('Mesa Intel HD Graphic')

    def HDD(self):
        self.kharakteristics.append('HHD 1000 Гб')

    def display_size(self):
        self.kharakteristics.append('15,6 FHD')

        netbook = Netbook (model_name = 'Asus')
        print(netbook.model)
        print(netbook.kharakteristics)

    class Lenovo:
        def __init__(self, Процессор, Оперативная_Память, Видеокарта, Жёсткий_Диск, Размер_экрана):
            self.Процессор = Процессор
            self.Оперативная_Память = Оперативная_Память
            self.Видеокарта = Видеокарта
            self.Жёсткий_Диск = Жёсткий_Диск
            self.Размер_экрана = Размер_экрана

        def get_Lenovo_info(self):
            print({'Процессор': self.Процессор, 'Оперативная Память': self.Оперативная_Память,
                   'Видеокарта': self.Видеокарта, 'Жёсткий Диск': self.Жёсткий_Диск,
                   'Размер_экрана': self.Размер_экрана})

    s = Lenovo('Intel® Core™ i5 CPU M450 @ 2.40GHz × 4 ', '4 Гб DDR4', 'Mesa DRI Intel® HD Graphics (ILK)',
               'HHD  1000 GB', '15.6')
    s.get_Lenovo_info()