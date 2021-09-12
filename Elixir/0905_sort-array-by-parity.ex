defmodule Solution do
  @spec sort_array_by_parity(nums :: [integer]) :: [integer]
  def sort_array_by_parity(nums) do
    Enum.filter(nums, &(rem(&1, 2) == 0)) ++ Enum.filter(nums, &(rem(&1, 2) == 1))
  end
end
