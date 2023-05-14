from Forms.Main_Form import Ui_Form
from StyleSheet.Style import Style
from Scripts.Scripts import Scripts
from Support.Support import Support
from Forms.Warning_Form_Handle import Warning_Form_Handle
import psutil
import os
import time
from datetime import datetime
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow
from os.path import abspath
import subprocess

class Main_Form_Handle(Ui_Form, Style, Scripts, Support):
    count = 0
    s = ''
    def __init__(self, form):
        self.setupUi(form)     
        # change brightness
        self.brightness_slider.valueChanged.connect(lambda : self.change_brightness())   
        self.Temperateur_value_Slider.valueChanged.connect(lambda : self.Change_Temperature())
        filename = abspath('./PBL_Image&Icon/icons8-full-battery.gif')
        print(filename)
        self.movie = QMovie(filename)
        self.gif_charging.setMovie(self.movie)
        self.movie.start()      

#CLOCK (start)
    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d" % (hh, mm, ss)

    # update clock
    def Time_Changing(self):
        time = datetime.now()
        formatted_time = time.strftime("%I:%M:%S %p")        
        self.Clock.display(formatted_time)
#CLOCK (end)

#TAB DETAIL (start)
    #Change the brightness of screen
    def change_brightness(self):
        val = str(self.brightness_slider.value())
        subprocess.run(self.Script_Change_Brightness(val), shell=True, stdout=subprocess.PIPE)        

    # update the current value of brightness
    def Brightness_value_updating(self):
        brightness_val = subprocess.run(self.Script_Update_Brightness_Value(), shell=True, stdout=subprocess.PIPE)        
        val = brightness_val.stdout.decode('utf-8').strip()
        val = val.replace("(","").replace('<','').replace('>','').replace(',','').replace(')','')
        self.brightness_slider.setValue(int(val))

    def Battery_Details_Updating(self):       
        # show % battery
        percentage = subprocess.run(self.Script_Show_Battery_Percent(), shell=True, stdout=subprocess.PIPE)
        percentage = int(percentage.stdout.decode('utf-8').strip().replace('%',''))
        self.Percentage_bar.setValue(percentage)
        # show warning low battery dialog
        if self.Percentage_bar.value() <= self. Battery_level.value() and self.count == 0 and self.btn_activate_warning_low_battery.isChecked():
            self.show_warning_dialog()
            self.count += 1
        if self.count == 300:
            self.count = 0
        # show state
        state = subprocess.run(self.Script_Show_State(), shell=True, stdout=subprocess.PIPE)
        self.txt_state.setText(state.stdout.decode('utf-8').strip())

        # show technoly        
        tech = subprocess.run(self.Script_Show_Technology(), shell=True, stdout=subprocess.PIPE)
        self.txt_technology.setText(tech.stdout.decode('utf-8').strip())

        # show design capacity
        design_cap = subprocess.run(self.Script_Show_Design_Capacity(), shell=True, stdout=subprocess.PIPE)
        self.txt_design_capacity.setText(design_cap.stdout.decode('utf-8').strip())

        # show full charge capacity
        full_cap = subprocess.run(self.Script_Show_Full_Charge_Capacity(), shell=True, stdout=subprocess.PIPE)
        self.txt_full_charge_capacity.setText(full_cap.stdout.decode('utf-8').strip())

        # show current capacity
        current_cap = subprocess.run(self.Script_Show_Current_Capacity(), shell=True, stdout=subprocess.PIPE)
        self.txt_current_capacity.setText(current_cap.stdout.decode('utf-8').strip())

        # show time left
        time_left = subprocess.run(self.Script_Show_Time_Left(), shell=True, stdout=subprocess.PIPE)
        self.txt_time_left.setText(time_left.stdout.decode('utf-8').strip())    

        # show time to full
        time_to_full = subprocess.run(self.Script_Show_Time_To_Full(), shell=True, stdout=subprocess.PIPE)
        self.txt_tim_to_full.setText(time_to_full.stdout.decode('utf-8').strip())      

        # show voltage
        voltage = subprocess.run(self.Script_Show_Voltage(), shell=True, stdout=subprocess.PIPE)
        self.txt_voltage.setText(voltage.stdout.decode('utf-8').strip())

        # show charge-cycles
        charge_cycles = subprocess.run(self.Script_Show_Charge_Cycles(), shell=True, stdout=subprocess.PIPE)
        self.txt_charge_cycles.setText(charge_cycles.stdout.decode('utf-8').strip())    

        s = state.stdout.decode('utf-8').strip()
        if s == 'charging':
            self.Show_Charging_Sign()
        elif s == 'fully-charged':
            self.Hide_Charging_Sign()
            self.show_Plugged_Sign()
        elif s == 'discharging':
            self.Hide_Charging_Sign()                
        s = percentage
        if s==100:
            self.Hide_Charging_Sign()

    def Show_Charging_Sign(self):
        self.gif_charging.show()
        self.icon_battery.hide()
        self.icon_lightning.show()
    
    def Hide_Charging_Sign(self):
        self.gif_charging.hide()
        self.icon_battery.show()
        self.icon_lightning.hide()

    def show_Plugged_Sign(self):
        self.icon_lightning.show()
