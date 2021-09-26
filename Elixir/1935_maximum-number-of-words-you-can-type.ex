defmodule Solution do
  @spec can_be_typed_words(text :: String.t(), broken_letters :: String.t()) :: integer
  def can_be_typed_words(text, broken_letters) do
    broken_letters_set = String.graphemes(broken_letters) |> MapSet.new()

    String.split(text)
    |> Enum.reduce(0, fn word, acc ->
      acc +
        Enum.reduce_while(String.graphemes(word), 1, fn char, acc ->
          if MapSet.member?(broken_letters_set, char), do: {:halt, 0}, else: {:cont, 1}
        end)
    end)
  end
end
