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
        share_0 = list()
        share_1 = list()
        sub = SubpixelGenerator()
        for h in range(height):
            for w in range(width):
                sample = np.random.binomial(1, 0.5)
                # if black
                if image[h][w] == 0.:
                    # if 0 is sampled then left handside is dark
                    if sample == 0.:
                        subpixel_0 = sub.get_leftie()
                        subpixel_1 = sub.get_rightie()
                    # if 1 is sampled then right handside is dark
                    else:
                        subpixel_0 = sub.get_rightie()
                        subpixel_1 = sub.get_leftie()
                # if white 
                else:
                    # if 0 is sampled then left handside is dark
                    if sample == 0.:
                        subpixel_0 = sub.get_leftie()
                        subpixel_1 = sub.get_leftie()
                    # if 1 is sampled then right handside is dark
                    else:
                        subpixel_0 = sub.get_rightie()
                        subpixel_1 = sub.get_rightie()
                share_0.append(subpixel_0)
                share_1.append(subpixel_1)
        # reshape share lists into numpy arrays
        rows_0 = list()
        rows_1 = list()
        for i in range(0, height * height, width):
            rows_0.append(share_0[i:i + width])
            rows_1.append(share_1[i:i + width])
        rows_concat_0 = list()
        rows_concat_1 = list()
        for i in range(len(rows_0)):
            rows_concat_0.append(np.concatenate(rows_0[i]))
            rows_concat_1.append(np.concatenate(rows_1[i]))
        share_0 = np.concatenate(rows_concat_0, axis=1)
        share_1 = np.concatenate(rows_concat_1, axis=1)
        return (share_0.transpose(), share_1.transpose())


