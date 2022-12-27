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
            print(x["text"] + " ")
            return x["text"]
            break
    stream.stop_stream()
    stream.close()
    p.terminate()
    return input('Say: ')


# настройки
opts = {
    "alias": ('жека', 'жень', 'холоп', 'братан', 'евгений', 'джек', 'жака', 'джека'),
    "tbr": ('включи', 'ключи', 'включить', 'ключе', 'легче', 'ключ'),
    "cmds1": (
    'привет', 'включи красный', 'включи оранжевый', 'включи желтый', 'включи зеленый', 'включи голубой', 'включи синий',
    'включи фиолетовый', 'включи ультрафиолет', 'закат', 'турция', 'день', 'ночь', 'мальдивы'),
    "cmds": (
    'привет', 'красный', 'оранжевый', 'жёлтый', 'зелёный', 'голубой', 'синий',
    'фиолетовый', 'ультрафиолет', 'закат', 'турция', 'мальдивы', 'работа', 'чтение', 'отдых')

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
            # cmd = recognize_cmd(cmd)
        if voice.startswith(opts["tbr"]):
            for x in opts['tbr']:
                #print('трабл')
                cmd = cmd.replace(x, "").strip()
            print("отсек слово включть")
        #print("Работаем1 " + cmd)
        cmd = match_two_words(cmd)
        print("Итоговая команда: " + cmd)
        execute_cmd(cmd)

    except:
        print("Неизвестная ошибка, повторите попытку!")


def match_two_words(word_1):
    print("Ok")
    for v in opts['cmds']:
        number = damerau_levenshtein_distance(word_1, v)
        if number <= 3:
            cmd = v
            return cmd

    # Считаем что разница в 3 символа и меньше еще нормальная
    return word_1

def execute_cmd(cmd):
    if cmd == "привет":
        print("салам")
        say_message("салам")

    elif cmd == 'что по чем':
        print("сотка")
        say_message("сотка")

    elif cmd == 'красный':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("r", encoding='utf-8')
        ard.write(b)
        print("color: red")

    elif cmd == 'оранжевый':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("o", encoding='utf-8')
        ard.write(b)
        print("color: orange")

    elif cmd == 'жёлтый':
        print("будет сделано")
        say_message("будет сделано")
        b = bytes("y", encoding='utf-8')
        ard.write(b)

        print("color: yellow")

    elif cmd == 'зелёный':
        print("принято, выполняю")
        say_message("слушаюсь и повинуюсь")
        b = bytes("g", encoding='utf-8')
        ard.write(b)
        print("color: green")

    elif cmd == 'голубой':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("e", encoding='utf-8')
        ard.write(b)
        print("color: eblue")

    elif cmd == 'синий':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("b", encoding='utf-8')
        ard.write(b)
        print("color: blue")

    elif cmd == 'фиолетовый':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("p", encoding='utf-8')
        ard.write(b)
        print("color: perpule")

    elif cmd == 'работа':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("d", encoding='utf-8')
        ard.write(b)
        print("color: day")

    elif cmd == 'ночь':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("n", encoding='utf-8')
        ard.write(b)
        print("color: night")

    elif cmd == 'турция':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("t", encoding='utf-8')
        ard.write(b)
        print("color: turcey")

    elif cmd == 'мальдивы':
        print("принято, выполняю")
        say_message("принято, ща все будет")
        b = bytes("m", encoding='utf-8')
        ard.write(b)
        print("color: maldivi")

    elif cmd == 'закат':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("z", encoding='utf-8')
        ard.write(b)
        print("color: zakat")

    elif cmd == 'ультрафиолет':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("u", encoding='utf-8')
        ard.write(b)
        print("color: ultra")

    elif cmd == 'чтение':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("a", encoding='utf-8')
        ard.write(b)
        print("color: read")
        
    elif cmd == 'отдых':
        print("принято, выполняю")
        say_message("принято, выполняю")
        b = bytes("x", encoding='utf-8')
        ard.write(b)
        print("color: relax")


    elif cmd == 'шутку':
        # рассказать анекдот
        print("Мой разработчик не научил меня анекдотам ... Ха ха ха")
        say_message("Мой разработчик не научил меня анекдотам... Ха ха ха")

    elif cmd == 'стоп':
        say_message('Чтобы зпустить работу скажите поехали.')


    elif cmd == 'поехали':
        say_message("Можете говорить команды")

    elif cmd == '':
        pass

    else:
        serial.reset_input_buffer()
        say_message('Команда неверна, повторите!')

def seфrch_word(text):
    test = text.split()
    for word in test:
        if word in opts["cmds"]:
            return word
    return "error"

def say_message(message):
    os.system(f"festival -b '(begin (voice_msu_ru_nsh_clunits) (SayText \"{message}\"))'")
    print("Жека: " + message)


if __name__ == '__main__':
    port = '/dev/ttyUSB1'
    ard = serial.Serial(port, 9600)
    message = "Добрый день, я готов к работе."
    os.system(f"festival -b '(begin (voice_msu_ru_nsh_clunits) (SayText \"{message}\"))'")
    command_last = ""
    flag = 1
    while True:
        print("Начало")
        # command = input()

        while flag == 1:
            command = listen_command()
            if command == "поехали":
                flag = 0
                b = bytes("f", encoding='utf-8')
                ard.write(b)
                message = "Готов к работе. Назовите команду."
                os.system(f"festival -b '(begin (voice_msu_ru_nsh_clunits) (SayText \"{message}\"))'")

                break
        command = listen_command()
        print("Считывание команды произошло")

        if command == "стоп" or command == "что" or command == "остановись" or command == "тихо":
            flag = 1
            say_message("Завершение работы, хорошего дня. В следующий раз скажите поехали, и я включу нужный свет.")


        elif command != command_last:
            callback(command)
            command_last = command
            print("Работаем " + command)
            
