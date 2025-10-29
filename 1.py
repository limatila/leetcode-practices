class Solution:
    going_right: bool = True
    count_selections: int = 0

    def check_will_go_out_of_bounds(self, index: int, nums: list[int]):
        return (index - 1) < 0 or (index + 1) < len(nums) - 1

    def change_direction(self):
        self.going_right = not self.going_right

    def countValidSelections(self, nums: list[int]) -> int:
        current_index: int = 0
        list_possible_selections: list[int] = []

        while current_index < len(nums):
            if nums[current_index] == 0:
                list_possible_selections.append(current_index)
            current_index += 1

        for possible_selection in list_possible_selections:
            current_index = possible_selection
            nums_copy = list(nums)
            # if self.check_will_go_out_of_bounds(current_index, nums):
            #     print('skipado')
            #     continue

            while( current_index >= 0 and current_index < len(nums_copy) ):
                print(current_index)
                if nums_copy[current_index] > 0:
                    nums_copy[current_index] -= 1
                    self.change_direction()

                if self.going_right: 
                    current_index += 1
                else: 
                    current_index -= 1
        
            print('finished:', nums_copy)
            for number in nums_copy:
                if number > 0:
                    print('skipado')
                    continue
            self.count_selections += 1

        return self.count_selections
