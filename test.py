from vosk import Model, KaldiRecognizer
import os, json
import pyaudio
import serial
import time
from pyxdameraulevenshtein import damerau_levenshtein_distance

def listen_command():
    model = Model("model")
    rec = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    while True:
        data = stream.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            x = json.loads(rec.Result())
            print(x["text"]+" ")
            return x["text"]
            break

    return input('Say: ')

# настройки
opts = {
    "alias": ('жека', 'жень', 'холоп', 'братан', 'евгений', 'джек'),
    "tbr": ('включи'),
    "cmds": ('привет', 'включи красный', ' включи оранжевый', 'включи желтый', 'включи зеленый', 'включи голубой', 'включи синий', 'включи фиолетовый', 'включи ультрафиолет', 'закат', 'турция', 'день', 'ночь', 'мальдивы')
    }


# функции
def callback(message):
    try:
        voice = message
        print("Распознано: " + voice)
        # обращаются к Жеке
        cmd = voice
        if voice.startswith(opts["alias"]):
            # обращаются к Жеке

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            # print(cmd)
            # Не распознаем и выполняем команду
            #cmd = recognize_cmd(cmd)
        print("Работаем1 " + cmd)
        cmd = match_two_words(cmd)
        print("Работаем2 " + cmd)
        execute_cmd(cmd)

    except:
        print("Неизвестная ошибка, повторите попытку!")

def match_two_words(word_1):
    for v in opts['cmds']:
        number = damerau_levenshtein_distance(word_1, v)
        if number < 3:
            cmd = v
            return cmd

    # Считаем что разница в 2 символа и меньше еще нормальная
    return word_1

def execute_cmd(cmd):

    if cmd == "привет":
        print("салам")
        say_message("салам")

    elif cmd == 'что по чем':
        print("сотка")
        say_message("сотка")

    elif cmd == 'включи красный':
        print("ща")
        say_message("ща")
        b = bytes("r", encoding='utf-8')
        ard.write(b)
        print("color: red")

    elif cmd == 'включи оранжевый':
        print("сек")
        say_message("сек")
        b = bytes("o", encoding='utf-8')
        ard.write(b)
        print("color: orange")

    elif cmd == 'включи желтый':
        print("будет сделано")
        say_message("будет сделано")
        b = bytes("y", encoding='utf-8')
        ard.write(b)
        print("color: yellow")

    elif cmd == 'включи зеленый':
        print("слушаюсь и повинуюсь")
        say_message("слушаюсь и повинуюсь")
        b = bytes("g", encoding='utf-8')
        ard.write(b)
        print("color: green")

    elif cmd == 'включи голубой':
        print("сек")
        say_message("сек")
        b = bytes("e", encoding='utf-8')
        ard.write(b)
        print("color: eblue")

    elif cmd == 'включи синий':
        print("сек")
        say_message("сек")
        b = bytes("b", encoding='utf-8')
        ard.write(b)
        print("color: blue")

    elif cmd == 'включи фиолетовый':
        print("сек")
        say_message("сек")
        b = bytes("p", encoding='utf-8')
        ard.write(b)
        print("color: perpule")

    elif cmd == 'день':
        print("сек")
        say_message("сек")
        b = bytes("d", encoding='utf-8')
        ard.write(b)
        print("color: day")

    elif cmd == 'ночь':
        print("сек")
        say_message("сек")
        b = bytes("n", encoding='utf-8')
        ard.write(b)
        print("color: night")

    elif cmd == 'турция':
        print("сек")
        say_message("сек")
        b = bytes("t", encoding='utf-8')
        ard.write(b)
        print("color: turcey")

    elif cmd == 'мальдивы':
        print("сек")
        say_message("сек")
        b = bytes("m", encoding='utf-8')
        ard.write(b)
        print("color: maldivi")

    elif cmd == 'закат':
        print("сек")
        say_message("сек")
        b = bytes("z", encoding='utf-8')
        ard.write(b)
        print("color: zakat")

    elif cmd == 'ультрафиолет':
        print("сек")
        say_message("сек")
        b = bytes("u", encoding='utf-8')
        ard.write(b)
        print("color: ultra")


    elif cmd == 'шутку':
        # рассказать анекдот
        print("Мой разработчик не научил меня анекдотам ... Ха ха ха")
        say_message("Мой разработчик не научил меня анекдотам... Ха ха ха")

    else:
        say_message('Команда не распознана, повторите!')

def do_this_command(message):
    message = message.lower()
    if "привет" in message:
        say_message("привет от Жеки!")
    elif "день" in message:
        say_message("Всего доброго!")
    elif "ночь" in message:
        say_message("Всего доброго!")
    elif "Включи красный" in message:
        say_message("Всего доброго!")
    elif "Включи синий" in message:
        say_message("Всего доброго!")
    elif "пока" in message:
        say_message("Всего доброго!")
        exit()
    else:
        say_message("введите команду")


def say_message(message):
    os.system(f"festival -b '(begin (voice_msu_ru_nsh_clunits) (SayText \"{message}\"))'")
    print("Жека: " + message)

if __name__=='__main__':
    port = '/dev/ttyUSB0'
    ard = serial.Serial(port, 9600)
    command_last = ""
    while True:
        command = listen_command()
        if command != command_last:
            callback(command)
            command_last = command
            print("Работаем " + command)