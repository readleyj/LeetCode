defmodule Solution do
  @spec unique_occurrences(arr :: [integer]) :: boolean
  def unique_occurrences(arr) do
    frequencies = Enum.frequencies(arr) |> Enum.map(fn {_, freq} -> freq end)
    size(MapSet.new(frequencies)) == length(frequencies)
  end
end
