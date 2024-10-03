import os
import io
from PIL import Image
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
anthropic_client = Anthropic(api_key=anthropic_api_key)
MODEL_NAME = "claude-3-haiku-20240307" #"claude-3-opus-20240229"

# defining the content checks & examples
content_checks = {
    "Safety_1": "Violence",
    "Safety_2": "Explicit Content",
    "Safety_3": "Cultural Sensitivity",
    "Safety_4": "Profanity",
    "Bias_1": "Stereotype / Racial Ethnic",
    "Bias_2": "Stereotype / Gender",
    "Bias_3": "Cultural Appropriation",
    "Bias_4": "Stereotypes / Sexual Orientation",
}

content_check_examples = {
    "Violence": ["An image showing destruction in urban areas that may suggest recent violence or unrest", 
                              "Aerial or street-level shots of cities with signs of aggression or conflict visible"],
    "Explicit Content": ["Photos of urban landscapes or public art that include explicit or adult content", 
                              "Images of cityscapes with graffiti containing offensive or explicit material"],
    "Cultural Sensitivity": ["Photographs of culturally significant sites that are presented in a disrespectful or harmful context", 
                             "Images of cities or landscapes that misuse cultural symbols or monuments"],
    "Profanity": ["Text overlay with curse words", 
                              "An aggressive gesture with known offensive meaning"],
    "Stereotypes / Racial Ethnic": ["Urban landscapes or city images that might unintentionally reinforce geographical stereotypes associated with race or ethnicity", 
                                    "Images that depict neighborhoods or cultural landmarks in a way that could perpetuate stereotypes"],
    "Stereotypes / Gender": ["Cityscapes or landscapes that include advertising or public messages perpetuating gender stereotypes", 
                             "Visual representations suggesting gender roles within urban or rural settings"],
    "Cultural Appropriation": ["Images of city art or architecture that appropriates elements from a culture in a manner lacking respect or context", 
                               "Photographs of landscapes featuring cultural festivals or events where there's potential for cultural appropriation"],
    "Stereotypes / Sexual Orientation": ["Urban scenes or public events depicted in a way that stereotypes communities based on sexual orientation", 
                                         "Landscapes or city images that might oversimplify the diversity of communities based on sexual orientation"]

}

# Anthropic Functions
def get_vision_completion(base64_string, prompt_text, MODEL_NAME):
    '''
    This function takes a base64 encoded image and a prompt text, and returns the completion from the Claude model.
    '''
    response = anthropic_client.messages.create(
        model=MODEL_NAME,
        max_tokens=2048,
        temperature=0,
        messages=[
                {
                    "role": 'user',
                    "content": [
                        {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": base64_string}},
                        {"type": "text", "text": prompt_text}
                    ]
                }
            ],
    )
    return response.content[0].text

def evaluate_image_for_content_with_examples(base64_string, content_check, examples, MODEL_NAME):
    # Constructing the examples section of the prompt
    examples_text = "\n\n".join([f"Example of {category}:\n- {example}" for category, example in content_check_examples.items()])
    
    # Adding the current content check to the prompt
    prompt_text = f"{examples_text}\n\nCheck this image to see if the content contains {content_check}. Respond ONLY with a YES or NO"
    
    message_list = [
        {
            "role": 'user',
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": base64_string}},
                {"type": "text", "text": prompt_text}
            ]
        }
    ]
    
    response = anthropic_client.messages.create(
        model=MODEL_NAME,
        max_tokens=2048,
        temperature=0,
        messages=message_list
    )
    
    return response.content[0].text

# utility function to process the image and get the content
def process_image(image_path):
    with Image.open(image_path) as img:
        # Convert to RGB mode (removes alpha channel if present)
        img = img.convert('RGB')
        
        # Save as JPEG in memory
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')
        img_content = buffer.getvalue()
    
    return img_content
