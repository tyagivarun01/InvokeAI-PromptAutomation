# InvokeAI-PromptAutomation
An Automation for creating dynamic prompts and creating Images using InvokeAI

https://github.com/invoke-ai/InvokeAI.git

InvokeAI is a leading creative engine for Stable Diffusion models, empowering professionals, artists, and enthusiasts to generate and create visual media using the latest AI-driven technologies. The solution offers an industry leading WebUI, supports terminal use through a CLI, and serves as the foundation for multiple commercial products.

This automation can be used with Invoke AI. It creates dynamic prompts based on differnet files. Once the files are filled with desiered number of prompt keywords they are then used generate a random prompt that can be utilized for generation of truely random images.

The request folder contains imagetotext request for Invoke AI. The request is modified accoding to the choices in programs.

Any number of models, checkpoints and safetensors can be used but only one is utlized at a time. While seding the rewuest a random scheduler and a random seed is generated which helps in random image generation.

The prompts also includes negative prompting that can be used during the generation. Fill it will desiered keywords.
You can refer to context.txt for how the files can be structured.

Important: Keywords must be seperated with a space. Comma, opening and closing brackets are removed automatically.

If you want the prompt to contain weights use (+) plus sighn with the keyword. Eg Forest+, Peaches++ etc

Invoke AI server needs to be up and running for this script to work.

Future plans: saving all created prompts to a file. Removing blank spaces. 
