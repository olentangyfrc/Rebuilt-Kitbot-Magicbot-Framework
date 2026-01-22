import math 
import wpimath

def filter_input(controller_input: float, apply_deadband: bool = True) -> float:
    """
    Filters the controller input by applying a squared scaling and an optional deadband.

    This function squares the input while preserving its sign to provide finer control
    at lower values. If `apply_deadband` is True, it applies a deadband to ignore small
    inputs that may result from controller drift.

    Args:
        controller_input (float): The raw input from the controller, ranging from -1 to 1.
        apply_deadband (bool, optional): Whether to apply a deadband to the input. Defaults to True.

    Returns:
        float: The filtered controller input.
    """
    controller_input_corrected = math.copysign(
        math.pow(controller_input, 2), controller_input
    )

    if apply_deadband:
        return wpimath.applyDeadband(controller_input_corrected, 0.15**2)
    else:
        return controller_input_corrected
