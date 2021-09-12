defmodule Solution do
  def num_digits(0), do: 0
  def num_digits(num), do: num_digits(div(num, 10)) + 1

  @spec find_numbers(nums :: [integer]) :: integer
  def find_numbers(nums) do
    Enum.count(nums, &(rem(num_digits(&1), 2) == 0))
  end
end
