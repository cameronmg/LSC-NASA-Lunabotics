// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot;

import edu.wpi.first.networktables.EntryListenerFlags;
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.motorcontrol.Spark;

/**
 * The VM is configured to automatically run this class, and to call the functions corresponding to
 * each mode, as described in the TimedRobot documentation. If you change the name of this class or
 * the package after creating this project, you must also update the build.gradle file in the
 * project.
 */
public class Robot extends TimedRobot {
  /**
   * This function is run when the robot is first started up and should be used for any
   * initialization code.
   */
  NetworkTableInstance inst = NetworkTableInstance.getDefault(); 
  //Get the table within that instance that contains the data. There can
  //be as many tables as you like and exist to make it easier to organize
  //your data. In this case, it's a table called datatable.
  NetworkTable table = inst.getTable("datatable");
  NetworkTableEntry leftStick = table.getEntry("LeftStickValue");
  NetworkTableEntry rightStick = table.getEntry("RightStickValue");
  //mapping motor PWM ports
  Spark motorFrontLeft = new Spark(5);
  Spark motorFrontRight = new Spark(6);
  Spark motorBackLeft = new Spark(3);
  Spark motorBackRight = new Spark(4);


  @Override
  public void robotInit() {}

  @Override
  public void robotPeriodic() {}

  @Override
  public void autonomousInit() {}

  @Override
  public void autonomousPeriodic() {}

  @Override
  public void teleopInit() {}
  double rightSickValues;
  double leftStickValues;

  double speed, turn, left, right;
  
  @Override
  public void teleopPeriodic() 
  {
      
      //add an entry listener for changed values of "RightSickValues", the lambda ("->" operator)
      //defines the code that should run when "RightSickValues" changes
      table.addEntryListener("RightStickValue", (table, key, entry, value, flags) -> 
      {
        rightSickValues = value.getDouble();
        //for this axis -controller: up is negative, down is positive
        speed = -rightSickValues * 0.6;
        //slow speed down to 60% and turning to 30% for better controllability
        turn = rightSickValues * 0.3;
        //left power = speed + turn
        double left = speed + turn;
      //right power = speed - turn
        double right = speed - turn;

        System.out.println("RightStickValue set: " + value.getValue());
        //setting speed of motors from xbox controller input
        motorFrontRight.set(-right);
        motorBackRight.set(right);
        motorBackLeft.set(-left);
        motorBackLeft.set(left);

      }
      , EntryListenerFlags.kNew | EntryListenerFlags.kUpdate);
      
      //add an entry listener for changed values of "RightSickValues", the lambda ("->" operator)
      //defines the code that should run when "RightSickValues" changes
      table.addEntryListener("LeftStickValue", (table, key, entry, value, flags) -> 
      {
        leftStickValues = value.getDouble();
        System.out.println("LeftStickValues set: " + value.getValue());
        //setting speed of motors from xbox controller input
        motorFrontLeft.set(leftStickValues);
        motorFrontRight.set(-leftStickValues);
        motorBackLeft.set(leftStickValues);
        motorBackRight.set(-leftStickValues);

      }
      , EntryListenerFlags.kNew | EntryListenerFlags.kUpdate);

  }

  @Override
  public void disabledInit() {}

  @Override
  public void disabledPeriodic() {}

  @Override
  public void testInit() {}

  @Override
  public void testPeriodic() {}

  @Override
  public void simulationInit() {}

  @Override
  public void simulationPeriodic() {}
}
