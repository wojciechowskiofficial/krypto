import numpy as np
import matplotlib.pyplot as plt

class Encoder:
    def __init__(self):
        self.bin_str_list = None
    def encode(self, message: str, image: np.ndarray):
        # run message convertion
        self._convert_message_to_bits(message)
        # remember original image shape
        og_shape = image.shape
        # flatten the image
        image = image.flatten()
        if self.bin_str_list is None:
            raise ValueError('message is None')
        # add message to the image
        for i in range(len(self.bin_str_list)):
            encoding = bin(image[i])
            encoding = encoding[:-1] + self.bin_str_list[i]
            image[i] = int(encoding, 2)
        image = np.reshape(image, og_shape)
        return image
    def _convert_message_to_bits(self, message: str):
        # add termination mark (@) to message
        message += '@'
        # get ascii
        ascii_list = [ord(character) for character in message]
        # convert decimal to binary
        bin_list = [bin(number) for number in ascii_list]
        #convert binary numbers to string binary numbers
        bin_str_list = [str(number)[2:] for number in bin_list]
        bin_str_list = [number for  number in bin_str_list]
        for i in range(len(bin_str_list)):
            while len(bin_str_list[i]) < 7:
                bin_str_list[i] = '0' + bin_str_list[i]
        bin_str_list = [digit for character in bin_str_list for digit in character]
        self.bin_str_list = bin_str_list

class Decoder:
    def decode(self, image: np.ndarray):
        # flatten the image 
        image = image.flatten()
        # decode the message
        bin_str_list = list()
        acc = str()
        for i in range(image.shape[0]):
            acc += bin(image[i])[-1]
        acc = [acc[i:i + 7] for i in range(0, len(acc), 7)]
        # find end of message id
        termination_id = acc.index('1000000') #0bx1000000 = '@'
        message = acc[:termination_id]
        # convert to text
        message = [int(number, 2) for number in message]
        message = [chr(number) for number in message]
        message = ''.join(message)
        return message
