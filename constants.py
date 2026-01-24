#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#


class DriveConstants:
    # Motor controller IDs for drivetrain motors
    LEFT_LEADER_ID = 13
    LEFT_FOLLOWER_ID = 10
    RIGHT_LEADER_ID = 11
    RIGHT_FOLLOWER_ID = 44

    # Current limit for drivetrain motors. 60A is a reasonable maximum to reduce
    # likelihood of tripping breakers or damaging CIM motors
    DRIVE_MOTOR_CURRENT_LIMIT = 60


class FuelConstants:
    # Motor controller IDs for Fuel Mechanism motors
    FEEDER_MOTOR_ID = 21
    INTAKE_LAUNCHER_MOTOR_ID = 20

    # Current limit and nominal voltage for fuel mechanism motors.
    FEEDER_MOTOR_CURRENT_LIMIT = 60
    LAUNCHER_MOTOR_CURRENT_LIMIT = 60

    # Voltage values for various fuel operations. These values may need to be tuned
    # based on exact robot construction.
    # See the Software Guide for tuning information
    INTAKING_FEEDER_VOLTAGE = -12.0
    INTAKING_INTAKE_VOLTAGE = -10.0
    LAUNCHING_FEEDER_VOLTAGE = -9.0
    LAUNCHING_LAUNCHER_VOLTAGE = -10.0
    EJECTING_FEEDER_VOLTAGE = 12.0
    EJECTING_INTAKE_VOLTAGE = 10.0
    SPIN_UP_FEEDER_VOLTAGE = -6.0
    SPIN_UP_SECONDS = 1.0


class OperatorConstants:
    # Port constants for driver and operator controllers. These should match the
    # values in the Joystick tab of the Driver Station software
    DRIVER_CONTROLLER_PORT = 0
    OPERATOR_CONTROLLER_PORT = 1

    # This value is multiplied by the joystick value when rotating the robot to
    # help avoid turning too fast and being difficult to control
    DRIVE_SCALING = 0.7
    ROTATION_SCALING = 0.8
