# NOVA AI — Video Studio

A free, local-first AI video generation interface for **ComfyUI**. Supports text-to-video and image-to-video when you install a compatible workflow and model.

## Hosted preview

GitHub Pages hosts the NOVA interface at:

https://yorrichi68-ai.github.io/NOVAI/

**Important:** GitHub Pages only hosts static files. It cannot run Python, ComfyUI, or the AI video model. To generate videos, run NOVA locally on the same computer as ComfyUI using the instructions below. The hosted page is a project landing/demo page, not a cloud GPU service.

## Run the generator locally

1. Install Python 3.
2. Install and start [ComfyUI](https://www.comfy.org/download). Its local API should be available at http://127.0.0.1:8188.
3. Download a compatible video workflow and model. Start with the [official ComfyUI Wan examples](https://comfyanonymous.github.io/ComfyUI_examples/wan/).
4. Download this repository (Code → Download ZIP) and extract it.
5. On Windows, double-click `start_nova_windows.bat`. Or run `python server.py` in this folder.
6. Open http://127.0.0.1:8000 in Chrome.
7. In ComfyUI, enable Dev Mode and save the workflow using **Save (API Format)**.
8. Import the JSON workflow into NOVA and map the prompt node/input. For image-to-video, also map the image loader node.

## Requirements

- Chrome or another modern browser
- Python 3
- ComfyUI
- A compatible video diffusion model and workflow
- A supported GPU is strongly recommended; generation may be impractically slow on CPU

## Files

- `index.html` — NOVA local studio interface
- `server.py` — local-only bridge between the browser UI and ComfyUI
- `start_nova_windows.bat` — Windows launcher
- `site/index.html` — GitHub Pages project landing page

## Notes

- No paid API key is required.
- This repository does not include model weights; they are large and have separate licenses.
- Workflow node IDs vary. You must map the correct node IDs and input names for your imported API workflow.
- The local bridge binds to 127.0.0.1 only. Do not expose it to the public internet.
