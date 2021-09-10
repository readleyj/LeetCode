defmodule Solution do
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    Enum.with_index(nums)
    |> Enum.reduce_while(%{}, fn {num, idx}, acc ->
      to_find = target - num

      case Map.has_key?(acc, to_find) do
        true -> {:halt, [acc[to_find], idx]}
        false -> {:cont, Map.put(acc, num, idx)}
      end
    end)
  end
end
