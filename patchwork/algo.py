import numpy as np

class Encoder:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.is_seeded = False
    def _get_random_pixel(self, args):
        if self.is_seeded is False:
            raise TypeError('seed the randomizer')
        width, height = args
        return (np.random.randint(0, width), 
                np.random.randint(0, height))
    def encode(self, image: np.ndarray):
        np.random.seed(self.k)
        self.is_seeded = True
        delta = image.itemsize * 8
        acc = 0
        for i in range(self.n):
            pixel_0 = self._get_random_pixel(image.shape)
            pixel_1 = self._get_random_pixel(image.shape)
            acc += image[pixel_0[0]][pixel_0[1]] - image[pixel_1[0]][pixel_1[1]]
            image[pixel_0[0]][pixel_0[1]] += delta
            image[pixel_1[0]][pixel_1[1]] -= delta
        self.S_n = acc
        self.S_n_prim = 2 * delta * self.n + self.S_n
        return image

class Decoder:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.is_seeded = False
    def _get_random_pixel(self, args):
        if self.is_seeded is False:
            raise TypeError('seed the randomizer')
        width, height = args
        return (np.random.randint(0, width), 
                np.random.randint(0, height))
    def decode(self, image: np.ndarray):
        np.random.seed(self.k)
        self.is_seeded = True
        delta = image.itemsize * 8
        acc = 0
        for i in range(self.n):
            pixel_0 = self._get_random_pixel(image.shape)
            pixel_1 = self._get_random_pixel(image.shape)
            acc += image[pixel_0[0]][pixel_0[1]] - image[pixel_1[0]][pixel_1[1]]
            image[pixel_0[0]][pixel_0[1]] -= delta
            image[pixel_1[0]][pixel_1[1]] += delta
        self.S_n = -2 * delta * self.n + acc
        return image
