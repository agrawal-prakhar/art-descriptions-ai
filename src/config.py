import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the Art Descriptions AI application."""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')
    
    # Output Configuration
    OUTPUT_FORMAT = os.getenv('OUTPUT_FORMAT', 'json')
    OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'descriptions')
    
    # File paths
    ASSETS_DIR = 'assets'
    DESCRIPTIONS_DIR = 'descriptions'
    
    # Supported image formats
    SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    
    # Accessibility-focused prompt template
    ACCESSIBILITY_PROMPT = """
    You are a precise visual describer. Your task is to create a detailed, factual description of what is visible in this image. Focus ONLY on what you can actually see - do not speculate, interpret, or add historical context.

    Here are examples of the type of description you should provide:

    Example 1:
    This watercolor is the artist's self-portrait, a head-on view of a dark-skinned man filling the vertical sheet of paper where the top of his head and both ears are omitted. The face is rendered predominantly in shades of black and gray and painted in small blotches as a stitched quilt would be sewn together. The eyes are dark with white highlights, set beneath what looks like eyebrows created by darker patches. The darker areas define the nose, mouth, and facial structure, while lighter areas highlight portions of the forehead, cheeks, and chin. The image is set against a light tan or beige background. At the bottom edge, there's a burgundy or reddish-brown color that might represent clothing below the neck. A vertical line is running down the center of the image, suggesting a folded page.

    Example 2:
    This vertical print, done in an etching technique, depicts two young women seated together by an interior wall. On the left sits a woman with dark, voluminous hair styled in a distinctive tall headdress. She wears elaborate clothing with a decorative bodice and flowing sleeves, and her bare feet are visible at the bottom of her dress. On the floor to her left sits another woman with darker features. She appears to be leaning against the festive-dressed woman. She wears a simple head covering, a simple skirted dress, and slippers. There is a patterned rug on the floor, and in the lower part of the print, partially obscured, stands a small decorated wooden stool with a spherical object looking like an apple. The interior wall is covered up to two-thirds of its height by what looks like a textured textile. There is a small wall opening (or a closed window) to the upper right of the image for keeping a few objects. A candlestick holder and another unidentified pouch-like object hang on each side of the opening. The artist's signature and date are handwritten in the upper left corner.

    Example 3:
    The portrait of a Black person fills almost entirely this black and white rectangular photograph. They face forward, their eyes partly closed. Their skin appears to have a dark, matte finish. The facial features are softly defined against the stark light background. They wear a tall, conical headdress that rises vertically from their head, wrapped in dark, furry fabric. A decorative element with what appears to be a small round pendant with a tassel hangs at the front of the headdress. The person’s neck and shoulders are completely encircled by a thick, textured collar with a distinctive pattern featuring dark spots or swirling shapes. This patterned material forms a circular support around her neck and upper chest.

    Example 4:
    This horizontal black and white photograph diptych consists of two rectangular panels side by side. The left panel shows a white plate against a black background, with text reading "NOT GOOD ENOUGH" printed in the middle of it. The right panel shows a portion of a Black woman’s body, with a fragment of white, scalloped-edged clothing visible. Only the woman’s lips and chin are visible, and the words "BUT GOOD ENOUGH TO SERVE" are printed between her collarbones. The panels are set within a light gray border or frame surrounding the entire image.

    Please provide a description that includes:

    1. **Overall Layout**: Describe the composition, orientation (vertical/horizontal), and general arrangement
    2. **Main Subject**: What is the primary focus or central element
    3. **Visual Details**: Colors, textures, lighting, and visible effects
    4. **Background Elements**: What appears in the background or surrounding areas
    5. **Text Elements**: Any visible text, titles, signatures, or labels
    6. **Physical Details**: Specific objects, clothing, poses, expressions, and visible features

    Guidelines:
    - Describe only what is visually present - no speculation or interpretation
    - Use precise, factual language
    - Organize from general to specific details
    - Include approximately 150-250 words
    - Focus on visual accuracy over artistic interpretation
    - If text is visible, describe its location and content
    - Mention the overall visual style or appearance (e.g., "sepia-toned", "vintage appearance")

    Your description should help someone understand exactly what is visible in the image without any added interpretation or historical context.
    """
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required. Please set it in your .env file.")
        
        # Create output directory if it doesn't exist
        os.makedirs(cls.DESCRIPTIONS_DIR, exist_ok=True)
        os.makedirs(cls.ASSETS_DIR, exist_ok=True) 