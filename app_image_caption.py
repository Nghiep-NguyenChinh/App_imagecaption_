import streamlit as st
import  os
import requests
# Import libraries
# sys.path.append("app_imagecaption_")





#########################################################
##### GIAO DIỆN
#########################################################
#st.title("**OBJECT DETECTION**")
st.markdown("<h1 style='text-align: center;'>IMAGE CAPTIONING</h1>", unsafe_allow_html=True)
st.markdown("""

|Menter   | Huỳnh Trọng Nghĩa  |
|:-------:|:------------------:|
| Mentees |Nguyễn Chính Nghiệp  |
|         |Hà Sơn Tùng         |
"""
            
            , unsafe_allow_html=True)

st.write("Bắt đầu dowload")
#Ham tải về
##  Kiểm tra file 'name' có tồn tại chưa || không thì kéo nội dung từ link url tạo thành name 
##
def download(url, name):      
    if (os.path.exists(name)==False):
        #st.write("Đang lấy file %s..." % name)
        w = requests.get(url).content  # lấy nội dung url
        with open(name,'wb') as f:
            st.write(f.write(w))   # in ra màn hình
        f.close()
#     else:
#         st.write("Đã tìm thấy file %s!" % name)


#st.write("Đang lấy file weights...")
download('https://archive.org/download/model_wieghts/model_clip/model_wieghts.pt',"model_weights.pt")

import clip_pre
st.write("Trạng thái: Sẵn sàng")


option = st.selectbox('Chọn model',('CLIP_', 'Yolov4'))
#st.write('You selected:', option)

##################################################################

#################
#### MAIN
################
img_l = st.file_uploader("Upload Image",type=['jpg'])


button = st.button("Bắt đầu tạo caption")

if button:
    clip_pre.upload_image(img_l)



