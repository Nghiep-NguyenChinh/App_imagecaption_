import streamlit as st
import  os
# import requests
# Import libraries
# sys.path.append("app_imagecaption_")
# Images
import PIL.Image
import gdown

url = "https://drive.google.com/uc?id=1-bKUmsoKXAhr-wvlaXqaQxBhEte0fUsB"
output = "model_weights.pt"




#########################################################
##### GIAO DIỆN
#########################################################
st.title("Karim Territory")

st.subheader(" Demo Image Captioning")
st.write("Bắt đầu dowload")
#Ham tải về
##  Kiểm tra file 'name' có tồn tại chưa || không thì kéo nội dung từ link url tạo thành name 
##
def download(url, output):      
    if (os.path.exists(output)==False):
        #st.write("Đang lấy file %s..." % name)
        gdown.download(url, output, quiet=False)


#st.write("Đang lấy file weights...")
download(url, output)

import clip_pre
st.write("Trạng thái: Sẵn sàng")


##################################################################

#################
#### MAIN
################
img_l = st.file_uploader("Upload Image",type=['jpg'])

button = st.button("Bắt đầu tạo caption")
if button:
    clip_pre.upload_image(img_l)

    



