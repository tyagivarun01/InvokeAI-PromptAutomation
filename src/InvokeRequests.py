#!/usr/bin/env python
# coding: utf-8

import CreatePrompt as k
import requests
from requests.exceptions import HTTPError
import json
import random

# This function sets all the parameter in the request
def set_parameters():
    #context_choices = random.sample(context, 30)
    prefix_choice = random.sample(k.prefix, 1)
    additional_instructions_choice = random.sample(k.additional_instructions, 20)
    #print(context_choices, prefix_choice, additional_instructions_choice)

    looks_choices = random.sample(k.looks, 20)
    position_choices = random.sample(k.position, 3)
    location_choices = random.sample(k.location, 5)
    image_type_choices = random.sample(k.image_type, 3)
    
    initial_prompt = k.list_to_string(prefix_choice)
    initial_prompt = initial_prompt + ", " + k.list_to_string(position_choices)
    initial_prompt = initial_prompt + ", " + k.list_to_string(location_choices)
    initial_prompt = initial_prompt + ", " + k.list_to_string(image_type_choices)
    initial_prompt = initial_prompt + ", " + k.list_to_string(additional_instructions_choice)
    
    automated_created_prompt = initial_prompt
    print(automated_created_prompt)
    negative_influence_prompt = random.sample(k.negative_influence, 20)
    automated_negative_created_prompt = k.list_to_string(negative_influence_prompt)
    
    random_seed = random.randint(1000000000, 9999999999)
    print(random_seed)
    k.json_dict["batch"]["data"][0][0]["items"][0] = random_seed
    k.json_dict["batch"]["data"][0][1]["items"][0] = random_seed
    k.json_dict["batch"]["graph"]["nodes"]["positive_conditioning"]["prompt"] = automated_created_prompt
    k.json_dict["batch"]["graph"]["nodes"]["metadata_accumulator"]["positive_prompt"] = automated_created_prompt

    k.json_dict["batch"]["graph"]["nodes"]["negative_conditioning"]["prompt"] = automated_negative_created_prompt
    k.json_dict["batch"]["graph"]["nodes"]["metadata_accumulator"]["negative_prompt"] = automated_negative_created_prompt
    
    k.json_dict["batch"]["graph"]["nodes"]["noise"]["width"] = 512
    k.json_dict["batch"]["graph"]["nodes"]["noise"]["height"] = 768
    k.json_dict["batch"]["graph"]["nodes"]["noise"]["seed"] = random_seed
    cfg_scale_random_value = random.randint(4, 7)
    k.json_dict["batch"]["graph"]["nodes"]["denoise_latents"]["cfg_scale"] = cfg_scale_random_value
    k.json_dict["batch"]["graph"]["nodes"]["metadata_accumulator"]["cfg_scale"] = cfg_scale_random_value

    set_schedulars = random.sample(k.schedulers, 1)
    k.json_dict["batch"]["graph"]["nodes"]["denoise_latents"]["scheduler"] = set_schedulars[0]
    k.json_dict["batch"]["graph"]["nodes"]["metadata_accumulator"]["scheduler"] = set_schedulars[0]
    

for x in range(0, 5):
    set_parameters()

    json_data = json.dumps(k.json_dict)
    url = "http://localhost:9090/api/v1/queue/default/enqueue_batch"
    response = requests.post(url, json_data)
    response.raise_for_status()