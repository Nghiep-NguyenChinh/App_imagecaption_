import streamlit as st
import  os
# Import libraries
sys.path.append("app_imagecaption_")
import clip_pre




#########################################################
##### GIAO DIỆN
#########################################################
#st.title("**OBJECT DETECTION**")
st.markdown("<h1 style='text-align: center;'>OBJECT DETECTION</h1>", unsafe_allow_html=True)
st.markdown("""

|Menter   | Huỳnh Trọng Nghĩa  |
|:-------:|:------------------:|
| Mentees |Nguyễn Chính Nghiệp  |
|         |Hà Sơn Tùng         |
"""
            
            , unsafe_allow_html=True)

st.write("")
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
st.write("Trạng thái: Sẵn sàng")


option = st.selectbox('Chọn model',('Faster-RCNN', 'Yolov4'))
#st.write('You selected:', option)

##################################################################

#################
#### MAIN
################
img_l = st.file_uploader("Upload Image",type=['jpg'])


clip_pre.upload_image(img_l)

btn = st.button("Bắt đầu nhận diện")



