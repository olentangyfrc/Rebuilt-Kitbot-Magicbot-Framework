#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import rev
from magicbot import tunable, will_reset_to

from constants import FuelConstants


class FuelMechanism:
    #intake_launcher_roller: rev.SparkMax
    #feeder_roller: rev.SparkMax
    # This makes literally no sense why you would make it this

    intaking_feeder_voltage = FuelConstants.INTAKING_FEEDER_VOLTAGE
    intaking_intake_voltage = FuelConstants.INTAKING_INTAKE_VOLTAGE
    launching_feeder_voltage = FuelConstants.LAUNCHING_FEEDER_VOLTAGE
    launching_launcher_voltage = FuelConstants.LAUNCHING_LAUNCHER_VOLTAGE
    spin_up_feeder_voltage = FuelConstants.SPIN_UP_FEEDER_VOLTAGE
    # This does not need to be tunable

    feeder_voltage = will_reset_to(0.0)
    intake_voltage = will_reset_to(0.0)
    # Confusing why it resets to 0 every control cycle; need to test
    
    def __init__(self) -> None:
        self.feeder_roller = rev.SparkMax(FuelConstants.FEEDER_MOTOR_ID, rev.SparkBase.MotorType.kBrushed)

        self.intake_launcher_roller = rev.SparkMax(FuelConstants.INTAKE_LAUNCHER_MOTOR_ID, rev.SparkBase.MotorType.kBrushed)
        #Proper Motor Config
    def intake(self) -> None:
        self.intake_voltage = self.intaking_intake_voltage
        self.feeder_voltage = self.intaking_feeder_voltage

    def eject(self) -> None:
        self.intake_voltage = -self.intaking_intake_voltage
        self.feeder_voltage = -self.intaking_feeder_voltage

    def spin_up(self) -> None:
        self.intake_voltage = self.launching_launcher_voltage
        self.feeder_voltage = -self.spin_up_feeder_voltage

    def launch(self) -> None:
        self.intake_voltage = self.launching_launcher_voltage
        self.feeder_voltage = -self.launching_feeder_voltage

    def stop(self) -> None:
        self.intake_voltage = 0.0
        self.feeder_voltage = 0.0

    def execute(self) -> None:
        self.intake_launcher_roller.setVoltage(self.intake_voltage)
        self.feeder_roller.setVoltage(self.feeder_voltage)
    