#TAB DETAIL (end)

#TAB OPTIONS (start)
    #update screen time off
    def Time_Screen_Off_Updating(self):
        time = subprocess.run(self.Script_Get_Time_Screen_Off(), shell=True, stdout=subprocess.PIPE)
        time = time.stdout.decode('utf-8').strip().replace('uint32 ', '')   #Get current time to screen off
        minute = self.Second_To_Minute(int(time))
        self.cbb_screen_blank.setCurrentText(minute)

    # action to suspend
    def suspend_action(self):        
        os.system(self.Script_Sleep())

    # set time and off for screen off
    def Screen_Off(self):
        time = self.cbb_screen_blank.currentText()
        second = self.Minute_To_Second(time)
        subprocess.run(self.Script_Set_Time_Screen_Off(second), shell=True, stdout=subprocess.PIPE)

    #ON BATTERY POWER
    # turn on the state of automatic suspend (on battery)
    def Automatic_Suspend_Battery_ON(self):
        self.btn_activate_battery.setStyleSheet(self.Style_Btn_On())
        self.btn_activate_battery.setText('ON')
        subprocess.run(self.Script_Turn_On_Automatic_Suspend_Battery(), shell=True, stdout=subprocess.PIPE)

    # turn off the state of automatic suspend (on battery)
    def Automatic_Suspend_Battery_OFF(self):
        self.btn_activate_battery.setStyleSheet(self.Style_Btn_Off())
        self.btn_activate_battery.setText('OFF')
        subprocess.run(self.Script_Turn_Off_Automatic_Suspend_Battery(), shell=True, stdout=subprocess.PIPE)

    # update the state of automatic suspend mode (on battery)
    def Automatic_Suspend_Battery_Updating(self):
        state = subprocess.run(self.Script_Get_State_Automatic_Suspend_Battery(), shell=True, stdout=subprocess.PIPE)
        state = state.stdout.decode('utf-8').replace("'", "").strip()
        if state == 'nothing':
            self.Automatic_Suspend_Battery_OFF()
        else: self.Automatic_Suspend_Battery_ON()

    # action to turn on/off automatic suspend mode (on battery)
    def Automatic_Suspend_Battery(self):
        if self.btn_activate_battery.isChecked():
            self.Automatic_Suspend_Battery_ON()
        else: self.Automatic_Suspend_Battery_OFF()
    
    # set delay time (on battery)
    def Suspend_Battery_Time(self):    
        time = self.cbb_battery_sleep.currentText()
        second = self.Minute_To_Second(time)
        subprocess.run(self.Script_Set_Time_Automatic_Suspend_Battery(second), shell=True, stdout=subprocess.PIPE)

    # update delay time (on battery)
    def Suspend_Battery_Time_Updating(self):
        time = subprocess.run(self.Script_Get_Time_Automatic_Suspend_Battery(), shell=True, stdout=subprocess.PIPE)
        time = time.stdout.decode('utf-8').strip()
        minute = self.Second_To_Minute(int(time))
        self.cbb_battery_sleep.setCurrentText(minute)

    #PLUGGED IN
    # turn on the state of automatic suspend (plug in)
    def Automatic_Suspend_Plugin_ON(self):
        self.btn_activate_plugin.setStyleSheet(self.Style_Btn_On())
        self.btn_activate_plugin.setText('ON')
        subprocess.run(self.Script_Turn_On_Automatic_Suspend_Plugin(), shell=True, stdout=subprocess.PIPE)

    # turn off the state of automatic suspend (plug in)
    def Automatic_Suspend_Plugin_OFF(self):
        self.btn_activate_plugin.setStyleSheet(self.Style_Btn_Off())
        self.btn_activate_plugin.setText('OFF')
        subprocess.run(self.Script_Turn_Off_Automatic_Suspend_Plugin(), shell=True, stdout=subprocess.PIPE)

    # update the state of automatic suspend mode (plug in)
    def Automatic_Suspend_Plugin_Updating(self):        
        state = subprocess.run(self.Script_Get_State_Automatic_Suspend_Plugin(), shell=True, stdout=subprocess.PIPE)
        state = state.stdout.decode('utf-8').replace("'", "").strip()
        if state == 'nothing':
            self.Automatic_Suspend_Plugin_OFF()
        else: self.Automatic_Suspend_Plugin_ON()

    # action to turn on/off automatic suspend mode (plug in)
    def Automatic_Suspend_Plugin(self):
        if self.btn_activate_plugin.isChecked():
            self.Automatic_Suspend_Plugin_ON()
        else: self.Automatic_Suspend_Plugin_OFF()    

    # set delay time (plug in)
    def Suspend_Plugin_Time(self):    
        time = self.cbb_plugged_sleep.currentText()
        second = self.Minute_To_Second(time)
        subprocess.run(self.Script_Set_Time_Automatic_Suspend_Plugin(), shell=True, stdout=subprocess.PIPE)     

    # update delay time (plug in)
    def Suspend_Plugin_Time_Updating(self):
        time = subprocess.run(self.Script_Get_Time_Automatic_Suspend_Plugin(), shell=True, stdout=subprocess.PIPE)
        time = time.stdout.decode('utf-8').strip()
        minute = self.Second_To_Minute(int(time))
        self.cbb_plugged_sleep.setCurrentText(minute)
