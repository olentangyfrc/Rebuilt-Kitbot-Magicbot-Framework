#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
import magicbot
import wpilib

from utilities_functions import filter_input
from components.drivetrain import DriveTrain
from components.fuel import FuelMechanism
from components.launch_sequence import LaunchSequence
from constants import OperatorConstants


class MyRobot(magicbot.MagicRobot):
    launch_sequence: LaunchSequence
    drivetrain: DriveTrain
    fuel: FuelMechanism

    def createObjects(self) -> None:

        # The driver's controller
        self.driver_controller = wpilib.XboxController(
            OperatorConstants.DRIVER_CONTROLLER_PORT
        )


    def teleopPeriodic(self) -> None:
        self.drivetrain.x_speed = filter_input(self.driver_controller.getLeftY(), True)
        self.drivetrain.z_rotation = filter_input(self.driver_controller.getRightX(), True)
        

        if self.driver_controller.getRightBumper():
            self.launch_sequence.launch()
        elif self.driver_controller.getLeftBumper():
            self.fuel.intake()
        elif self.driver_controller.getBButton():
            self.fuel.eject()
        else:
            self.fuel.stop()
        
            
