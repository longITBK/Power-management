class Support():   
    def Minute_To_Second(self, time):
        switcher={
            'Never': 0,
            '1 minute': 60,
            '2 minutes': 120,
            '3 minutes': 180,
            '4 minutes': 240,
            '5 minutes': 300,
            '8 minutes': 480,
            '10 minutes': 600,
            '12 minutes': 720,
            '15 minutes': 900,
            '30 minutes': 1800,
            '45 minutes': 2700,
            '1 hour': 3600,
            '80 minutes': 4800,
            '90 minutes': 5400,
            '100 minutes': 6000,
            '2 hours': 7200
        }
        return switcher.get(time, "invalid")

    def Second_To_Minute(self, time):
        switcher={
            0: 'Never',
            60: '1 minute',
            120: '2 minutes',
            180: '3 minutes',
            240: '4 minutes',
            300: '5 minutes',
            480: '8 minutes',
            600: '10 minutes',
            720: '12 minutes',
            900: '15 minutes',
            1800: '30 minutes',
            2700: '45 minutes',
            3600: '1 hour',
            4800: '80 minutes',
            5400: '90 minutes',
            6000: '100 minutes',
            7200: '2 hours'
        }
        return switcher.get(time, "invalid")

    def To_Hour_w_Comma(self, hour, minute):
        time = hour + minute/60
        return round(time, 2)

    def Get_Time_From(self):
        hour = self.Hour_From.value()
        minute = self.Minute_From.value()
        if self.btn_Time_Format_From.isChecked():
            time = self.To_Hour_w_Comma(hour, minute)
        else: time = self.To_Hour_w_Comma(hour+12, minute)
        return time

    def Get_Time_To(self):
        hour = self.Hour_To.value()
        minute = self.Minute_To.value()
        if self.btn_Time_Format_To.isChecked():
            time = self.To_Hour_w_Comma(hour, minute)
        else: time = self.To_Hour_w_Comma(hour+12, minute)
        return time