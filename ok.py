import os
from vertexai.preview.vision_models import ImageGenerationModel
import vertexai

from google.cloud import aiplatform
import vertexai.preview
from google.cloud import aiplatform_v1

# Assuming you have your API key stored in an environment variable
api_key = os.environ['GOOGLE_API_KEY']

# Initialize Vertex AI with your API key (might be different depending on authentication method)
vertexai.init(api_key='GOOGLE_API_KEY')

# Load the Image Generation model (check the available models in the documentation)
imagen = ImageGenerationModel.from_pretrained("your_model_name@your_version")  # Replace with actual model name and version

result = imagen.generate_images(
    prompt="Fuzzy bunnies in my kitchen",
    number_of_images=4,
    safety_filter_level="block_only_high",
    person_generation="allow_adult",
    aspect_ratio="3:4",
    negative_prompt="Outside",
)

for image in result.images:
    print(image)