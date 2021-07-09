class Preferences:
    hotkey = ['<Key.ctrl: <59>>', "\'\\x05\'"]  # ctrl + e KeyCode
    hotkey_highlight = []
    super_key = 'command'
    mode = 'advanced'
    appid = ''
    precision = 4  # decimal places
    key_press_pause = 0.02
    highlighting = False  # if true, clicks right arrow after copying

    @staticmethod
    def read(file_path):
        try:
            file = open(file_path, 'r')
        except FileNotFoundError:
            f = open(file_path, 'x')
            f.close()
            Preferences.write(file_path)
            file = open(file_path, 'r')
        lines = file.readlines()
        Preferences.hotkey = list(lines[0][:-1].split(','))
        Preferences.hotkey_highlight = list(lines[1][:-1].split(','))
        Preferences.super_key = lines[2][:-1]
        Preferences.mode = lines[3][:-1]
        Preferences.appid = lines[4][:-1]
        Preferences.precision = int(lines[5])
        Preferences.key_press_pause = float(lines[6])
        Preferences.highlighting = False if lines[7][0] == 'F' else True
        file.close()

    @staticmethod
    def write(file_path):
        file = open(file_path, 'w')
        variables = [','.join(Preferences.hotkey), ','.join(Preferences.hotkey_highlight), Preferences.super_key,
                     Preferences.mode, Preferences.appid, str(Preferences.precision),
                     str(Preferences.key_press_pause), str(Preferences.highlighting)]
        file.write('\n'.join(variables))
        file.close()
