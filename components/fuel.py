#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import rev

from constants import FuelConstants


class FuelMechanism:
    
    def __init__(self) -> None:
        self.feeder_roller = rev.SparkMax(FuelConstants.FEEDER_MOTOR_ID, rev.SparkBase.MotorType.kBrushed)

        self.feeder_voltage = 0.0
        self.intake_voltage = 0.0
        self.intake_enabled = False

        self.intake_launcher_roller = rev.SparkMax(FuelConstants.INTAKE_LAUNCHER_MOTOR_ID, rev.SparkBase.MotorType.kBrushed)
        #Proper Motor Config
    def intake(self) -> None:
        self.intake_voltage = FuelConstants.INTAKING_INTAKE_VOLTAGE
        self.feeder_voltage = FuelConstants.INTAKING_FEEDER_VOLTAGE

    def eject(self) -> None:
        self.intake_voltage = FuelConstants.EJECTING_INTAKE_VOLTAGE
        self.feeder_voltage = FuelConstants.EJECTING_FEEDER_VOLTAGE

    def spin_up(self) -> None:
        self.intake_voltage = FuelConstants.LAUNCHING_LAUNCHER_VOLTAGE
        self.feeder_voltage = -FuelConstants.SPIN_UP_FEEDER_VOLTAGE

    def launch(self) -> None:
        self.intake_voltage = FuelConstants.LAUNCHING_LAUNCHER_VOLTAGE
        self.feeder_voltage = -FuelConstants.LAUNCHING_FEEDER_VOLTAGE

    def stop(self) -> None:
        self.intake_voltage = 0.0
        self.feeder_voltage = 0.0

    def execute(self) -> None:
        
        self.intake_launcher_roller.setVoltage(self.intake_voltage)
        self.feeder_roller.setVoltage(self.feeder_voltage)
        
            

        

    
