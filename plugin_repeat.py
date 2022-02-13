# Повтори за мной
# author: Vetrov Igor

import random
from vacore import VACore

# функция на старте
def start(core:VACore):
    manifest = { # возвращаем настройки плагина - словарь
        "name": "Повтори за мной", # имя
        "version": "1.0", # версия
        "require_online": False, # требует ли онлайн?

        "commands": { # набор скиллов. Фразы скилла разделены | . Если найдены - вызывается функция
            "повтори|повтори за мной": play_repeat,
        }
    }
    return manifest

def play_repeat(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла,
                                              # если юзер сказал больше
                                              # в этом плагине не используется

    core.play_voice_assistant_speech(phrase)
