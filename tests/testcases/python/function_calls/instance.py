import tempfile

tf = tempfile.NamedTemporaryFile(mode='wt')
tf.write("foo")
tf.flush()
