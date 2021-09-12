defmodule Solution do
  @spec sum_of_unique(nums :: [integer]) :: integer
  def sum_of_unique(nums) do
    Enum.frequencies(nums)
    |> Enum.map(fn
      {num, 1} -> num
      {num, _} -> 0
    end)
    |> Enum.sum()
  end
end