#TAB OPTIONS (end)

#TAB MODES (start)
    #Get current power mode
    def Get_Power_Mode(self):        
        mode = subprocess.run(self.Script_Get_Power_Mode(), shell=True, stdout=subprocess.PIPE)
        s = mode.stdout.decode('utf-8').strip().replace("'", '').replace("'", '').replace(';', '')
        if s == 'balanced':
            self.radio_balanced.setChecked(True)
        elif s == 'power-saver':
            self.radio_power_saver.setChecked(True)
        else:
            self.radio_performance.setChecked(True)

    #Set power mode 
    def Power_Mode(self):
        performance = self.radio_performance.isChecked()
        balanced = self.radio_balanced.isChecked()
        power_saver = self.radio_power_saver.isChecked()
        if performance == True:
            os.system(self.Script_Set_Power_Mode(1))
        if balanced == True:
            os.system(self.Script_Set_Power_Mode(2))
        if power_saver == True:
            os.system(self.Script_Set_Power_Mode(3))
#TAB MODES (end)

#TAB NIGHT LIGHT (start)
    # update Time schedule of night light
    def Schedule_Time_Updating(self):           
        if self.tabWidget.currentIndex() >= 0:
            # schedule time from               
            time = subprocess.run(self.Script_Nightlight_Schedule_From(), shell=True, stdout=subprocess.PIPE)
            time = time.stdout.decode('utf-8').strip().split('.')
            hour = int(time[0])
            minute = '0.'+time[1]
            minute = round(float(minute)*60)
            if hour < 12:
                self.btn_Time_Format_From.setChecked(True)
                self.btn_Time_Format_From.setStyleSheet(self.Style_Btn_AM())
                self.btn_Time_Format_From.setText("AM")
            else: 
                self.btn_Time_Format_From.setChecked(False)
                self.btn_Time_Format_From.setText("PM")
                self.btn_Time_Format_From.setStyleSheet(self.Style_Btn_PM())
            if hour == 0 or hour == 12:
                hour = 12                   
            else: hour %= 12                             
            self.Hour_From.setValue(hour)
            self.Minute_From.setValue(minute)

            # schedule time to            
            time = subprocess.run(self.Script_Nightlight_Schedule_To(), shell=True, stdout=subprocess.PIPE)
            time = time.stdout.decode('utf-8').strip().split('.')
            hour = int(time[0])
            minute = '0.'+time[1]
            minute = round(float(minute)*60)
            if hour < 12:
                self.btn_Time_Format_To.setChecked(True)
                self.btn_Time_Format_To.setStyleSheet(self.Style_Btn_AM())
                self.btn_Time_Format_To.setText("AM")
            else: 
                self.btn_Time_Format_To.setChecked(False)
                self.btn_Time_Format_To.setText("PM")
                self.btn_Time_Format_To.setStyleSheet(self.Style_Btn_PM())
            if hour == 0 or hour == 12:
                hour = 12                   
            else: hour %= 12                                             
            self.Hour_To.setValue(hour)
            self.Minute_To.setValue(minute)

    # Turn on night light mode
    def Night_Light_Mode_ON(self):
        self.btn_activate_night_light.setStyleSheet(self.Style_Btn_On())
        self.btn_activate_night_light.setText('ON')
        mode = subprocess.run(self.Script_Turn_Night_Light_Mode(0), shell=True, stdout=subprocess.PIPE)

    # Turn off night light mode
    def Night_Light_Mode_OFF(self):
        self.btn_activate_night_light.setStyleSheet(self.Style_Btn_Off())
        self.btn_activate_night_light.setText('OFF')
        mode = subprocess.run(self.Script_Turn_Night_Light_Mode(1), shell=True, stdout=subprocess.PIPE)

    # update Night Light ...
    def Night_Light_Updating(self):
        # state of night light (on/off)
        mode = subprocess.run(self.Script_Get_Night_Light_State(), shell=True, stdout=subprocess.PIPE)
        mode = mode.stdout.decode('utf-8').strip()
        if mode == 'true':
            self.Night_Light_Mode_ON()
        else: self.Night_Light_Mode_OFF()
        # value of temperature
        val = subprocess.run(self.Script_Get_Value_of_Temperateur(), shell=True, stdout=subprocess.PIPE)
        val = val.stdout.decode('utf-8').strip().replace('uint32 ', '')
        self.Temperateur_value_Slider.setValue(int(val))
        # schedule mode
        mode = subprocess.run(self.Script_Get_Schedule_Mode(), shell=True, stdout=subprocess.PIPE)
        mode = mode.stdout.decode('utf-8').strip()
        if mode == 'true':
            self.cbb_schedule.setCurrentText('Sunset to Sunrise')
            self.hide_Time_Schedule()
        else: 
            self.cbb_schedule.setCurrentText('Manual Schedule')        
            self.show_Time_Schedule()

    # ON/OFF night light mode
    def Night_Light_Mode(self):
        if self.btn_activate_night_light.isChecked():
            self.Night_Light_Mode_ON()
        else: self.Night_Light_Mode_OFF()

    # change warm color
    def Change_Temperature(self):
        val = str(self.Temperateur_value_Slider.value())
        subprocess.run(self.Script_Change_Temperateur(val), shell=True, stdout=subprocess.PIPE)
    
    # show time schedule
    def show_Time_Schedule(self):
        self.frame_3.show()

    # hide time schedule
    def hide_Time_Schedule(self):
        self.frame_3.hide()

    # switch the schedule mode
    def Switch_Schedule(self):
        sche = self.cbb_schedule.currentText().strip()
        print(sche)
        if sche == 'Manual Schedule':
            subprocess.run(self.Script_Switch_Schedule(0), shell=True, stdout=subprocess.PIPE)
            self.show_Time_Schedule()
        else:
            subprocess.run(self.Script_Switch_Schedule(1), shell=True, stdout=subprocess.PIPE)
            self.hide_Time_Schedule()
    
    #AM/PM time from format
    def Time_Format_From_Clicking(self):        
        if self.btn_Time_Format_From.isChecked():
            self.btn_Time_Format_From.setStyleSheet(self.Style_Btn_AM())
            self.btn_Time_Format_From.setText("AM")
        else: 
            self.btn_Time_Format_From.setText("PM")
            self.btn_Time_Format_From.setStyleSheet(self.Style_Btn_PM())

    #AM/PM time to format
    def Time_Format_To_Clicking(self):
        if self.btn_Time_Format_To.isChecked():
            self.btn_Time_Format_To.setStyleSheet(self.Style_Btn_AM())
            self.btn_Time_Format_To.setText("AM")
        else: 
            self.btn_Time_Format_To.setText("PM")
            self.btn_Time_Format_To.setStyleSheet(self.Style_Btn_PM())

    # set time schedule to activate night light
    def Set_Times_Night_Light(self):
        time_from = self.Get_Time_From()        
        subprocess.run(self.Script_Set_Time_Night_Light_From(time_from), shell=True, stdout=subprocess.PIPE)
        time_to = self.Get_Time_To()
        subprocess.run(self.Script_Set_Time_Night_Light_To(time_to), shell=True, stdout=subprocess.PIPE)
