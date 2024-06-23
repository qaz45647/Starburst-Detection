import torch
import gradio as gr

model = torch.hub.load("./","custom",path="best.pt",source="local")
gr.Interface(inputs=["image"],outputs=["image"],fn=lambda img:model(img).render()[0]).launch()