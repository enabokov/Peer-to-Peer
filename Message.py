
commands = ['__GET_LOG__', '__SEND_LOG__', '__GET_FILE__', '__SEND_FILE__',
            '__GET_BLOCK__', '__SEND_BLOCK__', '__CREATE_FILE__', '__APPEND_TO_FILE__']


class Message:

    def __init__(self):
        self.my_ip = ''
        self.other_ip = ''
        self.path_folder = ''

    def get_log(self):
        command = commands[0]
        return command, 0

    def send_log(self, my_log):
        command = commands[1]
        return command, my_log

    def get_file(self, rel_path_file):
        command = commands[2]
        return command, rel_path_file

    def send_file(self, rel_path_file, file):
        command = commands[3]
        return command, rel_path_file, file

    def get_block(self, block_obj):
        command = commands[4]
        return command, block_obj

    def send_block(self, block):
        command = commands[5]
        return command, block

    def create_file(self, path):
        command = commands[6]
        return command, path

    def append_to_file(self, path, data):
        command = commands[7]
        return command, path, data