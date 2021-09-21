defmodule Solution do
  @spec count_k_difference(nums :: [integer], k :: integer) :: integer
  def count_k_difference(nums, k) do
    nums_with_index = Enum.with_index(nums)

    for(
      {num_i, i} <- nums_with_index,
      {num_j, j} <- nums_with_index,
      i < j,
      do: abs(num_i - num_j)
    )
    |> Enum.count(&(&1 == k))
  end
end
