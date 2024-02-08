from django.shortcuts import render
from .forms import TextToImageForm
from diffusers import AutoPipelineForText2Image
import torch

def text2image_view(request):
    if request.method == 'POST':
        form = TextToImageForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']

            # Load the model on CPU
            pipeline_text2image = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant=None)


            # No need to move the model to GPU since we are using CPU
            # pipeline_text2image = pipeline_text2image.to("cpu")

            # Run inference on CPU
            image = pipeline_text2image(prompt=prompt, guidance_scale=0.0, num_inference_steps=1).images[0]

            context = {'image': image, 'form': form}
            return render(request, 'text2image.html', context)
    else:
        form = TextToImageForm()

    context = {'form': form}
    return render(request, 'text2image.html', context)
