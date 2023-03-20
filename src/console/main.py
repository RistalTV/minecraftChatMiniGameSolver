from src import minecraft
from src.utilities import Config, clear


def main():
    config = Config()
    servers = config.settings['servers']
    server_name: str = None
    server_path: str = None
    print('Программа решения анаграмм и алгоритмических задач запустилась ...\n' + '-' * 80)
    print("Выберите сервер или добавьте его")
    for id, server in enumerate(servers.keys()):
        print(f"{id + 1}) {server}")
    print("\n0) Добавление сервера\n" + '-' * 80)
    while True:
        inp = int(''.join(filter(str.isdigit, "0"+str(input("Введите число: ")))))
        if inp == 0:  # добавление сервера
            clear()
            print("Начат процесс добавления сервера ...")
            name = input("Введите имя сервера: ")
            print("  # Пример пути к серверу")
            print(r"  # D:\Roaming\НазваниеПроекта\updates\НазваниеСервера")
            path = input("Введите путь к серверу:")
            config.add_server(name, path)
            main()
            break
        elif 0 < inp < len(servers.keys()) + 1:
            server_name = list(servers.keys())[inp-1]
            server_path = servers[server_name]
            break
    print(f"Начат поиск мини-игр на сервере {server_name}")

    while True:
        minecraft.seeChat(
            function=minecraft.handlerChat,
            path=server_path
        )
        # sleep(2)
