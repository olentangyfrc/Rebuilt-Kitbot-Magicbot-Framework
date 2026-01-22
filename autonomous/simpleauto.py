#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

from magicbot import AutonomousStateMachine, timed_state

from components.drivetrain import DriveTrain
from components.fuel import FuelMechanism


class SimpleAuto(AutonomousStateMachine):
    MODE_NAME = "Autonomous"
    DEFAULT = True

    drivetrain: DriveTrain
    fuel: FuelMechanism

    @timed_state(duration=0.25, first=True, next_state="launch")
    def drive_forward(self) -> None:
        self.drivetrain.drive.arcadeDrive(0.5, 0.0)

    @timed_state(duration=10.0, next_state="Stop")
    def launch(self) -> None:
        self.fuel.launch()
    
    @timed_state(duration=1.0)
    def Stop(self):
        self.drivetrain.x_speed = 0
        self.drivetrain.z_rotation = 0
        self.fuel.stop()

