defmodule Solution do
  @spec find_max_consecutive_ones(nums :: [integer]) :: integer
  def find_max_consecutive_ones(nums) do
    {max_ones, _} =
      Enum.reduce(nums, {0, 0}, fn num, {max_ones, current_ones} ->
        if num == 1, do: {max(max_ones, current_ones + 1), current_ones + 1}, else: {max_ones, 0}
      end)

    max_ones
  end
end
