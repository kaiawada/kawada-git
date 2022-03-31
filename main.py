from mimetypes import init
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')
st.write('Progress bar')
'START!!'

# latest_interation = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_interation.text(f'Iteration{i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)

# 'DONE!!!'


left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容の記載')




# if st.checkbox('Show Image'):
#     img = Image.open('sample_image2.jpg')
#     st.image(img, caption='Kai Awada', use_column_width = True)


# st.write('DataFrame')
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#     columns= ['lat','lon']
# )



#st.table(df.style.highlight_max(axis=0))

# st.map(df)







"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

"""

