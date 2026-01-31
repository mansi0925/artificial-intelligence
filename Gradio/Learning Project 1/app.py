import gradio as gr


def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation}, {name}! The temperature is {temperature} Fahrenheit."
    celcius = (temperature - 32) * 5.0/9.0
    return greeting, round(celcius, 2)


# text, image, audio, video, slider, checkbox, label
demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(label="Name"), gr.Checkbox(label="Is Morning"), gr.Slider(
        0, 100, label="Temperature in Fahrenheit")],
    outputs=[gr.Textbox(label="Greeting"), gr.Number(
        label="Temperature in Celsius")],
    api_name="predict"
)

demo.launch()
