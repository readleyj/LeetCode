defmodule Solution do
  @spec first_uniq_char(s :: String.t()) :: integer
  def first_uniq_char(s) do
    uniq_char_set =
      String.graphemes(s)
      |> Enum.frequencies()
      |> Map.new()

    String.graphemes(s)
    |> Enum.with_index()
    |> Enum.reduce_while(-1, fn {char, idx}, acc ->
      if uniq_char_set[char] == 1, do: {:halt, idx}, else: {:cont, -1}
    end)
  end
end
