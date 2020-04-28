from TextFromVoice import getVoiceFromText
from playAudio import play_audio
import time

def localtime():
    localtime = time.asctime( time.localtime(time.time()) )
    correct_time = localtime.split()
    correct_time = correct_time[3].split(':')

    #Для проверки

    #часы 
    #correct_time[0] = 1
    #минуты
    #correct_time[1] = 0
    #секунды
    #correct_time[2] = 0

    #Утро

    if (int(correct_time[0]) >= 4 and int(correct_time[0]) < 13):

        if (int(correct_time[1]) == 0):
            if(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                getVoiceFromText(text= "Сейчас ровно {} утра.".format(int(correct_time[0])))
            else:
                getVoiceFromText(text= "Сейчас ровно {} утра.".format(int(correct_time[0])))

        elif (int(correct_time[2]) == 0):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минута".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минуты".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минут".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

        elif (int(correct_time[2]) <= 4):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минута и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif (int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минуты и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минут и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

        elif (int(correct_time[2]) > 4):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минута и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минуты и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минут и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

    #День

    elif (int(correct_time[0]) >= 13 and int(correct_time[0]) < 17):

        correct_time[0] = int(correct_time[0]) - 12

        if (int(correct_time[1]) == 0):
            if (int(correct_time[0]) == 1):
                getVoiceFromText(text= "Сейчас ровно час дня.")
            elif(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                getVoiceFromText(text= "Сейчас ровно {} часа дня.".format(int(correct_time[0])))
            else:
                getVoiceFromText(text= "Сейчас ровно {} часов дня.".format(int(correct_time[0])))

        elif (int(correct_time[2]) == 0):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минута".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минуты".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минут".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

        elif (int(correct_time[2]) <= 4):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минута и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минуты и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минут и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

        elif (int(correct_time[2]) > 4):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минута и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минуты и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минут и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

    #Вечер

    elif (int(correct_time[0]) >= 17 and int(correct_time[0]) <= 23):

        correct_time[0] = int(correct_time[0]) - 12

        if (int(correct_time[1]) == 0):
            if(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                getVoiceFromText(text= "Сейчас ровно {} вечера.".format(int(correct_time[0])))
            else:
                getVoiceFromText(text= "Сейчас ровно {} вечера.".format(int(correct_time[0])))

        elif (int(correct_time[2]) == 0):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минута".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минуты".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минут".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

        elif (int(correct_time[2]) <= 4):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минута и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минуты и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минут и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

        elif (int(correct_time[2]) > 4):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минута и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минуты и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минут и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

    #Ночь

    elif (int(correct_time[0]) >= 0 and int(correct_time[0]) < 4):

        if (correct_time[0] == 0):
            correct_time[0] = 12

        if (int(correct_time[1]) == 0):
            if (int(correct_time[0]) == 1):
                getVoiceFromText(text= "Сейчас ровно час н+очи.")
            elif(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                getVoiceFromText(text= "Сейчас ровно {} часа н+очи.".format(int(correct_time[0])))
            else:
                getVoiceFromText(text= "Сейчас ровно {} часов н+очи.".format(int(correct_time[0])))

        elif (int(correct_time[2]) == 0):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минута".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минуты".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас ровно {} часов и {} минут".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

        elif (int(correct_time[2]) <= 4):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минута и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минуты и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минут и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

        elif (int(correct_time[2]) > 4):
            if (int(correct_time[1]) == 1):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минута и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            elif(int(correct_time[1]) >= 2 and int(correct_time[1]) <= 4):
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минуты и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))
            else:
                getVoiceFromText(text= "Местное время сейчас {} часов, {} минут и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2])))

    play_audio()