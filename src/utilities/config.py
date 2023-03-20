from __future__ import annotations

import os
import json

from . import get_script_dir


class Config:
    """Настройки проекта"""

    """Настройки"""
    settings: dict

    """Объект класса"""
    __instance: Config = None

    """Текущая директория скрипта"""
    DIR: str = os.getcwd()

    '''Текущая директория папки хранения настроек'''
    DIR_SETTINGS: str = os.path.join(DIR, 'solverAnagram')

    '''Текущий путь для файла настроек'''
    DIR_SETTINGS_FILE: str = os.path.join(DIR_SETTINGS, "settings.json")

    '''Изначальные настройки программы'''
    DEFAULT_SETTINGS = {
        'servers': {},
    }

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Config, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> Config:
        if Config.__instance:
            self.settings = self.get_conf()

    def add_server(self, name, path):
        self.settings['servers'][name] = os.path.join(path, r'logs\latest.log')
        self.save_conf()

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Config()
        return cls.__instance

    def get_conf(self) -> set | bool:
        """
        Получить объект настроек.
        :return: настройки или False
        """
        if self.check_file():
            with open(self.DIR_SETTINGS_FILE, "r") as read_file:
                config = json.load(read_file)
            if len(config) == 0:
                config = self.DEFAULT_SETTINGS
            return config

    def save_conf(self) -> None:
        """ Сохранение настроек """
        with open(self.DIR_SETTINGS_FILE, "w") as write_file:
            json.dump(self.settings, write_file, indent=4)

    def check_file(self) -> bool:
        """
        Проверяет есть ли файл настроек.

        :rtype: bool
        :returns: True если файл настроек есть
        """
        if os.path.isdir(self.DIR):
            if os.path.isdir(self.DIR_SETTINGS):
                if os.path.exists(self.DIR_SETTINGS_FILE):
                    return True
                else:
                    self.settings = self.DEFAULT_SETTINGS
                    self.save_conf()
                    self.check_file()
            else:
                os.makedirs(self.DIR_SETTINGS)
                self.check_file()
        else:
            return False
