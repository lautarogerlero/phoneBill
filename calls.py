class Call:
    def __init__(self, duration, extra):
        self.duration = duration
        self.extra = extra


    def getBill(self, duration, extra):
        return duration * extra

    def __str__(self):
        return f"Duration: {self.duration} min \nExtra: {self.extra} \nBill: ${self.getBill(self.duration, self.extra)}"


class Local(Call):
    def __init__(self, duration, extra):
        super().__init__(duration, extra)
        
    def __str__(self):
        return f"Type: Local \n{super().__str__()}"

class National(Call):
    def __init__(self, duration, extra, province):
        super().__init__(duration, extra)
        self.province = province

    def __str__(self):
        return f"Type: National \nProvince: {self.province} \n{super().__str__()}"

class International(Call):
    def __init__(self, duration, extra, country):
        super().__init__(duration, extra)
        self.country = country

    def __str__(self):
        return f"Type: International \nCountry: {self.country} \n{super().__str__()}"



