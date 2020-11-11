#!/usr/bin/env python3

import rospy
from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.srv import GetJointProperties


msg_topic = '/gazebo/apply_joint_effort'
joint_left = 'ddB_robot::left_wheel_hinge'
joint_right = 'ddB_robot::right_wheel_hinge'
msg_topic_feedback = '/gazebo/get_joint_properties'

pub_feedback = rospy.ServiceProxy(msg_topic_feedback, GetJointProperties)

rospy.init_node('dd_ctrl', anonymous=True)
pub = rospy.ServiceProxy(msg_topic, ApplyJointEffort)

effOrDir = int(raw_input("Set wheel effort(0), or wheel direction and speed(1)?:"))

if not effOrDir:
    effortL = float(raw_input("Enter Effort for Left wheel. Valid range [0,1]:"))
    effortR = float(raw_input("Enter Effort for Right wheel. Valid range [0,1]:"))
else:
    speedL = float(raw_input("Enter Speed for Left wheel. Neg for backward, Pos for forward:"))
    speedR = float(raw_input("Enter Speed for Right wheel. Neg for backward, Pos for forward:"))


start_time = rospy.Time(0,0)

f = float(20)
T = 1/f
Tnano = int(T*1000000000)

#print('T:', T)
#print('Tnano',Tnano)

end_time = rospy.Time(0,Tnano)
#print('end_time',end_time)
duration = end_time-start_time
rate = rospy.Rate(f)


while True:
    valLeft = pub_feedback(joint_left)
    valRight = pub_feedback(joint_right)   

    if effOrDir:
        #fixed acceleration up to requested speed
        if valLeft.rate[0]<speedL:
            effortL = 0.5
        if valLeft.rate[0]<speedR:
            effortR = 0.5
        #fixed decelleration down to requested speed
        if valLeft.rate[0]>speedL:
            effortL = -0.5
        if valLeft.rate[0]>speedR:
            effortR = -0.5 

    #print('effort to left wheel is:', effortL) 
    #print('effort to right wheel is:', effortR) 
    #print('start time', start_time)  
    #print('duration', end_time)  

    pub(joint_left, effortL, start_time, duration)
    pub(joint_right, effortR, start_time, duration)

    if valLeft.rate[0]>0:
        leftWheelDir = 'forward'
    else:
        leftWheelDir = 'reverse'
    if valRight.rate[0]>0:
        RightWheelDir = 'forward'
    else:
        RightWheelDir = 'reverse'
    
    print('Left wheel speed is:', valLeft.rate[0], 'in the ', leftWheelDir, ' direction')
    print('Right wheel speed is:', valRight.rate[0], 'in the ', RightWheelDir, ' direction')

    rate.sleep()