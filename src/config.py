import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the Art Descriptions AI application."""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4-vision-preview')
    
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
    You are an expert art historian and accessibility specialist. Your task is to create a comprehensive, 
    detailed visual description of this artwork that would be helpful for people with visual impairments, 
    including those who are blind or have low vision.
    
    Please provide a description that includes:
    
    1. **Overall Composition**: Describe the overall layout, size, and arrangement of elements
    2. **Subject Matter**: What is depicted in the artwork (people, objects, scenes, etc.)
    3. **Visual Elements**: Colors, textures, lighting, and visual effects
    4. **Artistic Style**: The artistic movement, technique, and style characteristics
    5. **Emotional Impact**: The mood, atmosphere, and emotional qualities conveyed
    6. **Historical Context**: When and where it was created, if relevant
    7. **Cultural Significance**: Any cultural, historical, or symbolic meanings
    
    Make your description:
    - Detailed and vivid, using descriptive language that creates mental images
    - Accessible to people with no visual experience
    - Organized in a logical flow from general to specific
    - Approximately 200-400 words in length
    - Written in clear, engaging language
    
    Focus on making the artwork come alive through words, helping someone who cannot see it 
    to understand and appreciate its beauty, meaning, and significance.
    """
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required. Please set it in your .env file.")
        
        # Create output directory if it doesn't exist
        os.makedirs(cls.DESCRIPTIONS_DIR, exist_ok=True)
        os.makedirs(cls.ASSETS_DIR, exist_ok=True) 