from TextFromVoice import getVoiceFromText
from playAudio import play_audio
from ctypes import windll, Structure, c_byte, c_ulong, byref

class _SYSTEM_POWER_STATUS(Structure):
        _fields_ = [
            ('ACLineStatus', c_byte),
            ('BatteryFlag', c_byte),
            ('BatteryLifePercent', c_byte),
            ('Reserved1', c_byte),
            ('BatteryLifeTime', c_ulong),
            ('BatteryFullLifeTime', c_ulong)
        ]

def charge_status():
    

    system_power_status = _SYSTEM_POWER_STATUS()
    result = windll.kernel32.GetSystemPowerStatus(byref(system_power_status))

    #charge = system_power_status.BatteryLifePercent
    charge = 100

    if (charge == 100):
        getVoiceFromText(text = "nVoice полностью зар+яжен!")

    elif (charge >= 75):
        getVoiceFromText(text= "nVoice достаточно зар+яжен, все отлично!")
    
    elif (charge >= 60):
        getVoiceFromText(text= "nVoice зар+яжен более чем на половину,- не беспок+ойтесь!")

    elif (charge  < 60 and charge >=40):
        getVoiceFromText(text= "nVoice зар+яжен на половину.")

    elif (charge < 40 and charge >= 20):
        getVoiceFromText(text= "nVoice зар+яжен менее чем на 40%.")

    elif (charge < 20 and charge >10):
        getVoiceFromText(text= "nVoice зар+яжен менее чем на 20%")

    elif (charge <= 10 and charge > 6):
        getVoiceFromText(text= "nVoice зар+яжен менее чем на 10%,- стоит поискать розетку!")
    
    elif (charge >= 5):
        getVoiceFromText(text= "nVoice почти разр+яжен, заряда акуммулятора осталось менее чем 5%! !")

    play_audio()

def accurate_charge_percent ():

    system_power_status = _SYSTEM_POWER_STATUS()
    result = windll.kernel32.GetSystemPowerStatus(byref(system_power_status))

    charge = system_power_status.BatteryLifePercent

    getVoiceFromText("Заряд nVoice равен {}%".format(charge))
    play_audio()

#accurate_charge_percent()
charge_status()

