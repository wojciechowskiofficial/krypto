import numpy as np

class SubpixelGenerator:
    def _get_zeros(self):
        return np.full(shape=(2, 2), fill_value=0.)
    def get_leftie(self):
        zeros = self._get_zeros()
        zeros[0][1] = 1.
        zeros[1][1] = 1.
        return zeros
    def get_rightie(self):
        zeros = self._get_zeros()
        zeros[0][0] = 1.
        zeros[1][0] = 1.
        return zeros
        


class Encoder:
    def encode(self, image: np.ndarray):
        (height, width) = image.shape
        #TODO: do the shares but with lists, convert to matrix att the end
        for h in range(height):
            for w in range(width):
                # if black
                if image[h][w] == 0.:
                    sample = np.random.binomial(1, 0.5)
                    # if 0 is sampled then left handside is dark
                    if sample == 0.:
                        #TODO

