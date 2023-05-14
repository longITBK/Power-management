class Scripts():
    def Script_Nightlight_Schedule_From(self):
        return "gsettings get org.gnome.settings-daemon.plugins.color night-light-schedule-from"

    def Script_Nightlight_Schedule_To(self):
        return "gsettings get org.gnome.settings-daemon.plugins.color night-light-schedule-to"

    def Script_Change_Brightness(self, val):
        return "gdbus call --session --dest org.gnome.SettingsDaemon.Power --object-path /org/gnome/SettingsDaemon/Power --method org.freedesktop.DBus.Properties.Set org.gnome.SettingsDaemon.Power.Screen Brightness \"<int32 "+ val +">\""

    def Script_Update_Brightness_Value(self):
        return "gdbus call --session --dest org.gnome.SettingsDaemon.Power --object-path /org/gnome/SettingsDaemon/Power --method org.freedesktop.DBus.Properties.Get org.gnome.SettingsDaemon.Power.Screen Brightness"

    def Script_Show_Battery_Percent(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'percentage:' | cut -d ':' -f 2"

    def Script_Show_State(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'state:' | cut -d ':' -f 2"

    def Script_Show_Technology(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'technology:' | cut -d ':' -f 2"

    def Script_Show_Design_Capacity(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'energy-full-design:' | cut -d ':' -f 2"

    def Script_Show_Full_Charge_Capacity(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'energy-full:' | cut -d ':' -f 2"

    def Script_Show_Current_Capacity(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'energy:' | cut -d ':' -f 2"

    def Script_Show_Time_Left(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'time to empty:' | cut -d ':' -f 2"

    def Script_Show_Time_To_Full(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'time to empty:' | cut -d ':' -f 2"

    def Script_Show_Voltage(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'voltage:' | cut -d ':' -f 2"
    
    def Script_Show_Charge_Cycles(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'charge-cycles:' | cut -d ':' -f 2"

    def Script_Show_Charge_Cycles(self):
        return "upower -i `upower -e | grep 'BAT'` | grep 'charge-cycles:' | cut -d ':' -f 2"

    def Script_Get_Time_Screen_Off(self):
        return "gsettings get org.gnome.desktop.session idle-delay"
    
    def Script_Sleep(self):
        return "systemctl suspend -i"
    
    def Script_Set_Time_Screen_Off(self, second):
        return "gsettings set org.gnome.desktop.session idle-delay " + str(second)

    def Script_Turn_On_Automatic_Suspend_Battery(self):
        return "gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'suspend'"

    def Script_Turn_Off_Automatic_Suspend_Battery(self):
        return "gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'nothing'"
    
    def Script_Get_State_Automatic_Suspend_Battery(self):
        return "gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type"

    def Script_Turn_On_Automatic_Suspend_Plugin(self):
        return "gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'suspend'"

    def Script_Turn_Off_Automatic_Suspend_Plugin(self):
        return "gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'"

    def Script_Get_State_Automatic_Suspend_Plugin(self):
        return "gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type"

    def Script_Set_Time_Automatic_Suspend_Battery(self, second):
        return "gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout "+str(second)
    
    def Script_Get_Time_Automatic_Suspend_Battery(self):
        return "gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout"

    def Script_Set_Time_Automatic_Suspend_Plugin(self, second):
        return "gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout "+str(second)
    
    def Script_Get_Time_Automatic_Suspend_Plugin(self):
        return "gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout"
    
    def Script_Get_Power_Mode(self):
        return "gdbus introspect --system --dest net.hadess.PowerProfiles --object-path /net/hadess/PowerProfiles | grep 'readwrite s ActiveProfile =' | cut -d '=' -f 2"

    def Script_Set_Power_Mode(self, s):
        if s==1:
            return "powerprofilesctl set performance"
        elif s==2:
            return "powerprofilesctl set balanced"
        elif s==3:
            return "powerprofilesctl set power-saver"
    
    def Script_Turn_Night_Light_Mode(self, s):
        if s==0:
            return "gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled true"
        elif s==1:
            return "gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled false"
    
    def Script_Get_Night_Light_State(self):
        return "gsettings get org.gnome.settings-daemon.plugins.color night-light-enabled"

    def Script_Get_Value_of_Temperateur(self):
        return "gsettings get org.gnome.settings-daemon.plugins.color night-light-temperature"

    def Script_Get_Schedule_Mode(self):
        return "gsettings get org.gnome.settings-daemon.plugins.color night-light-schedule-automatic"

    def Script_Change_Temperateur(self, val):
        return "gsettings set org.gnome.settings-daemon.plugins.color night-light-temperature " + val

    def Script_Switch_Schedule(self, s):
        if s==0:
            return "gsettings set org.gnome.settings-daemon.plugins.color night-light-schedule-automatic false"
        elif s==1:
            return "gsettings set org.gnome.settings-daemon.plugins.color night-light-schedule-automatic true"

    def Script_Set_Time_Night_Light_From(self, time):
        return "gsettings set org.gnome.settings-daemon.plugins.color night-light-schedule-from "+str(time)

    def Script_Set_Time_Night_Light_To(self, time):
        return "gsettings set org.gnome.settings-daemon.plugins.color night-light-schedule-to "+str(time)