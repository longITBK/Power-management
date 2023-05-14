from PyQt5.QtWidgets import QApplication, QMainWindow
from Forms.Main_Form_Handle import Main_Form_Handle
from PyQt5.QtCore import QTime, QTimer
from datetime import datetime
from PyQt5 import *;

class UI():
    def __init__(self):
        self.mainformUI = QMainWindow()
        self.mainformhandle = Main_Form_Handle(self.mainformUI)
    
        # create a timer
        self.timer = QTimer()
        self.timer.timeout.connect(lambda : self.mainformhandle.Time_Changing())
        self.timer.timeout.connect(lambda : self.mainformhandle.Battery_Details_Updating())        
        self.timer.timeout.connect(lambda : self.mainformhandle.Brightness_value_updating())
        self.timer.timeout.connect(lambda : self.mainformhandle.Get_Power_Mode())
        self.timer.timeout.connect(lambda : self.mainformhandle.Time_Screen_Off_Updating())
        self.timer.timeout.connect(lambda : self.mainformhandle.Automatic_Suspend_Battery_Updating())
        self.timer.timeout.connect(lambda : self.mainformhandle.Automatic_Suspend_Plugin_Updating())
        self.timer.timeout.connect(lambda : self.mainformhandle.Suspend_Battery_Time_Updating())
        self.timer.timeout.connect(lambda : self.mainformhandle.Suspend_Plugin_Time_Updating())
        self.timer.timeout.connect(lambda : self.mainformhandle.Night_Light_Updating())

        #start and update each 1s
        self.timer.start(1000)        
        self.mainformhandle.Battery_Details_Updating()
        self.mainformhandle.Time_Changing()
        self.mainformhandle.Brightness_value_updating()
        self.mainformhandle.Get_Power_Mode()
        self.mainformhandle.Time_Screen_Off_Updating()
        self.mainformhandle.Automatic_Suspend_Battery_Updating()
        self.mainformhandle.Automatic_Suspend_Plugin_Updating()
        self.mainformhandle.Suspend_Battery_Time_Updating()
        self.mainformhandle.Suspend_Plugin_Time_Updating()
        self.mainformhandle.Night_Light_Updating()
        self.mainformUI.show()         

        self.mainformhandle.tabWidget.tabBarClicked.connect(lambda : self.mainformhandle.Schedule_Time_Updating())

        # sleep
        self.mainformhandle.btn_suspend.clicked.connect(self.mainformhandle.suspend_action)
        
        # sleep screen on battery 
        self.mainformhandle.cbb_screen_blank.activated.connect(lambda : self.mainformhandle.Screen_Off())

        # On/Off Automatic suspend on battery power and plugin
        self.mainformhandle.btn_activate_battery.clicked.connect(lambda : self.mainformhandle.Automatic_Suspend_Battery())
        self.mainformhandle.btn_activate_plugin.clicked.connect(lambda : self.mainformhandle.Automatic_Suspend_Plugin())

        # sleep power on battery and plugin
        self.mainformhandle.cbb_plugged_sleep.activated.connect(self.mainformhandle.Suspend_Plugin_Time)
        self.mainformhandle.cbb_battery_sleep.activated.connect(self.mainformhandle.Suspend_Battery_Time)

        # switch power mode
        self.mainformhandle.radio_performance.clicked.connect(self.mainformhandle.Power_Mode)
        self.mainformhandle.radio_balanced.clicked.connect(self.mainformhandle.Power_Mode)
        self.mainformhandle.radio_power_saver.clicked.connect(self.mainformhandle.Power_Mode)

        # turn ON/OFF night light mode
        self.mainformhandle.btn_activate_night_light.clicked.connect(self.mainformhandle.Night_Light_Mode)

        # switch shedule
        self.mainformhandle.cbb_schedule.activated.connect(lambda : self.mainformhandle.Switch_Schedule())

        # set AM/PM format
        self.mainformhandle.btn_Time_Format_From.clicked.connect(lambda : self.mainformhandle.Time_Format_From_Clicking())
        self.mainformhandle.btn_Time_Format_To.clicked.connect(lambda : self.mainformhandle.Time_Format_To_Clicking())

        # OK the time schdule
        self.mainformhandle.btn_OK.clicked.connect(lambda : self.mainformhandle.Set_Times_Night_Light())

        #default low battery warning setting
        self.mainformhandle.default_setting_warning()

        self.mainformhandle.btn_activate_warning_low_battery.clicked.connect(lambda : self.mainformhandle.change_on_off_warning())

if __name__ == "__main__":
    app = QApplication([])

    ui = UI()
    app.exec_()