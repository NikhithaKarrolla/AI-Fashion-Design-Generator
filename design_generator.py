from diffusers import AutoPipelineForText2Image
import torch

pipe = AutoPipelineForText2Image.from_pretrained(
    "hf-internal-testing/tiny-stable-diffusion-pipe",
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

def generate_design(prompt):

    image = pipe(
        prompt=prompt,
        num_inference_steps=10
    ).images[0]

    image.save("generated/design.png")

    return "generated/design.png"