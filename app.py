import streamlit as st
import PIL
import google.generativeai as genai

# Function to process image and text using AI model
def process_image(image, text):
    genai.configure(api_key="")
    img = PIL.Image.open(image)
    img.thumbnail((200, 200))  # Resize the image to a smaller size
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([text, img])
    response.resolve()
    return response.text.lower()

# Streamlit app title
st.title("Conversation VQA")

# Sidebar for input
st.sidebar.header("Input Image and Topic")
image = st.sidebar.file_uploader("Upload Image")
topic = st.sidebar.text_input("Enter Topic Name")

# Main content
if image is not None and topic:
    # Display uploaded image
    st.sidebar.image(image, caption="Uploaded Image", use_column_width=True)

    # Get prediction from Gemini API
    prediction = st.button("Start Conversation")

    # Display prediction
    if prediction:
        st.write("Topic Name provided:", topic)
        
        # Process image and text
        text = f"The topic you have selected from the image is {topic}. Based on that, generate a conversation with questions and answers. Total number of questions should be four or five. The maximum size of all four or five questions should be less than 40 words, and the size of all answers should be a maximum of 100 words. At least 60% of the answers should consist of just 20 words."
        generated_text = process_image(image, text)
        
        # Organize conversation output effectively
        conversation = generated_text.split("\n\n")
        st.header("Conversation:")
        for i, convo in enumerate(conversation, start=1):
            st.subheader(f"Chat {i}:")
            conversation1 = convo.split("?")
            st.write((conversation1[0]+"?").strip())
            st.write((conversation1[1]).strip())