class Word:
    def __init__(self, data):
        self.bytes_list = []
        self.value = 0

        if isinstance(data, str):
            if len(data) != 4:
                raise ValueError("Word must be 4 characters long")
            for char in data:
                self.bytes_list.append(ord(char))
            #little endian
            self.value = self.bytes_list[0] | (self.bytes_list[1] << 8) | (self.bytes_list[2] << 16) | (self.bytes_list[3] << 24)
        elif isinstance(data, int):
            if data < 0 or data > 0xFFFFFFFF:
                raise ValueError("Word must be between 0 and 0xFFFFFFFF")
            self.value = data
            #little endian
            self.bytes_list = [data & 0xFF, (data >> 8) & 0xFF, (data >> 16) & 0xFF, (data >> 24) & 0xFF]
        else:
            raise ValueError("Word must be initialized with a string or integer")
    
    def get_value(self):
        return hex(self.value)
    
    def get_string(self):
        return "".join(chr(byte) for byte in self.bytes_list)

    def get_bytes_list(self):
        return self.bytes_list

    def __add__(self, other: 'Word'):
        return Word((self.value + other.value) & 0xFFFFFFFF)
    
    def __xor__(self, other: 'Word'):
        return Word(self.value ^ other.value)
    
    def __lshift__(self, other: int):
        return Word((self.value << other) & 0xFFFFFFFF)