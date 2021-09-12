defmodule Solution do
  @spec are_occurrences_equal(s :: String.t()) :: boolean
  def are_occurrences_equal(s) do
    frequencies = Enum.frequencies(String.graphemes(s)) |> Enum.map(fn {_, freq} -> freq end)
    MapSet.size(MapSet.new(frequencies)) == 1
  end
end
