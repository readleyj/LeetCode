defmodule Solution do
  @spec find_words(words :: [String.t()]) :: [String.t()]
  def find_words(words) do
    row_sets =
      Enum.map(["qwertyuiop", "asdfghjkl", "zxcvbnm"], fn row ->
        MapSet.new(String.graphemes(row))
      end)

    Enum.filter(words, fn word ->
      Enum.any?(row_sets, fn row_set ->
        MapSet.subset?(String.downcase(word) |> String.graphemes() |> MapSet.new(), row_set)
      end)
    end)
  end
end
