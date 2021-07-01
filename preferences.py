class Preferences:
    hotkey = "\'\\x05\'"  # ctrl + e KeyCode
    hotkey_special_key = '<Key.ctrl: <59>>'
    super_key = 'command'
    mode = 'advanced'
    appid = ''
    precision = 4  # decimal places
    key_press_pause = 0.02
    highlighting = False  # if true, clicks right arrow after copying

    @staticmethod
    def read(file_path):
        file = open(file_path, 'r')
        lines = file.readlines()
        Preferences.hotkey = lines[0][:-1]
        Preferences.hotkey_special_key = lines[1][:-1]
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
        variables = [Preferences.hotkey, Preferences.hotkey_special_key, Preferences.super_key,
                     Preferences.mode, Preferences.appid, str(Preferences.precision),
                     str(Preferences.key_press_pause), str(Preferences.highlighting)]
        file.write('\n'.join(variables))
        file.close()
