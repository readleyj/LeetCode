defmodule Solution do
  @spec frequency_sort(nums :: [integer]) :: [integer]
  def frequency_sort(nums) do
    frequencies = Enum.frequencies(nums)
    nums |> Enum.sort_by(&{frequencies[&1], -&1})
  end
end
