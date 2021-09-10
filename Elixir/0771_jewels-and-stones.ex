defmodule Solution do
  @spec num_jewels_in_stones(jewels :: String.t(), stones :: String.t()) :: integer
  def num_jewels_in_stones(jewels, stones) do
    jewels_set = MapSet.new(String.graphemes(jewels))

    Enum.count(String.graphemes(stones), &MapSet.member?(jewels_set, &1))
  end
end
