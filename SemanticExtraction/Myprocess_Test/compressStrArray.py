import io
import numpy as np

x = np.ones(10)

f = io.BytesIO
np.save(f, x)
f.seek(0)
out = f.read()

print(out)