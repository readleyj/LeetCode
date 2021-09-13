defmodule Solution do
  @spec array_sign(nums :: [integer]) :: integer
  def array_sign(nums) do
    Enum.map(nums, fn
      num when num < 0 -> -1
      num when num > 0 -> 1
      _ -> 0
    end)
    |> Enum.product()
  end
end
