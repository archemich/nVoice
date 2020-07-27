# nVoice
Вам необходимо установить следующее (Используйте команду "pip install ПАКЕТ" терминале 2 - powershell):
Пакеты: 
(pip) requests, pysoundfile, numpy, pyaudio,  psutil, SpeechRecognition, pyglet, fuzzywuzzy, python-Levenshtein, pyowm, 
Adafruit - sensors(
-git clone https://github.com/adafruit/Adafruit/Adafruit_Python_DHT.git
-cd Adafruit_Pyhton_DHT
-sudo python setup.py install)
(apt-get) (1)build-essential python-dev python-openssl  (sensors)

########################################
bluetooth
########################################

sudo apt-get upgrade
sudo apt-get install bluez pulseaudio-module-bluetooth python-gobject python-gobject-2 bluez-tools
sudo usermod -a -G lp имяпользователя(если не меняли - pi)

1) sudo nano /etc/bluetooth/audio.conf
2) Добавляем вот это
Enable=Source,Sink,Media,Socket
3) sudo nano /etc/pulse/daemon.conf
здесь ищем строку «resample-method = speex-float-3». Если в начале этой строки не стоит; — добавляем его.
4) заменяем resample-method = trivial
5) sudo nano /etc/bluetooth/main.conf
6) Тут можем изменить имя устройства на любое другое путём редактирования строки «Name» если перед этой строкой стоит # убираем её и редактируем имя на которое хотим, выглядеть должно примерно вот так "Name=ТутИмяНаАнглийском".

Дальше ищем строку "Class" и если перед ней стоит # убираем, делаем чтобы было вот так

Class=0x20041C
7)Создайте в /etc/init.d/ файл OnBluetooth(sudo nano /etc/init.d/OnBluetooth). В него
впишите это:
touch
8)Создайте в /etc/init.d/ файл OnBluetooth(sudo nano /etc/init.d/OnBluetooth). В него
впишите это:

#!/bin/bash

#Start systemctl service
sudo systemctl start bluetooth

sleep 1

#Start bluetoothctl with discoverable and pairable options
echo -e 'power on\ndiscoverable on\npairable on \t \nquit' | bluetoothctl

9) chmod 755 /etc/init.d/OnBluetooth
10) update-rc.d OnBluetooth enable