from nicegui import ui

ui.colors(
      primary='#6400BA',
      secondary='#7300BA',
      accent='#8300BA',
      positive='#6400BA',
      negative='#6400BA',
      info='#4500BA',
      warning='#4500BA'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: Applies the "positive" color defined above to the text.
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: Applies the "negative" color defined above to the text.

def convert_knob(e):
    temp = knob_input.value
    knob_result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")

with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl" "bg-opacity-90" "scale-105 hover:scale-110 transition-transform duration-300"):
    # w-100: Set element width to be fixed at 100
    # p-6: Adds padding of 1.5rem on all sides of the card.
    # shadow-xl: Gives the card a large drop shadow, making it stand out from the background.
    # mx-auto: Auto-adjusts the left and right margins to center a card. 
    # mt-10: Adds a top margin of 2.5rem, pushing our card down from the top.
    # rounded-xl: Adds XL rounded corners to the card.
    ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4 mx-auto")
    # text-2xl: Makes text larger by setting the size to  “2XL.” 
    # font-bold: Bolds the text
    # text-accent: Applies the "accent" color defined above to the text. 
    # mb-4: Gives space below the label by adding a bottom margin of 1rem. 
    input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
    # w-full: Sets the input’s width to 100% of its parent container.
    # border: Adds a thin border around the input field.
    # rounded: Gives the input field lightly rounded corners.
    conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
    convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded mx-auto block" "bg-primary hover:bg-secondary transition ease-in-out duration-300")
    # text-white: Makes the button text white.
    # py-2: Adds vertical padding of 0.5rem.
    # px-4: Adds horizontal padding of 1rem.
    result_label = ui.label("").classes("text-lg mt-4")

    with ui.card().classes("w-80 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-opacity-90 transition-transform duration-300 flex flex-col items-center text-center"):
        ui.label("Temperature Selector: Knob Edition").classes("text-xl font-semibold text-accent mb-4 text-center")
        knob_input = ui.knob(min=-100, max=100, value=0, show_value=True).classes("mb-4 mx-auto")
        knob_input.on("change", convert_knob)
        knob_result_label = ui.label("").classes("text-lg mt-4 text-center")

ui.run()