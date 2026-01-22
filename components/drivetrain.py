#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import rev
from magicbot import will_reset_to
from wpilib.drive import DifferentialDrive

from constants import DriveConstants
from constants import OperatorConstants


class DriveTrain:

    #x_speed = will_reset_to(0.0)
    #z_rotation = will_reset_to(0.0)

    x_speed = 0
    z_rotation = 0
    def __init__(self) -> None:
        # create motors for drive
        self.left_leader = rev.SparkMax(
            DriveConstants.LEFT_LEADER_ID, rev.SparkLowLevel.MotorType.kBrushed
        )
        self.left_follower = rev.SparkMax(
            DriveConstants.LEFT_FOLLOWER_ID, rev.SparkLowLevel.MotorType.kBrushed
        )
        self.right_leader = rev.SparkMax(
            DriveConstants.RIGHT_LEADER_ID, rev.SparkLowLevel.MotorType.kBrushed
        )
        self.right_follower = rev.SparkMax(
            DriveConstants.RIGHT_FOLLOWER_ID, rev.SparkLowLevel.MotorType.kBrushed
        )

        # Set can timeout. Because this project only sets parameters once on
        # construction, the timeout can be long without blocking robot operation.
        """self.left_leader.setCANTimeout(250)
        self.right_leader.setCANTimeout(250)
        self.left_follower.setCANTimeout(250)
        self.right_follower.setCANTimeout(250)"""

        # Create the configuration to apply to motors. Voltage compensation helps
        # the robot perform more similarly on different battery voltages.
        config = rev.SparkMaxConfig()
        config.voltageCompensation(12)
        config.smartCurrentLimit(DriveConstants.DRIVE_MOTOR_CURRENT_LIMIT)

        # Set configuration to follow each leader and then apply it to corresponding
        # follower.
       
        config.follow(self.left_leader)
        self.left_leader.setInverted(False)
        self.left_follower.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )

        self.right_leader.setInverted(True)
        config.follow(self.right_leader)
        self.right_follower.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
        
        self.drive = DifferentialDrive(self.left_leader, self.right_leader)

    def execute(self) -> None:
        self.x_speed = self.x_speed * OperatorConstants.DRIVE_SCALING
        self.z_rotation = self.z_rotation * OperatorConstants.ROTATION_SCALING
        self.drive.arcadeDrive(self.x_speed, self.z_rotation)

        
