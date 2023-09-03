import functools
import gradio as gr


def display_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        msg = ""
        if value < 18.5:
            msg += "Underweight"
        elif 18.5 <= value <= 24.9:
            msg += "Normal"
        elif 25 <= value < 30:
            msg += "Overweight"
        else:
            msg += "Obese"
        return value, msg

    return wrapper


@display_result
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
    interface = gr.Interface(
        fn=calculate_bmi, inputs=["number", "number"], outputs=["number", "text"]
    )
    interface.launch()
