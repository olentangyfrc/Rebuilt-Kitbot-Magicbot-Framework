#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

from magicbot import StateMachine, timed_state, state

from constants import FuelConstants
from components.fuel import FuelMechanism


class LaunchSequence(StateMachine):
    fuel: FuelMechanism

    def launch(self) -> None:
        self.engage()

    @timed_state(duration=FuelConstants.SPIN_UP_SECONDS, first=True)
    def spin_up(self) -> None:
        self.fuel.spin_up()

    @state
    def launch_fuel(self) -> None:
        self.fuel.launch()
