# COMP1040: The Craft of Computing
#
# Agent class for implementing agent behaviour. Objects of this class
# are contained within an Engine object. The Engine object makes calls
# to various member functions of the Agent class.
#
# Modify locations in the code marked FIXME or TODO and run the associated
# unit tests to make sure your code is working. Once the unit tests have
# passed you should run the code in `simulation.py.`
#

import random
from constants import *

class Agent(object):

    def __init__(self, personality):
        """
        Constructor for the Agent class.

        :param personality: The personality type for this agent.
        :return: None
        """

        # TODO: Implement code to store the given personality in a member
        # variable. Also initialise any other member variables you think
        # you may need. Remember that member variables are prepended with
        # "self."

        self.personality = personality  #initial personality
        self.receiveMessage = []        #note message received



    def get_personality(self):
        """Return the personality for this agent."""

        # TODO: Replace the code below to return the personality type for
        # this agent. The personality type is the same as the one provided
        # during construction of the object. Remember that member variables
        # are prepended by "self."

        return self.personality

    def receive_message(self, friend_id, msg_id, msg_type):
        """
        Called whenever the agent receives a message from a friend.

        :param friend_id: An integer identifying the friend that sent the message.
        :param msg_id: An integer identifying the message being received. Each message
            has a unique id but the same messages can be received from different
            friends.
        :param msg_type: The type of message received, either MessageType.RED,
            MessageType.GREEN or MessageType.BLUE.
        :return: None
        """

        # TODO: Implement any operations you need to remember that a particular
        # message was received from a particular friend since you do not want
        # to send the same message back to that friend. You do not need to
        # use all the input arguments.

        # add received message to the variable receive_message
        self.receiveMessage.append([friend_id,msg_id,msg_type])
        return None

    def broadcast_new_message(self):
        """
        Called at the beginning of each epoch by the simulation engine to
        determine if the agent wants to send a message, and if so, of what
        type.

        :return: One of the three message types or None.
        """

        # TODO: Implement code that randomly decides whether to broadcast a
        # new message and, if so, of what type. The decision should be based
        # on the probabilities described in the README file.
        rand = random.random()  # generate a random float number between 0 and 1
        if self.personality == PersonalityType.CHATTY:
            if rand <= 0.3:
                return MessageType.RED
            if 0.3 < rand <= 0.4:
                return MessageType.GREEN
            if 0.4 < rand <= 0.6:
                return MessageType.BLUE
            if rand > 0.6:
                return None
        else:
            if rand <= 0.1:
                return MessageType.RED
            if 0.1 < rand <= 0.15:
                return MessageType.GREEN
            if 0.15 < rand <= 0.25:
                return MessageType.BLUE
            if rand > 0.25:
                return None

    def forward_message(self, friend_id, friend_personality, msg_id, msg_type):
        """
        Called by the simulation engine for each message that the agent has received
        and each of the agent's friends in the social network. The agent should
        determine whether to forward the message on to that friend.

        :param friend_id: An integer identifying the friend.
        :param friend_personality: The friend's personality type. Either
            PersonalityType.CHATTY or PersonalityType.QUIET.
        :param msg_id: An integer identifying the message. Note that even though each
            message has a unique identifier the same message may be received from
            different friends. As such this method may be called with the same msg_id
            multiple times.
        :param msg_type: The type of message to be forwarded, either MessageType.RED,
            MessageType.GREEN or MessageType.BLUE.
        :return: True of the agent wants to forward the message and False otherwise.
        """

        # TODO: Implement code that decides whether to forward the message to the
        # friend specified by `friend_id`. Your code should take into consideration
        # the forwarding rules outlined in the README file.
        for d in self.receiveMessage:
            if [friend_id, msg_id, msg_type] == d:
                return False

        rand = random.random()

        if self.personality == PersonalityType.CHATTY:
            if friend_personality == PersonalityType.QUIET:
                if rand <= 0.3:
                    return True
                else:
                    return False
            elif msg_type == MessageType.RED:
                if rand <= 0.5:
                    return True
                else:
                    return False
            elif msg_type == MessageType.GREEN:
                if rand <= 0.5:
                    return True
                else:
                    return False
            else:
                if rand <= 0.3:
                    return True
                else:
                    return False

        elif self.personality == PersonalityType.QUIET:
            if msg_type == MessageType.RED:
                if rand <= 0.1:
                  return True
                else:
                  return False
            elif friend_personality == PersonalityType.CHATTY:
                if msg_type == MessageType.GREEN:
                  if rand <= 0.9:
                    return True
                  else:
                    return False
                else:
                  if rand <= 0.1:
                    return True
                  else:
                    return False
            elif friend_personality == PersonalityType.QUIET:
                if msg_type == MessageType.GREEN:
                  if rand <= 0.3:
                    return True
                  else:
                    return False
                else:
                  if rand <= 0.3:
                    return True
                  else:
                    return False



