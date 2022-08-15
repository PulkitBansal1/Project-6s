import streamlit as st							#Streamlit allows you to write an app the same way you write a python code.
from pkg.image_processor import processor				#using another file of python that I created

FOOTER_FILE = "layout/src/markdowns/footer.md"			#html file in which the footer of the webpage is defined.

SIDEBAR_OPTIONS = {
    "Home": {								#first sidebar option,ie,home,that is the home page of webpage.
      "page_source": "layout/src/markdowns/home.md"			#the link of the home page file.
    },
    "Image Processing": {						#second sidebar option,ie, image processing, that is the image processing page of webpage where user can edit image.
      "page_source": "layout/src/markdowns/image_processor.md"	#the link of the image processing page file.
    },
    "About Us": {							#third sidebar option,ie, about us,that is information of the webpage.
      "page_source": "layout/src/markdowns/about.md",		#the link of the about us page file.
      "image_source": "layout/src/images/about.jpg"
    },
    "Contact": {							#fourth sidebar option,ie, contact ,that is the details of the creator of webpage.
      "page_source": "layout/src/markdowns/contact.md",		#the link of the contact page file.
      "image_source": "layout/src/images/contact.jpg"
    },
}

IMAGE_OPERATIONS_TO_DISPLAY = {					#operations taht will display on screen of user.
  "convert2sketch": "Convert to Cartoon Sketch",
  "rotate": "Rotate Image",
  "brightness": "Adjust Brightness"
}

def get_image_operation_display(operation):
    return IMAGE_OPERATIONS_TO_DISPLAY[operation]

def get_file_content(file_path):					#gets response(file path).
    response = open(file_path, encoding="utf-8").read()
    return response

def add_title(title):
    st.title(title)

def display_about_image(file_path):
  img = processor.load_image(file_path)
  st.image(img, width=560)
  
def display_contact_image(file_path):					#displays the image on conatct page.
  img = processor.load_image(file_path)
  st.image(img, width=350)
	
def add_common_sidebars():						#sidebar

    st.sidebar.title("Choose one from the following options:")
    selection = st.sidebar.radio("", list(SIDEBAR_OPTIONS.keys()))

    with st.spinner(f"Loading {selection} ..."):
      markdown_content = get_file_content(SIDEBAR_OPTIONS[selection]["page_source"])
      st.markdown(markdown_content, unsafe_allow_html=True)  
      
    if selection == "About Us":
      display_about_image(SIDEBAR_OPTIONS[selection]["image_source"])

    if selection == "Contact":
      display_contact_image(SIDEBAR_OPTIONS[selection]["image_source"])

    if selection == "Image Processing":
      image_file = st.file_uploader("Upload Image", type = ['jpg', 'jpeg'])
      image_operation = st.selectbox(label="Please select one of the following options",
      options=("convert2sketch", "rotate", "brightness"),
      format_func=get_image_operation_display)
      processor.process_image(image_file, image_operation)


def add_common_footer():						#footer
  st.markdown(get_file_content(FOOTER_FILE), unsafe_allow_html=True)
