defmodule Solution do
  @alphabet_map for char <- ?a..?z, into: %{}, do: {<<char>>, false}

  @spec check_if_pangram(sentence :: String.t()) :: boolean
  def check_if_pangram(sentence) do
    Enum.reduce(String.graphemes(sentence), @alphabet_map, fn char, acc ->
      %{acc | char => true}
    end)
    |> Enum.all?(fn {_, v} -> v end)
  end
end
