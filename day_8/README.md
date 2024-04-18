# This project is a toy project for training and quality assurance purposes

# day 8

DO NOT COMMIT OPENAI KEY TO REPO

Figure out how to implement https://www.homegpt.app/

What are flaws or issues doing it?
Answer: need gpu to run this fast, and also need to work on better ways of prompting.

MY SOLUTION SHOULD INVOLVE

1. User Input (optional):
   Design a user interface (frontend, separate from Python backend) to collect user preferences (modern, etc.) and allow image upload of their home.

2. Semantic Segmentation (deeplap model):
   In the backend (Python), use libraries like TensorFlow to load a pre-trained semantic segmentation model.
   Apply the model to the uploaded image, identifying and segmenting different areas like walls, floors, furniture.
   or
   consider feeding the diffusion model the entire image and add more prompts from the user

3. Data Processing & User Preference Integration:
   Combine the user's preferred style (modern) with the segmentation information.
   This could involve generating a style palette or design recommendations specific to each segmented area (e.g., suggest modern furniture styles for a segmented furniture region).

4. Generate new images, consider using stable diffusion to generate the image with no.3 results