#TAB NIGHT LIGHT (end)

#TAB BATTERY WARNING (start)
    def default_setting_warning(self):
        self.btn_activate_warning_low_battery.setChecked(True)
        self.btn_activate_warning_low_battery.setStyleSheet(self.Style_Btn_On())
        self.btn_activate_warning_low_battery.setText('ON')

        self.txt_state_warning.setText(self.Style_SHOW())

        self.Battery_level.setValue(20)

    #change to show/not show warning low battery dialog
    def change_on_off_warning(self):
        if self.btn_activate_warning_low_battery.isChecked():            
            self.btn_activate_warning_low_battery.setChecked(True)
            self.btn_activate_warning_low_battery.setStyleSheet(self.Style_Btn_On())
            self.btn_activate_warning_low_battery.setText('ON')
            self.txt_state_warning.setText(self.Style_SHOW())            
        else:
            self.btn_activate_warning_low_battery.setChecked(False)
            self.btn_activate_warning_low_battery.setStyleSheet(self.Style_Btn_Off())
            self.btn_activate_warning_low_battery.setText('OFF')
            self.txt_state_warning.setText(self.Style_notSHOW())        

    def show_warning_dialog(self):
        if (self.Percentage_bar.value()<=self.Battery_level.value()):
            self.warningUI = QMainWindow()
            self.warning_form = Warning_Form_Handle(self.warningUI)
            self.warning_form.txt_battery_level.setText(str(self.Percentage_bar.value()) + '%')
            self.warningUI.show()

#TAB BATTERY WARNING (end)

