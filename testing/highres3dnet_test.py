import numpy as np
import tensorflow as tf

from layer.highres3dnet import HighRes3DNet


class HighRes3DNetTest(tf.test.TestCase):
    def test_shape(self):
        input_shape = (2, 32, 32, 32, 1)
        x = tf.ones(input_shape)

        highres_layer = HighRes3DNet(num_classes=5)
        out = highres_layer(x, is_training=True)
        print highres_layer.to_string()

        with self.test_session() as sess:
            sess.run(tf.global_variables_initializer())
            out = sess.run(out)

if __name__ == "__main__":
    tf.test.main()
