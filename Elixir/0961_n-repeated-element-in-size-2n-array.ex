defmodule Solution do
  @spec repeated_n_times(nums :: [integer]) :: integer
  def repeated_n_times(nums) do
    {num, _} =
      Enum.frequencies(nums)
      |> Enum.max_by(fn {_, freq} -> freq end)

    num
  end
end
