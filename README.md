# NOVA AI — Cloud Video Studio

NOVA AI is a browser-based text-to-video prototype hosted on GitHub Pages. It submits prompts directly to the public Lightricks LTX-Video Distilled Gradio Space on Hugging Face ZeroGPU.

## Live website

https://yorrichi68-ai.github.io/NOVAI/

## Cloud generation

1. Open the website.
2. Enter a descriptive prompt.
3. Choose a duration and output size.
4. Click **Generate Video in Cloud**.
5. Keep the tab open while the shared GPU queue runs.

The browser calls the public Gradio queue API at `https://lightricks-ltx-video-distilled.hf.space`. No local ComfyUI, local model, local server, or API key is required for the anonymous demo.

## Important limits

- This is a community-hosted shared demo, not NOVA-owned infrastructure.
- Hugging Face ZeroGPU quotas apply. The documented anonymous quota is small (2 GPU minutes/day); authenticated free accounts may receive a larger personal quota. Provider limits and availability can change.
- The Space may be busy, paused, changed, or unavailable. Generation is not guaranteed.
- This is not unlimited Google Flow-level service and does not promise a free unlimited video API.
- GitHub Pages hosts only the front end; video inference runs on the external Hugging Face Space.
- Do not put private API keys or tokens in this public repository.

## Source and service

- Front end: `index.html` and `site/index.html`
- Deployment: `.github/workflows/pages.yml`
- Hosted model Space: https://huggingface.co/spaces/Lightricks/ltx-video-distilled
- Model project: https://github.com/Lightricks/LTX-Video

## Troubleshooting

If generation fails, retry later; the shared Space may be sleeping, busy, or out of quota. If the provider changes its Gradio API, update the endpoint and parameter mapping in the page's script.
