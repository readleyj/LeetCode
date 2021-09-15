defmodule Solution do
  @spec missing_number(nums :: [integer]) :: integer
  def missing_number(nums) do
    n = length(nums)
    trunc((:math.pow(n, 2) + n) / 2) - Enum.sum(nums)
  end
end
