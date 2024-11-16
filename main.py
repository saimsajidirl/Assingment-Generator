import streamlit as st
from docx import Document
from io import BytesIO
import google.generativeai as genai
import time
from pptx import Presentation
from pptx.util import Pt

genai.configure(api_key='AIzaSyAYILkEzVTT4OrMcuvD_lOHfR5cl2UG5zE')

def generate_content(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def add_content_to_ppt(ppt, content):
    slides = content.split('\n\n')  
    
    for slide_content in slides:
        slide_lines = slide_content.split('\n')
        title = slide_lines[0]
        body = '\n'.join(slide_lines[1:])
        
        slide = ppt.slides.add_slide(ppt.slide_layouts[1]) 
        
        title_shape = slide.shapes.title
        body_shape = slide.shapes.placeholders[1]

        title_shape.text = title
        
        text_frame = body_shape.text_frame
        text_frame.text = body
        
        for paragraph in text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(18)  

        body_shape.width = Pt(600)  
        body_shape.height = Pt(400) 
        body_shape.left = Pt(50)  
        body_shape.top = Pt(100) 
    
    return ppt

st.set_page_config(page_title="Assignment Generator")

st.title("Generate Assignment in One Prompt")

topic = st.text_input("Enter Topic:")
extra_instruction = st.text_area("Extra Instruction (Optional)")

file_type = st.selectbox("Select file type", ("Word Document (Docx) ", "PowerPoint Presentation (PPT) "))

start_time = None
end_time = None

if st.button("Generate Content"):
    if topic:
        start_time = time.time()

        with st.spinner("Please wait, your document is being generated..."):
            if extra_instruction:
                prompt = f"{topic}. {extra_instruction}"
            else:
                prompt = topic

            if file_type == "PowerPoint":
                modified_prompt = f"Create a PowerPoint presentation on {prompt}. Break the content into slides. Each slide should have a title and bullet points. Provide at least 5 slides."
            else:
                modified_prompt = f"{prompt}"

            content = generate_content(modified_prompt)

            if file_type == "Word Document":
                doc = Document()
                doc.add_heading(f"{topic}", level=1)

                paragraphs = content.split('\n')
                heading_level = 1
                for para in paragraphs:
                    if para.startswith("# "):
                        doc.add_heading(para[2:], level=heading_level)
                        heading_level += 1
                    elif para.startswith("* "):
                        doc.add_paragraph(para[2:], style='List Bullet')
                    elif para.startswith("1. "):
                        doc.add_paragraph(para[3:], style='List Number')
                    else:
                        doc.add_paragraph(para)

                byte_stream = BytesIO()
                doc.save(byte_stream)
                byte_stream.seek(0)

                end_time = time.time()
                elapsed_time = end_time - start_time

                st.download_button(
                    label="Download Word Document",
                    data=byte_stream,
                    file_name=f"{topic}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

            elif file_type == "PowerPoint":
                ppt = Presentation()

                ppt = add_content_to_ppt(ppt, content)

                byte_stream = BytesIO()
                ppt.save(byte_stream)
                byte_stream.seek(0)

                end_time = time.time()
                elapsed_time = end_time - start_time

                st.download_button(
                    label="Download PowerPoint Presentation",
                    data=byte_stream,
                    file_name=f"{topic}.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )

            st.success(f"Document generated in {elapsed_time:.2f} seconds.")

    else:
        st.warning("Please enter a topic to generate content.")
