#!/usr/bin/env python
# coding: utf-8

import json
import os

#Root of execution src folder
src_folder = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.abspath(os.path.join(src_folder, '..'))
print(root_folder)

#Requests folder
requests_folder = r'..\InvokeRequests'
#Prompt files folder
prompt_files = r'PromptFiles'

# Reading the Invoke Json Request from file
with open(os.path.join(src_folder, requests_folder, 'text_to_image_request.txt'), 'r') as prompt_file:
        json_data_t2i = prompt_file.read()

# Converting Json String to dictionary
json_dict = json.loads(json_data_t2i)

# You can mention the models, safetensors, checkpoints that are utilized for image generation here.
# These models must be already imported in Invoke AI app
models = ["sxzLuma_09XVAE",
          "spectrisMachina_v1",
          "revAnimated_v122EOL", 
          "realisticVisionV51_v51VAE", 
          "Realistic_Vision_V1.4",
          "qgoPromptingreal_qgoPromptingrealV1", 
          "pirsusEpicRealism_v16ColoredSkin", 
          "personaStyle_lite", 
          "mistoonSapphire_v20",
          "meinaunreal_v41", 
          "M4RV3LSDUNGEONSNEWV25_mD25", 
          "ghostmix_v20Bakedvae", 
          "epicrealism_naturalSinRC1VAE", 
          "anything-v3-fp32-pruned",
          "absolutereality_v1", 
          "3dAnimationDiffusion_v10", 
          "CheckpointYesmix_v20", 
          "anything-v3-fp32-pruned",
          "cyberrealistic_v40"]

# Mention the model that needs to be used [count from 0 onwards in the list]
selected_model = 5
json_dict["batch"]["graph"]["nodes"]["main_model_loader"]["model"]["model_name"] = models[selected_model]
json_dict["batch"]["graph"]["nodes"]["metadata_accumulator"]["model"]["model_name"] = models[selected_model]

# List of available Schedulers in Invoke AI
schedulers = ["ddim",
              "ddpm",
              "deis",
              "dpmpp_2m",
              "dpmpp_2m_k",
              "dpmpp_2m_sde",
              "dpmpp_2m_sde_k",
              "dpmpp_2s",
              "dpmpp_2s_k",
              "dpmpp_sde",
              "dpmpp_sde_k",
              "euler",
              "euler_a",
              "euler_k",
              "heun",
              "heun_k",
              "kdpm_2",
              "kdpm_2_a",
              "lms",
              "lms_k",
              "pndm",
              "unipc"
             ]
set_schedulers = schedulers[15]

# Printing which mddel will be set in the request
print(json_dict["batch"]["graph"]["nodes"]["main_model_loader"]["model"]["model_name"])

# Function to split keywords of prompt from Prompt files and removing any unnecessary characters if required
def read_file_for_prompts(filename):
    words = []
    with open(filename, 'r') as prompt_file:
        content = prompt_file.readlines()
        print("Content:  ", content)
    for line in content:
        print("Line:  ", line)
        for item in (line.split(" ")):
            if "," in item:
                print("Item contains comma")
                item = remove_comma(item)
            if "(" in item:
                print("Item contains bracket")
                item = remove_bracket_start(item)
            if ")" in item:
                print("Item contains bracket")
                item = remove_bracket_end(item)
            if "\n" in item:
                break
            print("Item:  ", item)
            words.append(item.strip())
        print("Words:  ", words)
    return words

# Remove Useless Commas
def remove_comma(word_with_comma):
    word_without_comma = word_with_comma.replace(",","")
    return word_without_comma

# Remove Useless Brackets
def remove_bracket_start(word_with_bracket):
    word_without_bracket = word_with_bracket.replace("(","")
    return word_without_bracket

# Remove Useless Closing Bracket
def remove_bracket_end(word_with_bracket):
    word_without_bracket = word_with_bracket.replace(")","")
    return word_without_bracket

# Here we read the prompt files convert them to list using this function
context = read_file_for_prompts(os.path.join(root_folder,  prompt_files, "context.txt"))

# You can use the above-mentioned function to create a list or You can create a comma separated list here also
prefix = read_file_for_prompts(os.path.join(root_folder,  prompt_files, "your_prefix_file.txt"))
looks = read_file_for_prompts(os.path.join(root_folder,  prompt_files, "your_looks_file.txt"))
position = read_file_for_prompts(os.path.join(root_folder,  prompt_files, "your_position_file.txt"))
location = read_file_for_prompts(os.path.join(root_folder,  prompt_files, "your_locations.txt"))
image_type = ["128K resolution","sharp focus","natural background","cinematic","masterpiece","hyper-detailed", "intricate","cyberpunk iconography"]
temperature  = []
negative_influence = read_file_for_prompts(os.path.join(root_folder,  prompt_files, "your_prefix_file.txt"))
additional_instructions = read_file_for_prompts(os.path.join(root_folder,  prompt_files, "your_prefix_file.txt"))

def list_to_string(chosen_lists):
    prompt = " "
    return prompt.join(chosen_lists)