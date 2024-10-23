from diffusers import StableDiffusionPipeline
import torch
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
## stable diffusion didn't worked as it was a xl model and took time to load image
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype = torch.float32,
    safety_checker = None
)

pipe = pipe.to("cpu")

pipe.enable_attention_slicing() #reduce memory usage and optimize cpu


prompt="a beautifull images of pokemons"

image = pipe(
    prompt, 
    num_inference_steps= 15,
    height=384, 
    width=384,
    guidance_scale = 6.0
).images[0]

image.save("pokemon.png")