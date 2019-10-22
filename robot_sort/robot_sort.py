class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        OLD PLAN I HAD
        ------------------
        The robot is capable of moving left and right inside the list.
        The robot is capable of comparing an item he's holding vs the item he's looking at.
        The robot can swap items.

        The robot starts at position 0.
        Loop through the entire length of the list
            Pick up the item at position 0, then move right and compare the item you have to that item.
                If the item is larger than the one in the robot's hand, swap it.
            Go back through the list in the opposite direction, this time comparing in an opposite fashion
                if the item is smaller than the one in the robot's hand, swap it.
        
        -------------------------------------------

        The robot starts at position 0.
        Pick up the initial item.

        While the robot can move right, move him right.

            If the item he has is larger, swap the item.
                At this point, there's actually "None" in the position behind. 
                Move left, swap items with "None" (basically, the robot's hand is empty)
                Move back to the right, and swap "None" with the new card
            
            If the item has has is smaller, you want to place the card back down and pick up the new card:
                Move back to the left and "swap" the item with "None"
                Move back to the right and swap None with the new highest card
        
        Once the robot can not move right anymore, he is at the end of the array
        NEED A WAY TO TELL IF THE ROBOT HAS FINISHED MOVING ALL THE WAY RIGHT -- the robot's light
            The last item in the array will be a "None" because he just swapped with that position.
            Swap again with "None" so the robot's hand is empty.
            Move the robot all the way back to the beginning of the array
            While the robot can move left
                Move left until he can't move left anymore
            Reset the light
            RECURSION
            


        ------------------------------------------------
        
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.

        """
        self.swap_item()
        # self.set_light_on()

        while self.can_move_right():
            self.move_right()
             # self.set_light_on()

            if self.compare_item() == 1:
                self.set_light_on()
                self.swap_item()
                self.move_left()
                self.swap_item()
                self.move_right()
                self.swap_item()
            else:
                self.move_left()
                self.swap_item()
                self.move_right()
                self.swap_item()

            # continue
            # break
            
        else:
            self.swap_item()
            if self.light_is_on():
                while self.can_move_left():
                    self.move_left()
                self.set_light_off()
                self.sort() # ACTS AS A RESET, BINGO

        # while self.can_move_right():
        #     self.move_right()
        #     # print("Line 118: Moving right!")
        #     if self.compare_item() == 1:
        #         self.swap_item()
        #         self.move_left()
        #         self.swap_item()
        #         self.move_right()
        #         self.swap_item()
        #     elif self.compare_item() == -1:
        #         self.move_left()
        #         self.swap_item()
        #         self.move_right()
        #         self.swap_item()
        # else:
        #     while self.can_move_left():
        #         self.move_left()
        #         # print("Line 133: Moving left!")
        #         self.swap_item()
        #         self.move_left()
        #     if self.compare_item() == -1:
        #         self.swap_item()
        #         self.move_right()
        #         self.swap_item()
        #         self.move_left()
        #         self.swap_item()
        #     elif self.compare_item() == 1:
        #         self.move_right()
        #         self.swap_item()
        #         self.move_left()
        #         self.swap_item()
    
        # while self.can_move_left():
        #     self.move_left()
        #     if self.compare_item() == -1:
        #         self.swap_item()
        #         self.move_right()
        #         self.swap_item()
        #         self.move_left()
        #         self.swap_item()
        #     elif self.can_move_left() == False and self.compare_item() == None:
        #         break
        #     elif self.compare_item() == 1:
        #         self.move_left()

        # for i in (0, len(self._list)):
        #     while self.can_move_right():
        #         self.move_right()
        #         print(f"Line 117: Moving right!")
        #         if self.compare_item() == -1:
        #             self.swap_item()
        #         else:
        #             self.move_right()
            
        #     while self.can_move_left():
        #         print(f"Line 125: Moving left!")
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             self.move_left()
        #         else:
        #             self.move_left()



        # self.set_light_on()
        # for i in (0, len(self._list)):

        # while self.light_is_on():
        #     while self.can_move_right():
        #         self.move_right()
        #         print(f"Line 117: Moving right!")
        #         if self.compare_item() == -1:
        #             self.swap_item()
        #         else:
        #             self.move_right()
            
        #     while self.can_move_left():
        #         print(f"Line 125: Moving left!")
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             self.move_left()
        #         elif self.can_move_left() == False and self.compare_item() == None:
        #             self.set_light_off()
        #         else:
        #             self.move_left()
        
        # self.set_light_off()




# l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
# robot = SortingRobot(l)

# print(robot.can_move_right())
# print(robot.sort())
# print(robot._position)
# print(robot._item)
# print(robot._list)





if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)