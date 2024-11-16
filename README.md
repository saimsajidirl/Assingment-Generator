# Software Requirements Specification (SRS) for Assignment Generator
Version: 1.0
Date: Nov 17 2024
Authors: 

1. Introduction

The Assignment Generator is a Streamlit-based application that generates assignments and presentations based on user-provided prompts. It uses the Gemini API to generate text content and can produce either a Word document (DOCX) or a PowerPoint presentation (PPTX).

1.1 Purpose

This SRS document describes the functionality, requirements, and specifications for the Assignment Generator. The application is designed for users who want to quickly create educational content such as assignments or presentations based on a specific topic.

1.2 Scope

The application will allow users to:

Enter a topic and optional additional instructions.

Select between a Word document or a PowerPoint presentation as the output format.

Generate content via the Gemini API.

Download the generated document.

1.3 Definitions, Acronyms, and Abbreviations

API: Application Programming Interface

DOCX: Microsoft Word Document format

PPTX: Microsoft PowerPoint Presentation format


2. Overall Description

2.1 Product Perspective

The Assignment Generator is a standalone application built with Streamlit, Google Gemini API, and Python. It provides an easy-to-use interface for generating educational content and leverages Generative AI to create high-quality content on demand.

2.2 Product Functions

Topic Input: Accepts a topic from the user.

Additional Instructions: Optional field for additional guidance.

File Type Selection: Allows users to choose between DOCX and PPTX formats.

Content Generation: Uses Gemini API to generate text based on the provided prompt.

Download: Provides a download link for the generated document.

2.3 User Classes and Characteristics

The intended users include educators, students, and individuals who need to create assignments or presentations efficiently.

2.4 Operating Environment

The application runs on:

Operating System: Any OS supporting Streamlit (Windows, macOS, Linux).

Browser: Compatible with major browsers (Chrome, Firefox, Edge).

API: Requires an internet connection to access the Gemini API.

2.5 Design and Implementation Constraints

Gemini API Usage: Limited by the number of requests allowed by Google Generative AI API.

File Download: File size and formatting constraints are based on DOCX and PPTX standards.

2.6 User Documentation

The application includes in-app guidance on:


Entering the topic.

Choosing a file format.

Generating and downloading the document.

3. Functional Requirements
   
3.1 Input Topic

Description: User enters a topic to generate content.
Input: Text input field.
Pre-conditions: Topic field must not be empty.
Post-conditions: The topic is passed to the content generation module.
3.2 Additional Instructions
Description: Optional instructions to further guide the content generation.
Input: Text area field.
Pre-conditions: N/A
Post-conditions: Additional instructions are included in the prompt if provided.
3.3 File Type Selection
Description: Allows the user to select DOCX or PPTX format.
Input: Dropdown selector.
Pre-conditions: Valid selection.
Post-conditions: Content is formatted according to the selected file type.
3.4 Content Generation
Description: Sends a prompt to Gemini API and receives generated content.
Input: Topic and additional instructions.
Output: Generated text content.
Pre-conditions: Topic is provided.
Post-conditions: Content is prepared for download.
3.5 File Download
Description: Allows users to download the generated file.
Input: Button click.
Output: DOCX or PPTX file.
Pre-conditions: File has been generated.
Post-conditions: File is saved locally by the user.
5. Non-Functional Requirements
4.1 Performance Requirements
The application should respond to user input within 2 seconds.
Content generation should take no longer than 20 seconds, depending on API response time.
4.2 Reliability
Application should handle invalid inputs gracefully and show appropriate error messages.
4.3 Usability
The interface should be intuitive and accessible to users with basic computer skills.
4.4 Portability
Application should be deployable on any system supporting Streamlit.
6. External Interface Requirements
5.1 User Interfaces
A web-based user interface using Streamlit.
Includes input fields, dropdowns, and buttons for interaction.
5.2 Hardware Interfaces
Compatible with standard personal computing devices.
5.3 Software Interfaces
Google Generative AI API (Gemini) for content generation.
5.4 Communication Interfaces
Internet connection for API access.
7. Other Requirements
API Key Management: The API key should be securely stored and managed.
