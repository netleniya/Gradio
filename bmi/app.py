import gradio as gr


def calculate_bmi(height: float, weight: float) -> float:
    """calculate the body mass index given height and weight

    Args:
        height (float): height in (cm)
        weight (float): weight in (kg)

    Returns:
        float: BMI
    """
    return round(weight / height**2 * 10000, 1)


if __name__ == "__main__":
    interface = gr.Interface(fn=calculate_bmi, inputs=["number", "number"], outputs=["number"])
    interface.launch()
