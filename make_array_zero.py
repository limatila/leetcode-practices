# 3354. Make Array Elements Equal to Zero#


class Solution:
    going_right: bool = True
    count_selections: int = 0

    def change_direction(self, choice: bool = None):
        if choice is not None:
            self.going_right = choice
        else:
            self.going_right = not self.going_right

    def go_next_position(self, current_index: int) -> int:
        if self.going_right:
            current_index += 1
        else:
            current_index -= 1

        # print(current_index)
        return current_index

    def choose_starting_point(self, zero_selection: int) -> int:
        if self.going_right:
            return zero_selection - 1
        else:
            return zero_selection + 1

    def is_out_of_bounds(self, index: int, nums: list[int]) -> bool:
        return index < 0 or index > len(nums) - 1

    def will_go_out_of_bounds(self, index: int, nums: list[int]) -> bool:
        print(
            f"analysing bounds on: {index}, {'going right' if self.going_right else 'going left'}"
        )

        ultimo_index = len(nums) - 1

        if self.going_right:
            # checa se uma adição ao valor sair dos index
            return (index + 1) > ultimo_index
        else:
            # checa se uma remoção ao valor sair dos index
            return (index - 1) < 0

    def countValidSelections(self, nums: list[int]) -> int:
        current_index: int = 0
        list_possible_selections: list[int] = []

        while current_index < len(nums):
            if nums[current_index] == 0:
                list_possible_selections.append(current_index)
            current_index += 1

        for possible_selection in list_possible_selections:
            for direction_choice in [True, False]:
                self.change_direction(direction_choice)
                current_index = self.choose_starting_point(possible_selection)
                nums_copy = list(nums)
                if self.will_go_out_of_bounds(current_index, nums_copy):
                    print(
                        f"skipado out of bounds: {'going right' if self.going_right else 'going left'} para {nums_copy}"
                    )
                    continue

                print("starting loop:", nums_copy)
                print(current_index)
                while True:
                    current_index = self.go_next_position(current_index)
                    
                    if self.is_out_of_bounds(current_index, nums_copy):
                        break;

                    if nums_copy[current_index] > 0:
                        nums_copy[current_index] -= 1
                        self.change_direction()

                print("finished loop:", nums_copy)
                for number in nums_copy:
                    if number > 0:
                        print("skipado incompleto")
                        increment_count_selections = False
                        break
                    increment_count_selections = True

                if increment_count_selections:
                    self.count_selections += 1

        return self.count_selections
