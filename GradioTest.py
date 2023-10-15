#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 14:28:52 2023

@author: christian
"""

import gradio as gr

def greet(name, is_dawn, temp):
    salutation = "Morning" if is_dawn else "Evening"
    greeting = f"{salutation} {name}. Today is {temp} degrees"
    celsius = (temp - 32) * 5 / 9
    return greeting, round(celsius, 2)

demo = gr.Interface(fn=greet, inputs=["text", "checkbox", gr.Slider(0,100)],
                    outputs=["text", "number"])

demo.launch()