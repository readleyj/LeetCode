defmodule Solution do
  @spec largest_altitude(gain :: [integer]) :: integer
  def largest_altitude(gain) do
    {running_alts, _} = Enum.map_reduce([0] ++ gain, 0, fn x, acc -> {x + acc, x + acc} end)
    Enum.max(running_alts)
  end
end
